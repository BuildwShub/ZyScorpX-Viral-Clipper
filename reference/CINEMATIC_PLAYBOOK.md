# ZyScorpX Cinematic Video Playbook

> **For any AI assistant or editor:** this file is your complete brief for making cinematic GTA 6 videos for the
> creator **ZyScorpX**. Read all of it before doing anything. It is self-contained: it describes the target
> style, the workflow, the technical pipeline, the quality checks, the outro, the post text, and the mistakes
> the creator has already rejected. Follow it exactly. When something here conflicts with your own habits, this
> file wins. When something is not covered, ask the creator; don't guess.

---

## 0. Ten rules that are never broken

1. **Hook in the first 1–2 seconds:** a spoken or typed question/claim, or the single most striking shot.
   Never a logo, "presents" card or slow establishing shot first.
2. **One idea, one arc:** every video has a premise a viewer could repeat in one sentence, built as
   **setup → turn → DROP → payoff**.
3. **Kinetic typography, not subtitles:** words appear as they are spoken, stacked in mixed fonts in the frame.
   The key word is huge and in the GTA VI gradient.
4. **Only the best shots:** golden hour, neon, aerials, explosions, speed, faces looking into the lens.
   No HUD, no facecam, no menus, no walking from behind, no dull interiors.
5. **The music drives the edit:** every cut lands on a beat. The drop lands on the most spectacular shot.
6. **Seamless audio:** dialogue sits inside the music with smooth ducking and crossfades, never a hard cut.
7. **Zero stutter:** no dropped or repeated frames. Render in one pass and check it with tools.
8. **Every video ends with the ZyScorpX outro** (section 9), in every format.
9. **Approval gate:** send the creator the concept, hook and shot outline, and get a "yes" **before**
   rendering. Never batch-produce several videos on an idea the creator hasn't approved.
10. **No "trailer" or "out now" wording.** GTA 6 launched on 2026-11-19. Credit the source creators in the
    post text only, never on screen.

---

## 1. Who this is for

| Platform | Handle | Link |
|---|---|---|
| Instagram | zyscorpx.tv | https://www.instagram.com/zyscorpx.tv/ |
| YouTube | @ZyScorpXTV | https://www.youtube.com/@ZyScorpXTV |
| X | @ZyScorpX | https://x.com/ZyScorpX |

Niche: GTA 6 (and GTA 5 nostalgia), gameplay moments and cinematic edits. Posts to YouTube Shorts, Instagram
Reels and X. Brand colours: GTA VI gradient magenta/pink **#FF4FA3** → orange **#FFB047**, accent yellow
**#FFE500**, neon pink **#FF4FA3**. GitHub repo with the tools: `BuildwShub/ZyScorpX-Viral-Clipper`
(public; never commit cookies, third-party video or music).

---

## 2. The reference: what "cinematic" means for this channel

The **only** approved reference is the creator's clip `Clipping_Campaigns.mp4` (40.8 s, 1280x720, 30 fps; an
edit signed "zaid."). If you can see the file, study it. If you can't, the breakdown below is exact
(measured frame by frame).

### 2.1 Structure (copy this arc)

| Time | Section | What happens |
|---|---|---|
| 0.0–1.7 s | **Hook** | A black screen. A narrator asks "Why did I move here?" and the words build up one by one in mixed fonts. |
| 1.7–10 s | **Setup / nostalgia** | Slow, gorgeous GTA 5 shots (a helicopter over Los Santos at sunset, Route 68, bikers, casino roulette, a jet over the skyline). Voice-over: "I guess it was the weather… or the… that thing… that magic." Every phrase is typeset over its shot. |
| ≈10 s | **Turn** | "THAT MAGIC" in a huge gradient with a helicopter flying **in front of** the text, then the GTA V logo morphs into the GTA VI logo. |
| 10–18 s | **New world** | Leonida: sunset highways, Vice City neon, the Keys from above, characters. Character lines: "You see her?" plus the name **LUCIA** in elegant italic, "Do you know why you're here?", "Bad luck, I guess." |
| 18–19.6 s | **Transition** | A white canvas with a pink/blue gradient band. A collage of many small GTA 6 clips slides in and stacks up ("the whole world" moment). |
| ≈20 s | **DROP** | The beat drops (loudness jumps from about −15 dB to about −6 dB) on a spectacular shot. |
| 20–37.5 s | **Action** | Rapid beat-synced cuts: shootouts, explosions, a police chase, a speedboat, motorcycles, a helicopter, character close-ups. One character line breaks through ("Hands above your head!") and the hook line returns as a refrain ("You know why you're here"). |
| 37.5–38.4 s | **Logo moment** | A golden-hour city shot with a small "VI" logo in the gradient. |
| end | **Outro** | For ZyScorpX: the channel outro (section 9). |

