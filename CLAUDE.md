# Project memory: viral shorts for ZyScorpX

This repo holds `shortsclip`, a tool that turns YouTube/Twitch videos into vertical shorts. This file is the
standing brief for any Claude session that edits videos for this creator. Read it fully before starting.

## Creator accounts (put these on every post)

| Platform | Handle | Link |
|---|---|---|
| Instagram | zyscorpx.tv | https://www.instagram.com/zyscorpx.tv/ |
| YouTube | @ZyScorpXTV | https://www.youtube.com/@ZyScorpXTV |
| X | @ZyScorpX | https://x.com/ZyScorpX |

Niche: GTA 6 / GTA 5 gaming news, comparisons and gameplay moments. Posts to YouTube Shorts, Instagram Reels and X.

## Standard deliverable for "give me N viral clips from <URL>"

1. N vertical videos, 1080x1920, 30 fps, H.264 + AAC, 20–60 s each, burned-in captions.
2. One cover image per video (1080x1920 JPG), same style as the existing grid (see "Thumbnail style").
3. Per video, ready-to-paste text in fenced code blocks:
   - **Instagram caption**: hook sentence with emojis, question CTA + 👇, then
     `🎥 Credit: <Source channel> (YouTube)` and `📲 YT: @ZyScorpXTV | X: @ZyScorpX`, then 12 hashtags.
   - **YouTube**: title (< 100 chars, ends `#Shorts`), description (keyword-rich first line, CTA,
     `🎥 Original footage: <channel> – <source URL>`, then the follow block below, then 3–4 hashtags
     incl. `#Shorts`), and a comma-separated tags line.
   - **X post** (< 280 chars): one-line hook, `🎥 <channel>`, `📺 youtube.com/@ZyScorpXTV | 📸 IG: zyscorpx.tv`, `#GTA6`.
4. A table: file name, source timestamp range, length.
5. Copyright reminder: footage belongs to the source creator; always keep the credit line.

YouTube follow block:
```
📲 Follow for more GTA 6:
Instagram: https://www.instagram.com/zyscorpx.tv/
YouTube: https://www.youtube.com/@ZyScorpXTV
X: https://x.com/ZyScorpX
```

Base hashtags: `#gta6 #gtavi #grandtheftauto #rockstargames #gaming #gamingnews #ps5 #xbox #viral #fyp` + 2 topic tags.
Comparison videos use `#gta6 #gta5 #gta6vsgta5 ...`. Remind the user to leave Instagram's "AI label" off (real game footage).

Output folders go under `/home/user/<Topic>_Shorts/` with covers in a `thumbnails/` subfolder. Files are named
`NN_Short_Title.mp4` and `NN_Short_Title_thumbnail.jpg`. Send them with SendUserFile and remind the user to
download them, because the cloud container is deleted after inactivity.

## Technical rules (always)

- **A. Zero drift.** Never cut DASH video/audio with `-c copy`. Download video and audio as separate
  streams, then re-time both: `[0:v]setpts=PTS-STARTPTS` and `[1:a]asetpts=PTS-STARTPTS,aresample=async=1`.
  Verify with ffprobe that both streams start at `0.000000` (`shortsclip.render.verify`).
- **B. Encoder.** Use `h264_nvenc -preset p4 -b:v 8M` if it works, else `libx264 -preset veryfast -crf 19`
  (`shortsclip.render.encoder()`). Cloud containers have no GPU.
- **C. Captions.** ASS file, Montserrat ExtraBold, uppercase, size 72, white, `\bord6\shad3`. The spoken word
  pops in yellow `\c&H00E5FF&` (#FFE500) at `\fscx115\fscy115`, in chunks of up to 3 words
  (`shortsclip.render.build_ass`). Word timings come from faster-whisper `small`. If the video has no
  narration, write short descriptive captions timed to the action and spread the word-pop evenly across each line.
- **D. Cleanup.** Delete every temp file (slices, frames, .ass, .wav, scripts). Output folders hold only the
  final .mp4 files (and covers in `thumbnails/`).
- Check captions against the visuals before delivering. Grab frames and look at them. Do not claim
  "same car" and so on unless it is true.

## Layouts (pick by source type)

1. **Streamer with facecam** (repo default): blurred, darkened background (`boxblur=25:2,eq=brightness=-0.15`),
   facecam ~620x490 at the top (y 0–480), gameplay cropped to 3:4 and scaled to 1080x1440 at y=480, captions at
   `\pos(540,620)`. No facecam: a two-line headline in the top band (`\pos(540,240)`, line 2 yellow).
2. **Voice-over explainer / news video** (e.g. Hollywood GTA): blurred background, the full 16:9 frame scaled to
   1080x608 at y=656 (keeps infographics readable), headline at `\pos(540,480)`, captions below the frame at
   `\pos(540,1430)`.
3. **GTA 5 vs GTA 6 comparison** (e.g. GameV): dark #0b0b0b canvas. Header "GTA 5  VS  GTA 6" (white, 50,
   y=68) plus the topic (yellow Montserrat Black 92, y=160). GTA 5 panel 1080x810 at y=230, GTA 6 panel at y=1050,
   a 10 px yellow seam between them, a "GTA 5" pill (white) and a "GTA 6" pill (yellow) at the panels' top-left,
   captions on the seam at `\pos(540,1045)`. Full-screen source crop: `crop=1440:1080:240:0`. Split-screen
   source: left half `crop=960:720:0:180`, right half `crop=960:720:960:180`, each scaled to 1080x810.
   **Sync the key moment** (explosion, impact, first punch) in both panels using audio RMS peaks. Mix both
   audio tracks (`amix` weights 0.75/0.75), or use the single track for split-screen sources. Several rounds
   per short are joined with `concat`.

