"""Transcribe the source and find the highest-energy standalone moments."""
import re
import subprocess

import numpy as np

SR = 16000

# Words and phrases that signal hype, rage, panic or laughter. Weight = how strong a signal.
HYPE = {
    "oh my god": 3, "what the": 2.5, "no no": 3, "no way": 2.5, "let's go": 2.5, "holy": 2.5,
    "insane": 2, "crazy": 1.5, "clutch": 3, "ace": 2, "wasted": 2.5, "dead": 1.5, "died": 2,
    "kill": 1.5, "killed": 2, "headshot": 3, "run": 1, "help": 1.5, "bro what": 3, "wait wait": 2.5,
    "haha": 3, "hahaha": 3, "lol": 2, "lmao": 2, "scream": 2, "jumpscare": 3, "scared": 2,
    "oh no": 3, "oh crap": 3, "oh shit": 3, "what is happening": 3, "why": 0.5, "explode": 2.5,
    "exploding": 2.5, "boom": 2, "shoot": 1.5, "shot": 1.5, "worked": 1.5, "rage": 2,
}


def load_audio(path, start=None, duration=None):
    """Decode any media to mono 16 kHz float32 via ffmpeg (avoids PyAV version issues)."""
    cmd = ["ffmpeg", "-v", "error"]
    if start is not None:
        cmd += ["-ss", f"{start:.3f}"]
    cmd += ["-i", path]
    if duration is not None:
        cmd += ["-t", f"{duration:.3f}"]
    cmd += ["-vn", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


def transcribe(pcm, model_name="small", device="auto", language=None):
    """Return a list of words: (start, end, text)."""
    from faster_whisper import WhisperModel
    if device == "auto":
        try:
            import ctranslate2
            device = "cuda" if ctranslate2.get_cuda_device_count() > 0 else "cpu"
        except Exception:
            device = "cpu"
    model = WhisperModel(model_name, device=device,
                         compute_type="float16" if device == "cuda" else "int8")
    segs, _ = model.transcribe(pcm, word_timestamps=True, vad_filter=True, language=language)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in (s.words or []) if w.word.strip()]


def _z(x):
    x = np.asarray(x, np.float32)
    sd = x.std()
    return (x - np.median(x)) / (sd if sd > 1e-6 else 1.0)


def loudness(pcm):
    n = len(pcm) // SR
    blocks = pcm[: n * SR].reshape(n, SR)
    return 20 * np.log10(np.sqrt((blocks ** 2).mean(1)) + 1e-9)


def motion(video, seconds):
    """Mean absolute frame difference per second (2 fps, 64x36 grayscale)."""
    w, h = 64, 36
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", video, "-an", "-vf",
                          f"fps=2,scale={w}:{h},format=gray", "-f", "rawvideo", "-"],
                         stdout=subprocess.PIPE)
    frames = np.frombuffer(p.stdout.read(), np.uint8)
    p.wait()
    frames = frames[: len(frames) // (w * h) * (w * h)].reshape(-1, w * h).astype(np.float32)
    diff = np.abs(np.diff(frames, axis=0)).mean(1) if len(frames) > 1 else np.zeros(1)
    per_sec = np.zeros(seconds, np.float32)
    for i, d in enumerate(diff):
        if i // 2 < seconds:
            per_sec[i // 2] = max(per_sec[i // 2], d)
    return per_sec


def hype_track(words, seconds):
    hype = np.zeros(seconds, np.float32)
    rate = np.zeros(seconds, np.float32)
    toks = [(s, re.sub(r"[^a-z' ]", "", t.lower())) for s, _, t in words]
    for i, (s, t) in enumerate(toks):
        sec = int(s)
        if sec >= seconds:
            continue
        rate[sec] += 1
        bigram = t + " " + toks[i + 1][1] if i + 1 < len(toks) else t
        trigram = bigram + " " + toks[i + 2][1] if i + 2 < len(toks) else bigram
        hype[sec] += max(HYPE.get(t, 0), HYPE.get(bigram, 0), HYPE.get(trigram, 0))
        if i and t == toks[i - 1][1] and len(t) > 1:  # "no no no", "go go go"
            hype[sec] += 1
    return hype, rate


def _smooth(x, k=3):
    return np.convolve(x, np.ones(k) / k, "same")


def find_moments(words, loud_db, motion_sec, count=2, min_len=20, max_len=45):
    """Return up to `count` non-overlapping windows as dicts(start, end, kind, score)."""
    T = len(loud_db)
    hype, rate = hype_track(words, T)
    loud_z, mot_z, rate_z = _z(loud_db), _z(motion_sec[:T]), _z(_smooth(rate, 5))
    hype_s = _smooth(hype, 3)
    tracks = {
        "action": 0.6 * mot_z + 0.5 * loud_z + 0.4 * hype_s,
        "reaction": 1.0 * hype_s + 0.5 * loud_z + 0.3 * rate_z,
    }

    def best(track, taken):
        top = None
        for L in range(min_len, max_len + 1, 5):
            if L > T:
                break
            c = np.convolve(track, np.ones(L) / L, "valid")
            pk = np.array([track[i:i + L].max() for i in range(len(c))])
            sc = c + 0.5 * pk  # sustained energy + one big peak
            for i in np.argsort(-sc)[:50]:
                if all(i + L <= a or i >= b for a, b in taken):
                    if top is None or sc[i] > top[0]:
                        top = (float(sc[i]), int(i), int(i + L))
                    break
        return top

    order = ["action", "reaction"] + ["action", "reaction"] * count
    picks, taken = [], []
    for kind in order[:count]:
        b = best(tracks[kind], taken)
        if not b:
            break
        s, e = _snap(words, b[1], b[2], min_len, max_len, T)
        picks.append({"start": s, "end": e, "kind": kind, "score": b[0]})
        taken.append((int(s), int(e) + 1))
    return sorted(picks, key=lambda p: p["start"])


def _snap(words, s, e, min_len, max_len, T):
    """Start just before a sentence opens (hook), end right after the last word lands."""
    starts = [w[0] for i, w in enumerate(words)
              if i == 0 or w[0] - words[i - 1][1] > 0.35 or words[i - 1][2][-1:] in ".?!"]
    cand = [t for t in starts if s - 3 <= t <= s + 2]
    ns = (min(cand, key=lambda t: abs(t - s)) - 0.3) if cand else s
    ends = [w[1] for w in words if e - 3 <= w[1] <= e + 3]
    ne = (min(ends, key=lambda t: abs(t - e)) + 0.4) if ends else e
    ns = max(ns, 0.0)
    ne = min(max(ne, ns + min_len), ns + max_len, T)
    return round(ns, 2), round(ne, 2)