### 2.2 Pacing

- 92 cuts in 40.8 s, an average of **0.44 s per shot**. The setup breathes (0.5–2.5 s shots); after the drop,
  cuts are 1–6 frames on beats and impacts.
- Tension builds for 15–20 s, then the drop releases it. **The drop is the emotional peak, not the start.**
- Target length: **30–45 s plus the 5 s outro.**

### 2.3 Typography (the signature look)

- **Word-by-word, synced to speech:** each word appears exactly when it is said and builds a stacked lockup
  near the centre of the frame. There are no subtitle-style captions at the bottom of the frame.
- **Mixed typefaces inside one phrase.** Example lockup for "why DID I MOVE HERE?":
  - a heavy geometric sans, all caps (**Montserrat Black/ExtraBold** or **Archivo Expanded Black**): "DID", "HERE?";
  - a condensed italic serif (**Playfair Display Italic** or **Bodoni Moda Italic**, condensed with `\fscx80`):
    "I MOVE", "I GUESS";
  - a light italic/script (**Playfair Display Italic** light, or **Great Vibes** sparingly): "was", "why", "you're";
  - a wide, letter-spaced sans (**Archivo Expanded**, tracking +40): "T H A T".
- **The key emotional word is huge** (fills about 40–60 % of the frame width) and filled with the GTA VI
  gradient #FF4FA3→#FFB047, e.g. "MAGIC". Dramatic words can be red condensed caps (#E8202A), e.g. "BAD LUCK".
- **Character names** are in elegant italic serif with a pink→gold gradient, e.g. "LUCIA", "JASON".
- **Depth:** on 1–3 hero shots per video, put the text **behind** the foreground subject (a helicopter or
  person passes in front of it) using a subject mask (rembg/SAM on those frames). Text can also be pinned to
  a moving object (motion tracking).
- The text is white or a gradient with a soft drop shadow. There are no boxes, pills, outlines or emoji on screen.
- Get fonts from Google Fonts (github.com/google/fonts, `ofl/...`). Montserrat: `apt-get install -y fonts-montserrat`.

### 2.4 Picture

- **Golden hour and neon:** warm orange/pink/magenta sunsets against deep teal/blue nights. Average saturation is
  high (about 0.42). Grade: contrast ×1.07, saturation ×1.15, cool shadows/warm highlights, light vignette.
- Shot priority: aerials and skylines at sunset → explosions/fire → vehicles at speed → characters looking
  into the lens → neon nights → water/boats.
- **Forbidden on screen:** HUD (minimap, prompts, objective text, weapon wheel, reticle, vehicle-name labels),
  streamer facecam, subtitles burned in by the game, cutscene letterbox bars, menus, nudity, and dark,
  muddy or static shots.

### 2.5 Audio