## Thumbnail style (the account's grid look; keep it consistent)

- 1080x1920 JPG, quality 95. Only y 240–1680 shows on the Instagram 3:4 profile grid, so keep text there.
- Background: a full-bleed key frame cropped to 9:16 (skip the source's top ~11% chapter or logo strip and the
  bottom ~15% burned-in captions/HUD), upscaled with lanczos, unsharp mask, color ×1.2, contrast ×1.08.
- Dark gradients: top 0–420 px (alpha 150→0), bottom from y=900 (alpha 0→235).
- Yellow (#FFE500) rounded pill tag centered at y=300: Montserrat Black 54, black text ("GTA 6", or
  "GTA 5 VS GTA 6" for comparisons).
- Hook: 2 lines of Montserrat Black up to 190 px, fit to 960 px wide, line 1 white and line 2 yellow, black
  stroke 12 plus a blurred drop shadow, baseline of line 2 at y=1520. Use short punchy claims
  ("3X BIGGER / THAN RDR2", "NO KEY? / NO CAR.", "GO FULL / PSYCHO").
- **Comparison covers** (approved version): GTA 5 frame on top (0–960), GTA 6 frame below (960–1920), a
  10 px yellow seam, small "GTA 5" / "GTA 6" pills at each panel's bottom-left, the same centered pill tag
  "GTA 5 VS GTA 6", and the hook straddling the seam (white line just above it, yellow line just below it)
  with a soft dark band behind it, so the action in both panels stays visible.
- Pick frames by extracting exact timestamps with `ffmpeg -ss T -i src -frames:v 1` and viewing them.
  (Contact sheets built with the `fps=` filter label frames about one step early, so do not trust their labels.)

## Environment gotchas (cloud container)

- YouTube bot check: yt-dlp needs a cookies file from a throwaway account in `/root/.config/yt-dlp/cookies.txt`
  plus `--js-runtimes node --remote-components ejs:github`, both kept in `/root/.config/yt-dlp/config`. If the
  container was reset, ask the user to upload `cookies.txt` again. Never commit cookies.
- ffmpeg does not use `HTTPS_PROXY`. Run `export http_proxy=$HTTPS_PROXY` before yt-dlp, which hands
  HLS/live downloads to ffmpeg.
- faster-whisper and PyAV can mismatch (`metadata_errors` TypeError). Decode audio with ffmpeg into a numpy
  float32 array and pass that instead (`shortsclip.analyze.load_audio`).
- Install the Montserrat font with `apt-get install -y fonts-montserrat` if `fc-list | grep Montserrat` is empty.
- Live streams: `--live-from-start` cannot do `--download-sections`. Hard-link the fragment files before
  stopping yt-dlp, and never `rm full.*` while it may be merging.
- The GitHub repo is `BuildwShub/viral-shorts-clipper`. Do **not** add a `Co-Authored-By: Claude` line to
  commits (the user removed it from Contributors).

## History (already published, do not repeat)

- GTA 6 explainer "Everything You NEED To Know" (Hollywood GTA, youtu.be/4ykW64CwrWU): 10 reels posted
  (map size, real Miami or GTA 6, stealing cars, 6 stars/cops, robbing, 600K animations, body changes,
  psycho profile, PS5 Pro 30 FPS, New Zealand early unlock).
- GTA 6 vs GTA 5 comparison (GameV, youtu.be/2qGZp_Lkbc4): 5 shorts (explosions, crash physics, car damage,
  water physics, fights & guns) with comparison covers.
- A GTA countdown live stream (Fresh Gaming): 2 test clips.
- GTA 6 launched on 2026-11-19. Drop "launches tonight" wording from now on.
