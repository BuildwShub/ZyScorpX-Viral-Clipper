"""shortsclip: turn a YouTube/Twitch VOD (or local video) into viral 9:16 shorts."""
import argparse
import os
import re
import shutil
import sys
import tempfile

from . import analyze, download, render


def _time(s):
    """Accept 90, 1:30 or 01:01:30 (seconds or [hh:]mm:ss)."""
    parts = [float(p) for p in str(s).split(":")]
    t = 0.0
    for p in parts:
        t = t * 60 + p
    return t


def _range(s):
    a, b = s.split("-", 1)
    return _time(a), _time(b)


def _hms(t):
    t = int(round(t))
    return f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"


def _slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")[:40] or "clip"


def check_tools():
    missing = [t for t in ("ffmpeg", "ffprobe") if not shutil.which(t)]
    if missing:
        sys.exit(f"Missing {', '.join(missing)} in PATH. See README > Install.")


def main(argv=None):
    p = argparse.ArgumentParser(prog="shortsclip", description=__doc__)
    p.add_argument("source", help="YouTube/Twitch URL or a local video file")
    p.add_argument("-n", "--clips", type=int, default=2, help="number of shorts to make (default 2)")
    p.add_argument("--min", type=int, default=20, help="min clip length in seconds (default 20)")
    p.add_argument("--max", type=int, default=45, help="max clip length in seconds (default 45)")
    p.add_argument("--clip", action="append", type=_range, metavar="START-END",
                   help="render this exact range instead of auto-detecting (repeatable), e.g. 42:33-43:11")
    p.add_argument("--section", type=_range, metavar="START-END",
                   help="only download/scan this part of a long VOD, e.g. 1:00:00-1:30:00")
    p.add_argument("--facecam", metavar="X:Y:W:H",
                   help="facecam box in source pixels; omit if the stream has no facecam")
    p.add_argument("--crop-center", default="0.5:0.5", metavar="FX:FY",
                   help="gameplay crop centre as fractions of width:height (default 0.5:0.5)")
    p.add_argument("--headline", action="append", metavar="'LINE 1|LINE 2'",
                   help="top-band headline when there is no facecam (one per clip, repeatable)")
    p.add_argument("--font", default="Montserrat ExtraBold", help="subtitle font (e.g. Impact)")
    p.add_argument("--model", default="small", help="faster-whisper model: tiny/base/small/medium/large-v3")
    p.add_argument("--language", default=None, help="speech language code, e.g. en (default: auto)")
    p.add_argument("--cookies", help="cookies.txt for YouTube bot checks (Netscape format)")
    p.add_argument("--max-height", type=int, default=1080, help="max source resolution (default 1080)")
    p.add_argument("--ytdlp-arg", action="append", default=[], metavar="ARG",
                   help="extra raw yt-dlp argument (repeatable), e.g. --ytdlp-arg=--js-runtimes=node")
    p.add_argument("-o", "--out", default=".", help="output folder (default: current folder)")
    p.add_argument("--keep-temp", action="store_true", help="keep the temp folder for debugging")
    a = p.parse_args(argv)

    check_tools()
    os.makedirs(a.out, exist_ok=True)
    work = tempfile.mkdtemp(prefix="shortsclip_")
    try:
        print("[1/4] Fetching source ...", flush=True)
        src = download.fetch(a.source, work, a.cookies, a.section, a.max_height, a.ytdlp_arg)
        off = src["offset"]

        print(f"[2/4] Transcribing with faster-whisper ({a.model}) ...", flush=True)
        pcm = analyze.load_audio(src["audio"])
        words = analyze.transcribe(pcm, a.model, language=a.language)

        if a.clip:
            moments = [{"start": s - off, "end": e - off, "kind": "manual"} for s, e in a.clip]
        else:
            print("[3/4] Scoring loudness, motion and hype words ...", flush=True)
            loud = analyze.loudness(pcm)
            mot = analyze.motion(src["video"], len(loud))
            moments = analyze.find_moments(words, loud, mot, a.clips, a.min, a.max)
        if not moments:
            sys.exit("No moments found (source too short?).")

        print(f"[4/4] Rendering {len(moments)} short(s) with {render.encoder()[1]} ...", flush=True)
        facecam = tuple(int(v) for v in a.facecam.split(":")) if a.facecam else None
        cc = tuple(float(v) for v in a.crop_center.split(":"))
        results = []
        for i, m in enumerate(moments, 1):
            dur = m["end"] - m["start"]
            clip_words = [w for w in words if m["start"] <= w[0] < m["end"]]
            headline = (a.headline[i - 1] if a.headline and i <= len(a.headline)
                        else " ".join(w[2] for w in clip_words[:5]))
            name = f"{_slug(src['title'])}_short{i}_{m['kind']}.mp4"
            out = os.path.join(a.out, name)
            render.render(src["video"], src["audio"], m["start"], dur, out, words, work,
                          facecam=facecam, crop_center=cc, headline=headline, font=a.font)
            results.append((out, m["start"] + off, m["end"] + off, m["kind"]))

        print("\nDone. Both streams verified to start at 0.000000s.\n")
        for out, s, e, kind in results:
            print(f"  {os.path.abspath(out)}\n     source {_hms(s)} - {_hms(e)}  ({e - s:.1f}s, {kind})")
    finally:
        if a.keep_temp:
            print(f"Temp kept at {work}")
        else:
            shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