- One moody, cinematic track that **builds and then drops** (≈15–20 s in). The music is the spine.
- A **voice-over** at the start (a narrator's question/claim) plus 2–5 short, punchy **character lines**,
  each typeset on screen. Where does the VO come from? Ask the creator: their own recording, or real game
  dialogue only. **Never AI-synthesised voices or music** unless the creator explicitly asks.
- The refrain: repeat the hook line once near the end for closure.

---

## 3. Workflow (follow in this order)

1. **Brief:** confirm with the creator the source video(s)/footage, the number of videos, the format
   (default: **9:16 1080x1920 for Shorts/Reels**, plus a 16:9 1920x1080 master if asked), the music track,
   and the VO source.
2. **Environment setup** (section 11). Ask for a fresh YouTube `cookies.txt` if YouTube blocks downloads.
3. **Mine the source:** download it (section 11), transcribe it **with word timings**, find the cutscenes
   (letterbox detection), find action (motion/loudness peaks), and build contact sheets. Note every great
   shot with exact timestamps.
4. **Concept pitch (STOP for approval):** for each video send:
   - the **one-sentence premise**;
   - the **hook** (the exact first 2 s: the shot plus the words on screen);
   - the **arc** (setup → turn → drop → payoff) with the exact dialogue lines and their timestamps;
   - a **shot outline** (8–15 key shots with timestamps) and the music section (start time, drop time);
   - the title idea.
   Do not render until the creator says yes.
5. **Build:** cut list on a beat grid → one-pass render → typography → grade → audio mix → outro.
6. **QA** (section 8). Fix anything that fails and re-run QA.
7. **Deliver** (section 10): videos, covers, post text, a zip, and a reminder to download.
8. **Clean up:** delete the temp files and the source download once the creator approves.

---

## 4. Footage rules

- **Source:** 4K60 when available (`yt-dlp -f 315` VP9 2160p60, or 401 AV1, plus best audio).
- **Facecam removal:** crop it out; never blur it or paint over it. Typical streamer layout: facecam at
  x ≥ 0.78·W, y ≤ 0.30·H. Choose crop windows that end left of the facecam or start below it.
- **HUD-safe area (typical):** keep crops above y = 0.81·H (minimap, prompts and subtitles sit below).
  Cutscenes have letterbox bars (about 2.7 % of H top and bottom), so start crops at y ≥ 0.065·H.
- **Check every shot:** sample every 5th frame for black bars (an edge row with max brightness < 14), HUD
  fragments, reticles, vehicle-name pop-ups and facecam edges. Look at the frames yourself.
- **9:16 reframing:** crop each shot around its subject (the face, the car, the explosion). For shots that
  only work wide, use a scaled 16:9 band with a blurred fill only as a last resort.
- **Stutter check on the source:** streams lag. Before using a range, check for repeated/frozen frames
  (`mpdecimate`, or frame-difference ≈ 0 on non-static content) and skip any stuttering range.
- **Content to avoid:** nudity (it exists in GTA 6 story scenes), gore close-ups, and any shot where the
  streamer's voice is over the line you want.

---

## 5. Dialogue and voice

- Use only lines where **no streamer/narrator talks over them**. Verify each line twice: (a) re-transcribe
  the exact source range with faster-whisper `small` (word timestamps, beam 5, a window starting about 0.5 s
  before the line), and (b) read the game's own subtitle in that frame.
- Choose lines for the **story**, not because they passed verification. A line must set up, turn or pay off
  the premise. A line that needs context the viewer doesn't have is cut.
- Cut lines at natural pauses (word gaps ≥ 80 ms), never mid-word. Leave 0.15 s of air before and 0.25 s after.
- Swearing: the audio can stay uncensored if the creator is fine with it. On-screen text uses `f***` style.

---

## 6. Audio mix (seamless, never "cut-and-paste")

The creator explicitly rejected abrupt fades: "unprofessional fade in/out of the music and game audio, looks
like an abrupt cut". Do this instead:

- **Continuous bed:** under any scene that has dialogue, keep that scene's **game ambience running for the
  whole shot** at about −24 dB, so the background never pops in or out.
- **Dialogue in/out:** 0.3–0.6 s crossfades, cut at pauses. Use **J/L cuts**: a line can start 0.2–0.5 s before
  its picture cut, or end after it.
- **Music ducking:** sidechain-style, smooth, ≈ −12 to −16 dB under speech, **attack 0.4 s, release 0.8 s**.
  For example in ffmpeg: `[music][voice]sidechaincompress=threshold=0.03:ratio=8:attack=400:release=800:makeup=1`.
  Never an on/off volume switch.
- **Voice chain:** high-pass at 90–100 Hz → gentle compressor (3:1, about 4 ms attack, 80 ms release) → level to
  about −14 to −12 dBFS RMS with the gain capped by the clip's peaks (no hard clipping or heavy tanh, which
  squashes consonants and makes words unintelligible).
- **Drop:** about 50–100 ms before the drop, pull everything to near silence (a "breath"), then hit the drop on
  a frame-exact cut.
- **Master:** `loudnorm=I=-14:TP=-1:LRA=11`, AAC 320 kbps, 48 kHz stereo.
- **Listening check:** play every dialogue transition and the drop. You can't listen yourself, so also
  check the RMS envelope around each transition: no step > 3 dB in the bed, and no gap of silence that isn't
  intended.
- **Music:** cut it on its own beat grid (fit the BPM and phase from onset energy). Content ID warning:
  commercial tracks will be claimed; tell the creator.

---

## 7. Render pipeline (stutter-free)

The creator saw **frame drops and lag** in earlier renders. They came from cutting every shot separately
with `-ss` + `fps=30` and joining the pieces with `concat`. Do this instead:

