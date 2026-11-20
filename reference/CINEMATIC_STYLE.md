# ZyScorpX cinematic style: the ONLY reference for cinematic videos

Set by the user on 2026-11-20. Whenever the user asks for a "cinematic" video (edit, montage, cinematic
short/reel), match this reference. It replaces every earlier cinematic recipe, including the rejected
"dialogue montage" style (see CLAUDE.md, "REJECTED").

The reference file is `Clipping_Campaigns.mp4` (40.8 s, 1280x720, 30 fps, edited by "zaid."). It is not
committed because this repo is public and the clip contains Rockstar trailer footage and another editor's
work. If you need to see it again, ask the user to upload it. Everything below was measured from that file.

## The idea in one line

A short, emotional "story" told by a moody voice-over and kinetic typography: nostalgia for the old game
(GTA 5 / Los Santos), then a turn to the new one (GTA 6 / Leonida), then a beat drop into a fast,
fiery action montage, ending on the GTA VI logo and a tiny creator signature.

## Structure (timings from the reference)

| Time | Section | What happens |
|---|---|---|
| 0.0–1.7 s | **Hook** | Black screen. A spoken question, "Why did I move here?", builds up word by word in mixed fonts. The video opens on a question, not a logo. |
| 1.7–10 s | **Nostalgia** | Slow, beautiful GTA 5 shots (helicopter over Los Santos at sunset, Route 68, bikers, casino roulette, a jet over the city). The voice-over continues: "I guess it was the weather… or the… that thing… that magic." Every phrase is typeset over the shot. |
| ≈10 s | **Turn** | "THAT MAGIC" in a huge gradient (pink→orange) with a helicopter flying **in front of** the text (subject masking). Then the GTA V logo morphs into the GTA VI logo. |
| 10–18 s | **New world** | Leonida scenery (sunset highways, Vice City at night, the Keys from above) and character moments from GTA 6 with character lines: "You see her?" plus the name "LUCIA" in elegant italic, "Do you know why you're here?", "Bad luck, I guess." |
| 18–19.6 s | **Transition** | A white canvas with a pink/blue gradient band. A collage of many small GTA 6 clips slides in and stacks up (a "the whole world" moment). |
| ≈20 s | **DROP** | The music hits (loudness jumps from about −15 dB to about −6 dB). |
| 20–37.5 s | **Action** | Rapid cuts of the most spectacular moments: shootouts, explosions, a car chase, the police, a speedboat, motorcycle, helicopter, and character close-ups. One character line breaks through ("Hands above your head!") and the hook line returns as a refrain ("You know why you're here"). |
| 37.5–38.4 s | **Logo** | A golden-hour city shot with a small "VI" logo in the GTA VI gradient. |
| 38.4–40.8 s | **Outro** | Fade to black, a small white signature wordmark ("zaid.") in the centre, held until silence. For ZyScorpX, use the user's own outro video instead (see CLAUDE.md, "Channel outro"). |

## Pacing

- 92 cuts in 40.8 s, an average shot of **0.44 s**. The nostalgia part breathes (shots of 0.5–2.5 s);
  the action part is very fast (runs of 1–3 frame cuts around beats and impacts).
- Every cut lands on a beat or an accent in the music. Shots of a few frames are used as flash accents.
- Tension builds for about 20 s, then the beat drops. The drop is the emotional release, not the start.

## Typography (the signature look)

- **Kinetic, word-by-word.** Each spoken word appears exactly when it is said, and the phrase builds up as
  a stacked lockup in the centre of the frame. There are no subtitle-style captions at the bottom.
- **Mixed typefaces in one phrase:** a heavy geometric sans (all caps, e.g. "DID", "HERE?", "WEATHER"),
  a condensed italic serif ("I MOVE", "I GUESS"), a light script or italic ("was", "why", "you're"), and a
  wide spaced sans ("T H A T"). Lowercase and uppercase are mixed on purpose.
- **Key words in big colour:** the emotional word is huge and filled with the GTA VI gradient
  (magenta/pink→orange, e.g. "MAGIC"), or in red condensed caps for drama ("BAD LUCK").
- **Names in elegant italic serif** with a pink-gold gradient ("LUCIA").
- **Depth:** text sits behind foreground subjects (the helicopter passes in front of "THAT MAGIC") and is
  motion-tracked onto moving objects (the signature rides on the side of the speedboat).
- The text is white or a gradient with a soft shadow. There are no boxes, pills or outlines.

## Picture and colour

- 16:9 full frame (for 9:16 versions, reframe each shot around its subject; never shrink the 16:9 into a box).
- **Golden hour and neon:** warm sunset oranges, pinks and magentas against deep teal/blue nights. Fire and
  explosions push the warm end, neon pushes the magenta end. Average saturation is high (about 0.42).
- Only the most beautiful or spectacular shots are used: aerials, sunsets, skylines, explosions, vehicles at
  speed, and close-ups of characters looking into the camera. There's no HUD, no facecam, no menus and no
  walking from behind.

## Audio

- The music drives everything. It's a single moody track that builds, then drops at about 20 s.
- There's a calm voice-over at the start (a narrator's spoken question) and short, punchy character lines,
  each one typeset on screen.
- Dialogue sits **inside** the music. Use smooth ducking and no hard cuts (see CLAUDE.md, "Audio around
  character dialogue").
- It ends on a clean fade to silence over the outro.

## Checklist before rendering a cinematic

1. Is there a spoken or typed **question or claim in the first 1–2 s**?
2. Is there a clear **arc** (setup → turn → drop → payoff) that the viewer can feel?
3. Does every phrase use **kinetic, mixed-font typography** synced to the voice, with the key word in the
   GTA VI gradient?
4. Does the **drop** land on the most spectacular shot, followed by rapid beat-synced cuts?
5. Does it end on the logo moment, then the **ZyScorpX outro**?
6. Have you sent the user the concept and shot outline and had it approved **before** rendering (CLAUDE.md)?
