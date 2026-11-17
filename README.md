# viral-shorts-clipper

Turn a YouTube or Twitch VOD, or any local video, into ready-to-post **9:16 vertical shorts** for TikTok, YouTube Shorts and Instagram Reels:

- **Auto moment detection.** Transcribes the stream and scores every second on loudness, on-screen motion and hype words ("oh my god", "no no no", "wasted", laughter...). It picks the best **action** moment and the best **reaction** moment, each 20–45 s, starting on a hook and ending right after the payoff.
- **Zero audio/video drift.** Video and audio are downloaded as separate streams and both re-timed to `0.000000s`. Every output is checked with `ffprobe`.
- **Viral framing.** Output is 1080x1920. A blurred, darkened gameplay background fills the frame, the facecam sits enlarged on top, and the gameplay is cropped to 3:4 below it (1080x1440 at y=480). Streams with no facecam get a bold two-line headline in the top band instead.
- **Hormozi karaoke subtitles.** Word-by-word timing from faster-whisper. Uppercase text in Montserrat ExtraBold 72 with a heavy black outline. The spoken word pops in electric yellow `#FFE500` at 115%.
- **GPU or CPU.** Uses NVIDIA NVENC (`h264_nvenc`) when it works and falls back to `libx264 -preset veryfast` otherwise.
- **Clean output.** All temporary files are deleted, so the output folder holds only the final `.mp4` files.

## Install

You need **Python 3.10+**, **FFmpeg** and **Node.js** (or Deno). yt-dlp needs a JavaScript runtime to solve YouTube's download challenge.

### Windows

```powershell
winget install Python.Python.3.12
winget install Gyan.FFmpeg --accept-package-agreements --accept-source-agreements
winget install OpenJS.NodeJS.LTS
```

Close and reopen the terminal so the new PATH entries load.

### macOS

```bash
brew install python ffmpeg node
```

### Linux (Debian/Ubuntu)

```bash
sudo apt install python3 python3-pip ffmpeg nodejs fonts-montserrat
```

### Then, on every OS

```bash
git clone https://github.com/BuildwShub/viral-shorts-clipper.git
cd viral-shorts-clipper
pip install -e .
```

Install the **Montserrat** font so the subtitles render correctly. On Windows and macOS, download it from https://fonts.google.com/specimen/Montserrat and install `Montserrat-ExtraBold.ttf`. You can also use a font you already have, for example `--font Impact`.

Check your setup:

```bash
python --version
ffmpeg -version
nvidia-smi
```

`nvidia-smi` is optional. If it is missing, rendering uses the CPU.

## Usage

Make 2 auto-detected shorts from a VOD:

```bash
shortsclip "https://www.youtube.com/watch?v=VIDEO_ID"
```

Common options:

```bash
# Streamer facecam in the top-right corner of a 1920x1080 stream (X:Y:W:H in source pixels)
shortsclip URL --facecam 1440:0:480:360

# Only scan one part of a long VOD (faster)
shortsclip URL --section 1:00:00-1:45:00

# Render exact ranges you already picked
shortsclip URL --clip 42:33-43:11 --clip 46:33-47:13

# No facecam: set the top headline yourself (second line is yellow)
shortsclip URL --headline "GLITCHED INTO|MICHAEL'S HOUSE" --headline "BLEW MYSELF UP|WASTED TWICE"

# Local file, 3 clips, larger Whisper model, output to a folder
shortsclip stream.mp4 -n 3 --model medium -o shorts/
```

The output looks like this:

```
Done. Both streams verified to start at 0.000000s.

  C:\clips\My_Stream_short1_action.mp4
     source 00:46:33 - 00:47:13  (39.4s, action)
  C:\clips\My_Stream_short2_reaction.mp4
     source 00:42:33 - 00:43:11  (38.0s, reaction)
```

Run `shortsclip --help` for every option.

### Finding the facecam box

Take a screenshot of the stream at full resolution, for example with `ffmpeg -ss 60 -i stream.mp4 -frames:v 1 shot.png`. Open it in Paint or any image editor. Read the facecam's top-left corner (X, Y) and its width and height (W, H), then pass `--facecam X:Y:W:H`.

### Moving the gameplay crop

By default the 3:4 gameplay crop is centred on the frame, where the crosshair usually is. To shift it, pass `--crop-center FX:FY` as fractions of the width and height. For example, `--crop-center 0.4:0.5` moves the crop left.

## YouTube "Sign in to confirm you're not a bot"

YouTube sometimes blocks downloads, especially from servers and VPNs. Export cookies from a logged-in browser and pass them in:

1. In a private/incognito window, log into YouTube with a **throwaway** Google account.
2. Use the "Get cookies.txt LOCALLY" browser extension to export `cookies.txt` (Netscape format).
3. Run `shortsclip URL --cookies cookies.txt`.

> **Security:** a cookies file gives full access to that Google account. Never use your main account, never commit the file (`.gitignore` already blocks `cookies*.txt`), and sign the account out of all devices when you are done.

If you see `n challenge solving failed` or `No video formats found`, yt-dlp could not run its JavaScript solver. Install Node.js and add:

```bash
--ytdlp-arg=--js-runtimes=node --ytdlp-arg=--remote-components=ejs:github
```

You can also put those two flags in your yt-dlp config file (`%APPDATA%\yt-dlp\config` on Windows, `~/.config/yt-dlp/config` on macOS/Linux) so they apply every time.

## Live streams

A stream that is **still live** cannot be clipped directly. Wait for the VOD, or record it yourself and pass the local file:

```bash
yt-dlp --live-from-start -o stream.mp4 URL
shortsclip stream.mp4
```

## How moment detection works

1. faster-whisper transcribes the whole source with word-level timestamps.
2. Each second gets three scores: loudness (RMS), motion (frame difference) and a hype-word score.
3. **Action score** = motion + loudness + hype. **Reaction score** = hype + loudness + speech rate.
4. Every 20–45 s window is ranked by its average score plus its biggest peak.
5. The best action window and the best non-overlapping reaction window are kept.
6. Cuts are snapped to sentence starts (hook) and word ends (payoff).

Not happy with the picks? Look at the printed timestamps, then re-run with `--clip` and your own ranges.

## License

MIT