1. **Intermediates at native frame rate:** for each needed source range, extract with a 1 s handle on each
   side, **without changing fps** (keep 60 fps), into a high-quality mezzanine (x264 CRF 12 or ProRes).
2. **Frame-exact cut list:** express every cut as a frame number at 60 fps, snapped to the music beat grid.
3. **One final pass:** a single ffmpeg filter graph (or a Python frame pipe) that trims every shot by frame
   number, crops/reframes, concatenates **inside the graph**, applies the grade, overlays the typography (ASS or
   PNG sequence), and converts **once** to 30 fps at the end (`fps=30` after the concat, or `framerate` for
   slow-mo). Encode libx264 CRF 16, preset medium, yuv420p, `-movflags +faststart`.
4. **Re-time the streams:** `setpts=PTS-STARTPTS` and `asetpts=PTS-STARTPTS,aresample=async=1`. Both streams
   must start at `0.000000` (check with ffprobe).
5. **Speed ramps** (optional, for impacts): use `setpts` on 60 fps material (2x slow-mo = 60→30 fps without
   duplicate frames). Never slow 30 fps material (it duplicates frames).
6. **Append the outro** (section 9) as the last step.

Typography implementation: an ASS file with per-word `\t` fades/pops (≈ 80–120 ms in, scale 92 %→100 %), or
PIL-rendered PNG word-lockups for gradient words and masked "behind the subject" shots (composite them with
`overlay` at exact frames). Keep everything inside the IG grid safe area for 9:16 (y 240–1680) and away from the
bottom 300 px (Shorts/Reels UI).

---

## 8. QA checklist (all must pass before delivery)

- [ ] The first 2 s contain the hook. The drop lands on the most spectacular shot.
- [ ] One clear idea; the payoff/refrain at the end.
- [ ] No HUD, facecam, letterbox bars, reticle, menus or nudity. Check with contact sheets of every shot
      (every 5th frame) and look at them.
- [ ] Words appear exactly on the spoken syllable; no typos; mixed fonts as in 2.3.
- [ ] **No dropped/duplicate frames:** `ffmpeg -i out.mp4 -vf "mpdecimate,freezedetect=n=0.001:d=0.3" -an -f null -`
      reports nothing outside intended holds. Scrub every cut.
- [ ] **Seamless audio:** no pops/steps at dialogue edges, smooth ducking. Re-transcribe every line in the
      final mix (it must be intelligible) AND check the RMS envelope.
- [ ] Loudness −14 LUFS (±1), true peak ≤ −1 dBFS; both streams start at 0.000000.
- [ ] The outro is present and correct for the format (16:9 or 9:16).
- [ ] File names, resolution, fps and duration are right.

---

## 9. The ZyScorpX outro (on EVERY video, short and reel)

