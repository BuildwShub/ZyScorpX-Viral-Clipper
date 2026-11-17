"""Render one 9:16 short: zero-drift slice, facecam-top framing, karaoke subtitles."""
import json
import os
import subprocess

YELLOW = r"\c&H00E5FF&"  # #FFE500 in ASS BGR order


def probe_size(path):
    s = json.loads(subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height", "-of", "json", path]))["streams"][0]
    return s["width"], s["height"]


_ENCODER = None


def encoder():
    """NVENC when it actually works on this machine, else CPU libx264."""
    global _ENCODER
    if _ENCODER is None:
        test = subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "color=s=256x256:d=0.2",
                               "-c:v", "h264_nvenc", "-f", "null", "-"], capture_output=True)
        _ENCODER = (["-c:v", "h264_nvenc", "-preset", "p4", "-b:v", "8M", "-maxrate", "10M",
                     "-bufsize", "16M"] if test.returncode == 0 else
                    ["-c:v", "libx264", "-preset", "veryfast", "-crf", "19", "-maxrate", "8M",
                     "-bufsize", "16M"])
    return _ENCODER


def _ts(t):
    t = max(t, 0.0)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def _esc(s):
    return s.replace("\\", "/").replace("{", "(").replace("}", ")")


def build_ass(words, duration, font, headline=None):
    """Word-by-word Hormozi karaoke. words: (start, end, text) relative to clip start."""
    out = [
        "[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 2", "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, "
        "Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        f"Style: K,{font},72,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,6,3,5,40,40,0,1",
        f"Style: H,{font},64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,6,3,5,40,40,0,1",
        "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]
    if headline:  # only used when there is no facecam to fill the top band
        a, _, b = headline.upper().partition("|")
        txt = _esc(a) + (r"\N{" + YELLOW + "}" + _esc(b) if b else "")
        out.append(f"Dialogue: 1,{_ts(0)},{_ts(duration)},H,,0,0,0,,{{\\pos(540,240)\\bord6\\shad3}}{txt}")

    chunks, cur = [], []
    for w in words:
        if cur and (len(cur) == 3 or w[0] - cur[-1][1] > 0.6):
            chunks.append(cur)
            cur = []
        cur.append(w)
    if cur:
        chunks.append(cur)
    for chunk in chunks:
        for i, (ws, we, _) in enumerate(chunk):
            end = chunk[i + 1][0] if i + 1 < len(chunk) else we
            parts = [("{" + YELLOW + r"\fscx115\fscy115}" + _esc(t.upper()) + r"{\r}") if j == i
                     else _esc(t.upper()) for j, (_, _, t) in enumerate(chunk)]
            out.append(f"Dialogue: 0,{_ts(ws)},{_ts(max(end, ws + 0.05))},K,,0,0,0,,"
                       f"{{\\pos(540,620)\\bord6\\shad3}}" + " ".join(parts))
    return "\n".join(out) + "\n"


def render(video, audio, start, duration, out_path, words, workdir, *, facecam=None,
           crop_center=(0.5, 0.5), headline=None, font="Montserrat ExtraBold"):
    """facecam: (x, y, w, h) in source pixels, or None. crop_center: gameplay crop centre (0-1)."""
    W, H = probe_size(video)
    # Gameplay: 3:4 crop. 540x720 on a 1080p source, same proportion on other sizes.
    ch = int(round(H * 720 / 1080)) // 2 * 2 if H > 720 else H // 2 * 2
    cw = int(round(ch * 3 / 4)) // 2 * 2
    x0 = int(min(max(crop_center[0] * W - cw / 2, 0), W - cw))
    y0 = int(min(max(crop_center[1] * H - ch / 2, 0), H - ch))

    rel = [(s - start, e - start, t) for s, e, t in words if s >= start and e <= start + duration]
    ass_name = "subs_" + os.path.splitext(os.path.basename(out_path))[0] + ".ass"
    with open(os.path.join(workdir, ass_name), "w", encoding="utf-8") as f:
        f.write(build_ass(rel, duration, font, None if facecam else headline))

    # Rule A: both streams re-timed to 0 and audio resampled against drift.
    fc = ["[0:v]setpts=PTS-STARTPTS,fps=30,split=3[a][b][c]",
          "[1:a]asetpts=PTS-STARTPTS,aresample=async=1[aout]",
          "[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
          "boxblur=25:2,eq=brightness=-0.15[bg]",
          f"[b]crop={cw}:{ch}:{x0}:{y0},scale=1080:1440:flags=lanczos[gp]"]
    if facecam:
        fx, fy, fw, fh = facecam
        fc.append(f"[c]crop={fw}:{fh}:{fx}:{fy},scale=620:490:force_original_aspect_ratio=decrease[cam]")
        fc.append("[bg][gp]overlay=0:480[t1]")
        fc.append("[t1][cam]overlay=(W-w)/2:max((480-h)/2\\,0)[t2]")
    else:
        fc.append("[c]nullsink")
        fc.append("[bg][gp]overlay=0:480[t2]")
    fc.append(f"[t2]ass={ass_name}[vout]")

    # cwd=workdir keeps the subtitle path relative (Windows drive letters break the ass filter).
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start:.3f}", "-i", os.path.abspath(video),
                    "-ss", f"{start:.3f}", "-i", os.path.abspath(audio), "-t", f"{duration:.3f}",
                    "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]", *encoder(),
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", os.path.abspath(out_path)],
                   check=True, cwd=workdir)
    return verify(out_path)


def verify(path):
    """Both streams must start at 0.000000s."""
    streams = json.loads(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,start_time,duration",
         "-of", "json", path]))["streams"]
    starts = {s["codec_type"]: float(s.get("start_time", 0)) for s in streams}
    if any(abs(v) > 0.001 for v in starts.values()):
        raise RuntimeError(f"A/V start offset detected in {path}: {starts}")
    return starts
