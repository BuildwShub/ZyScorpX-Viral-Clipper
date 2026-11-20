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
