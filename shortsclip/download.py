"""Fetch the source: separate best video and audio streams via yt-dlp, or a local file."""
import json
import os
import subprocess
import sys


def _ytdlp(args):
    return subprocess.run([sys.executable, "-m", "yt_dlp", *args], check=True,
                          capture_output=True, text=True).stdout


def fetch(source, workdir, cookies=None, section=None, max_height=1080, extra_args=()):
    """Return dict(video, audio, title, offset).

    offset: seconds into the original stream where the downloaded media starts
    (non-zero when a --section was requested).
    """
    if os.path.isfile(source):
        title = os.path.splitext(os.path.basename(source))[0]
        return {"video": source, "audio": source, "title": title, "offset": 0.0}

    base = ["--no-warnings", "--no-playlist", "--no-part", *extra_args]
    if cookies:
        base += ["--cookies", cookies]
    offset = 0.0
    if section:
        base += ["--download-sections", f"*{section[0]}-{section[1]}"]
        offset = float(section[0])

    info = json.loads(_ytdlp([*base, "--skip-download", "--dump-json", source]))
    if info.get("is_live"):
        sys.exit("This is a live stream that is still running. Wait for the VOD, "
                 "or download it yourself and pass the local file.")

    # Video and audio are downloaded as separate DASH streams and never merged
    # with -c copy; the renderer re-times both to 0 (zero drift).
    out = {}
    for kind, fmt in (("video", f"bv*[height<={max_height}]/b[height<={max_height}]/bv*"),
                      ("audio", "ba/b")):
        path = _ytdlp([*base, "-f", fmt, "-o", os.path.join(workdir, f"src_{kind}.%(ext)s"),
                       "--print", "after_move:filepath", source]).strip().splitlines()[-1]
        out[kind] = path
    out["title"] = info.get("title") or info.get("id") or "clip"
    out["offset"] = offset
    return out