The approved end card (the last 5 s of the creator's "02_GTA6_Trailer_Cut_ZyScorpX.mp4"):

- A dark, **blurred copy of the video's last shot** (Gaussian blur ≈ W/70, darkening alpha 110→230 toward the bottom).
- A **round scorpion avatar** with a pink glow (the YouTube channel avatar:
  https://yt3.googleusercontent.com/AJ14JdcosksfLS5klNTZ-ygS3FTAdr_TFrRJLboXPCIvc-U5I2SMU9SwmrfIxB16TVtkLRYdSw=s0).
- The **ZYSCORPX.TV** wordmark in **Montserrat Black Italic**: "ZYSCORP" white, "X" pink #FF4FA3, ".TV" yellow #FFE500.
- **FOLLOW FOR MORE GTA 6** (Montserrat Bold, #F6E4EC) with a 4 px pink underline.
- Three rows: **IG** pill (#E1306C) instagram.com/zyscorpx.tv · **YT** pill (#FF0000) youtube.com/@ZyScorpXTV ·
  **X** pill (black, white outline) x.com/ZyScorpX (Montserrat SemiBold).
- **16:9 layout (1920x1080):** avatar r = 176 centred at (431, 502); wordmark 142 px at (645, 278); tagline 40 px at
  (645, 478); underline x 645–1215, y 545–549; rows start at y 591, 86 px apart, pills 92x57.
- **9:16 layout (1080x1920):** stacked and centred: avatar r = 190 at y 640, wordmark 118 px at y 900, tagline at y 1062,
  underline at y 1124, rows from y 1180, 96 px apart.
- **Timing:** the picture crossfades from the last shot over 0.35 s; the card fades in over 0.6 s; it holds for 5.0 s.
- **Audio:** the soundtrack continues under the outro and fades out from 2.5 s to 3.1 s, then silence.
- **Tool:** `python3 -m shortsclip.outro append final.mp4 final_with_outro.mp4 --music song.wav --music-at <s>`
  (in the repo). The full source is in the Appendix, so it can be recreated anywhere.

---

## 10. Deliverables

- **Files:** `/home/user/<Topic>_Shorts/NN_Title_ZyScorpX.mp4` (1080x1920 30 fps H.264 + AAC; 16:9 masters
  1920x1080 if asked), covers in `thumbnails/NN_Title_ZyScorpX_thumbnail.jpg`, plus one zip of everything. Send
  them and remind the creator to **download them** (cloud containers are deleted after inactivity).
- **Covers:** 9:16 1080x1920 "modern key art": a full-bleed graded key frame (a face close-up reads best at feed
  size); top-left a round avatar plus "ZYSCORPX" (Archivo Expanded ExtraBold) and a tracked "PRESENTS" (Inter
  Display Medium); the official GTA VI logo (keyed from the game's title card); bottom-left a thin pink→cyan
  line plus "REAL GAMEPLAY", line 1 white Archivo Expanded ExtraBold, line 2 **Archivo Expanded Black in the
  #FF4FA3→#FFB047 gradient**. Keep text within y 240–1680. 16:9 covers: 3840x2160 JPG under 2 MB. Check
  candidates at feed size (480x270 / 270x480) side by side, recommend ONE, and offer 2 alternates for YouTube
  Test & Compare. Avoid: yellow pills, classic serif titles (Cinzel), and cluttered text.
- **Table:** file name, the source timestamp ranges used, length.
- **Post text per video** (fenced code blocks):
  - **YouTube title:** < 100 characters, curiosity-driven, post-launch, e.g. `GTA 6 Feels Like a Movie 🎬🔥 (Real Gameplay)`;
    Shorts end with `#Shorts`. Give **one** firm recommendation.
  - **YouTube description:**
    ```
    <keyword-rich hook line> 🔥
    <question CTA> 👇

    🎥 Original footage: <channel> – <source URL>
    🎵 Music: <artist> – <track>

    📲 Follow for more GTA 6:
    Instagram: https://www.instagram.com/zyscorpx.tv/
    YouTube: https://www.youtube.com/@ZyScorpXTV
    X: https://x.com/ZyScorpX

    #gta6 #gta6gameplay <topic tag> #Shorts
    ```
  - **Tags line:** comma-separated, 15–20 relevant keywords (gta 6, gta 6 gameplay, gta vi, grand theft auto 6,
    leonida, vice city, character names, the topic, rockstar games, gta 6 shorts…). Never unrelated tags.
  - **Instagram:** hook sentence with emojis, question CTA + 👇, `🎥 Credit: <channel> (YouTube) | 🎵 <artist>`,
    `📲 YT: @ZyScorpXTV | X: @ZyScorpX`, then 12 hashtags:
    `#gta6 #gtavi #grandtheftauto #rockstargames #gaming #gamingnews #ps5 #xbox #viral #fyp` + 2 topic tags
    (e.g. `#gta6gameplay #leonida`). Never `#gta6trailer`.
  - **X:** one-line hook, `🎥 <channel>`, `📺 youtube.com/@ZyScorpXTV | 📸 IG: zyscorpx.tv`, `#GTA6`.
- **Reminders every time:** the footage belongs to the source creator, so always keep the credit line;
  commercial music gets Content ID claims; on Instagram leave the "AI label" **off** (real game footage);
  the audio may contain uncensored language.

---

## 11. Environment (cloud container) setup and gotchas

```bash
pip install -U yt-dlp faster-whisper numpy pillow opencv-python-headless fonttools
apt-get update && apt-get install -y fonts-montserrat ffmpeg
mkdir -p /root/.config/yt-dlp && printf -- '--cookies /root/.config/yt-dlp/cookies.txt\n--js-runtimes node\n--remote-components ejs:github\n' > /root/.config/yt-dlp/config
export http_proxy=$HTTPS_PROXY        # ffmpeg ignores HTTPS_PROXY
```

- YouTube's bot check needs a **Netscape cookies.txt from a throwaway account** (exported in a private window).
  Ask the creator to upload it. Never commit or share it.
- Format IDs vary: list them with `yt-dlp -F`. Audio: pick the original-language `251`/`140` variant (e.g. `251-5`)
  or `-f "bestaudio[acodec=opus]/bestaudio"`.
- YouTube throttles single 4K downloads (≈ 40 min for 8 GB). Use `--download-sections "*START-END"` in parallel
  for just the ranges you need, after mining with a low-res copy (`-f 160/133`).
- faster-whisper + PyAV can break (`metadata_errors` TypeError): decode audio with ffmpeg into a float32 numpy
  array (16 kHz mono) and pass that in. Transcribing 80 min on 4 CPUs with `small` int8 takes about 60 min, so
  transcribe only the ranges you need when you can.
- Facecam in the top-right corner makes "letterbox detection" fail on full-width rows: measure the bars on the
  left 75 % of the width.
- Files over 30 MB can't be uploaded to the chat. Ask the creator to trim with ffmpeg locally, e.g.
  `ffmpeg -i in.mp4 -ss 40 -c:v libx264 -crf 16 -c:a aac -b:a 320k out.mp4`.
- Git: don't add a `Co-Authored-By: Claude` line to commits (the creator removed it).

---

## 12. Rejected work: never repeat

**"Dialogue montages" (2026-11-20)**, three 16:9 videos from Hollow's "GTA 6 – Part 2" ("No Second Chances",
"Rent Day", "Life in the Keys"). The creator's verdict: *"utter nonsense: no hook, no attachment, no creativity,
wasted my tokens."* Why they failed:

- They opened with "ZYSCORPX PRESENTS" over calm shots, then 15–25 s of talking before anything happened. The
  best moment (a double truck jump off a broken bridge) was buried at 27 s.
- The lines were chosen because they passed verification, not because they told a story: mid-scene fragments
  with no setup, stakes or payoff.
- Dull footage: dark scenes, walking, shop interiors, driving seen from behind.
- Plain bottom subtitles instead of kinetic typography.
- Abrupt audio: 30 ms clip fades and 0.12 s music-duck ramps made the game audio and music pop in and out.
- Stutter from per-shot `-ss` + `fps=30` + `concat`.
- An old recipe was followed mechanically instead of judging "would a viewer stop scrolling?"

Also rejected earlier: a credits line on the end card; "GTA VI / OUT NOW" text; synthesised or original music;
videos with no character dialogue; slow pacing; streamer commentary; any "trailer cut" wording; yellow-pill
YouTuber thumbnails and classic serif (Cinzel) thumbnails.

---

## Appendix: `shortsclip/outro.py` (recreates the outro anywhere)

It needs `fonts-montserrat`, Pillow and ffmpeg, and the avatar image at `assets/zyscorpx_avatar.jpg`
(download it from the avatar URL in section 9 and save it as 720x720 JPG).

```python
"""ZyScorpX channel outro, appended to EVERY video, short and reel.

Rebuilt from the user's approved end card (the last 5 s of "02_GTA6_Trailer_Cut_ZyScorpX.mp4"):
a round scorpion avatar with a pink glow, the ZYSCORPX.TV wordmark (white, pink X, yellow .TV, heavy italic),
"FOLLOW FOR MORE GTA 6" with a pink underline, and IG / YT / X rows, over a blurred, darkened copy of the
video's last shot. The card fades in over 0.6 s, the picture crossfades in, and it holds for 5 s.

    python3 -m shortsclip.outro append in.mp4 out.mp4 [--music song.wav --music-at 123.4]
    python3 -m shortsclip.outro card 1920x1080 card.png      # just the transparent overlay (preview)

The size is taken from the input video: 16:9 inputs get the horizontal layout (avatar left, text right),
9:16 inputs get the stacked layout. --music continues the soundtrack under the outro (from --music-at,
fading out between 2.5 s and 3.1 s, like the original). Without it, the video's own audio crossfades to silence.
"""
import argparse
import json
import os
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
AVATAR = os.path.join(HERE, "..", "assets", "zyscorpx_avatar.jpg")
FONTS = "/usr/share/fonts/truetype/montserrat/"
F_WORD = FONTS + "Montserrat-BlackItalic.ttf"
F_BOLD = FONTS + "Montserrat-Bold.ttf"
F_SEMI = FONTS + "Montserrat-SemiBold.ttf"
WHITE, PINK, YELLOW = (255, 255, 255, 255), (255, 79, 163, 255), (255, 229, 0, 255)
ROWS = [("IG", "instagram.com/zyscorpx.tv", (225, 48, 108)),
        ("YT", "youtube.com/@ZyScorpXTV", (255, 0, 0)),
        ("X", "x.com/ZyScorpX", (12, 12, 12))]
DURATION, FADE_IN, XFADE = 5.0, 0.6, 0.35


def _avatar(size):
    av = Image.open(AVATAR).convert("RGBA").resize((size, size), Image.LANCZOS)
    m = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(m).ellipse([0, 0, size * 4 - 1, size * 4 - 1], fill=255)
    av.putalpha(m.resize((size, size), Image.LANCZOS))
    return av


def _glow(img, cx, cy, r):
    g = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse([cx - r - 14, cy - r - 14, cx + r + 14, cy + r + 14], fill=(255, 79, 163, 190))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(r * 0.16)))
    ring = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(ring).ellipse([cx - r - 5, cy - r - 5, cx + r + 5, cy + r + 5], fill=(25, 12, 30, 255))
    img.alpha_composite(ring)
    img.alpha_composite(_avatar(2 * r), (cx - r, cy - r))


def _shadowed(img, pos, text, font, fill, blur=8):
    s = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(s).text((pos[0] + 3, pos[1] + 6), text, font=font, fill=(0, 0, 0, 170))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(img).text(pos, text, font=font, fill=fill)


def _wordmark(img, x, y, font):
    d = ImageDraw.Draw(img)
    for part, col in (("ZYSCORP", WHITE), ("X", PINK), (".TV", YELLOW)):
        _shadowed(img, (x, y), part, font, col)
        x += d.textlength(part, font=font)


def _rows(img, x, y, step, s):
    d = ImageDraw.Draw(img)
    fl, fp = ImageFont.truetype(F_SEMI, int(46 * s)), ImageFont.truetype(F_BOLD, int(30 * s))
    pw, ph = int(92 * s), int(57 * s)
    for i, (tag, url, col) in enumerate(ROWS):
        yy = y + i * step
        d.rounded_rectangle([x, yy, x + pw, yy + ph], radius=int(12 * s), fill=col + (255,),
                            outline=(255, 255, 255, 255) if tag == "X" else None, width=max(2, int(3 * s)))
        tw = d.textlength(tag, font=fp)
        d.text((x + (pw - tw) / 2, yy + (ph - fp.size) / 2 - 2 * s), tag, font=fp, fill=WHITE)
        _shadowed(img, (x + pw + int(31 * s), yy + (ph - fl.size) / 2 - 6 * s), url, fl, WHITE, blur=6)


def card(w, h):
    """Transparent end-card overlay for a w x h frame."""
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if w >= h:  # horizontal layout, measured from the approved 1920x1080 card
        s = w / 1920
        _glow(img, int(431 * s), int(502 * s), int(176 * s))
        x = int(645 * s)
        _wordmark(img, x, int(278 * s), ImageFont.truetype(F_WORD, int(142 * s)))
        ff = ImageFont.truetype(F_BOLD, int(40 * s))
        _shadowed(img, (x, int(478 * s)), "FOLLOW FOR MORE GTA 6", ff, (246, 228, 236, 255), blur=6)
        d.rectangle([x, int(545 * s), int(1215 * s), int(549 * s)], fill=(255, 79, 163, 255))
        _rows(img, x, int(591 * s), int(86 * s), s)
    else:  # vertical layout: stacked and centred, all inside the IG grid safe area (y 240-1680)
        s = w / 1080
        cx = w // 2
        _glow(img, cx, int(640 * s), int(190 * s))
        fw = ImageFont.truetype(F_WORD, int(118 * s))
        tw = sum(d.textlength(p, font=fw) for p in ("ZYSCORP", "X", ".TV"))
        _wordmark(img, int(cx - tw / 2), int(900 * s), fw)
        ff = ImageFont.truetype(F_BOLD, int(40 * s))
        t = "FOLLOW FOR MORE GTA 6"
        fx = cx - d.textlength(t, font=ff) / 2
        _shadowed(img, (fx, int(1062 * s)), t, ff, (246, 228, 236, 255), blur=6)
        d.rectangle([int(fx), int(1124 * s), int(w - fx), int(1128 * s)], fill=(255, 79, 163, 255))
        fl = ImageFont.truetype(F_SEMI, int(46 * s))
        block = 92 * s + 31 * s + max(d.textlength(r[1], font=fl) for r in ROWS)
        _rows(img, int(cx - block / 2), int(1180 * s), int(96 * s), s)
    return img


def _probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type,width,height,r_frame_rate",
                          "-show_entries", "format=duration", "-of", "json", path],
                         capture_output=True, text=True, check=True).stdout
    j = json.loads(out)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    has_a = any(s["codec_type"] == "audio" for s in j["streams"])
    n, d = v["r_frame_rate"].split("/")
    return int(v["width"]), int(v["height"]), float(n) / float(d), float(j["format"]["duration"]), has_a


def append(src, out, music=None, music_at=0.0):
    w, h, fps, dur, has_a = _probe(src)
    with tempfile.TemporaryDirectory() as tmp:
        last = os.path.join(tmp, "last.png")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.2", "-i", src, "-frames:v", "1", last], check=True)
        bg = Image.open(last).convert("RGB").filter(ImageFilter.GaussianBlur(max(w, h) / 70))
        dark = Image.new("RGBA", bg.size, (0, 0, 0, 0))
        dd = ImageDraw.Draw(dark)
        for y in range(h):  # darker towards the bottom, like the original
            dd.line([(0, y), (w, y)], fill=(0, 0, 0, int(110 + 120 * (y / h) ** 1.4)))
        bg = Image.alpha_composite(bg.convert("RGBA"), dark).convert("RGB")
        bgp, cardp = os.path.join(tmp, "bg.png"), os.path.join(tmp, "card.png")
        bg.save(bgp)
        card(w, h).save(cardp)
        o = os.path.join(tmp, "outro.mp4")
        a_in = (["-ss", f"{music_at:.3f}", "-t", f"{DURATION:.3f}", "-i", music] if music else
                ["-f", "lavfi", "-t", f"{DURATION:.3f}", "-i", "anullsrc=r=48000:cl=stereo"])
        a_f = ("[2:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=out:st=2.5:d=0.6[a]" if music
               else "[2:a]anull[a]")
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", f"{fps}", "-t", f"{DURATION:.3f}", "-i", bgp,
             "-loop", "1", "-framerate", f"{fps}", "-t", f"{DURATION:.3f}", "-i", cardp, *a_in,
             "-filter_complex",
             f"[0:v]scale={w * 1.06:.0f}:-2,zoompan=z='1+0.0004*on':d=1:s={w}x{h}:fps={fps},format=yuv420p[b];"
             f"[1:v]format=rgba,fade=t=in:st=0:d={FADE_IN}:alpha=1[c];[b][c]overlay=0:0:format=auto,format=yuv420p[v];{a_f}",
             "-map", "[v]", "-map", "[a]", "-t", f"{DURATION:.3f}", "-r", f"{fps}", "-c:v", "libx264", "-crf", "16",
             "-preset", "medium", "-c:a", "aac", "-b:a", "320k", o], check=True)
        main_a = "[0:a]aresample=48000,aformat=channel_layouts=stereo[ma];" if has_a else \
            f"anullsrc=r=48000:cl=stereo,atrim=0:{dur:.3f}[ma];"
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-i", src, "-i", o, "-filter_complex",
             f"[0:v]fps={fps},format=yuv420p,setpts=PTS-STARTPTS[v0];[1:v]fps={fps},format=yuv420p,setpts=PTS-STARTPTS[v1];"
             f"[v0][v1]xfade=transition=fade:duration={XFADE}:offset={dur - XFADE:.3f}[v];"
             f"{main_a}[1:a]asetpts=PTS-STARTPTS[oa];[ma][oa]acrossfade=d={XFADE}:c1=tri:c2=tri,"
             f"asetpts=PTS-STARTPTS,aresample=async=1[a]",
             "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "320k", "-movflags", "+faststart", out], check=True)
    return out


def main(argv=None):
    p = argparse.ArgumentParser(prog="shortsclip.outro", description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("append", help="append the outro to a finished video")
    a.add_argument("src"); a.add_argument("out")
    a.add_argument("--music", help="soundtrack to continue under the outro")
    a.add_argument("--music-at", type=float, default=0.0, help="position in --music where the outro starts (s)")
    c = sub.add_parser("card", help="write the transparent overlay PNG")
    c.add_argument("size", help="WxH, e.g. 1920x1080 or 1080x1920"); c.add_argument("out")
    args = p.parse_args(argv)
    if args.cmd == "append":
        print(append(args.src, args.out, args.music, args.music_at))
    else:
        w, h = map(int, args.size.lower().split("x"))
        card(w, h).save(args.out); print(args.out)


if __name__ == "__main__":
    main()
```
