"""Transkribiert quellen/videos/NN/video.mp4 -> transkript.txt (mit Zeitstempeln) + transkript.json.

Aufruf: python tools/transkribiere.py [NN ...]   (ohne Argument: alle Ordner ohne transkript.txt)
Benoetigt: faster-whisper (venv: C:/Users/USER/.venvs/whisper)
"""
import json
import subprocess
import sys

import numpy as np
from pathlib import Path

from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent.parent / "quellen" / "videos"


def load_audio(path):
    # ffmpeg statt PyAV: faster-whisper ruft av.open mit einem Argument auf, das die installierte PyAV-Version nicht kennt
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0


def ts(sec):
    m, s = divmod(sec, 60)
    return f"{int(m):02d}:{s:05.2f}"


def main():
    wanted = sys.argv[1:]
    dirs = sorted(d for d in ROOT.iterdir() if d.is_dir())
    if wanted:
        dirs = [d for d in dirs if d.name in wanted]
    else:
        dirs = [d for d in dirs if not (d / "transkript.txt").exists()]

    model = WhisperModel("large-v3-turbo", device="cpu", compute_type="int8")
    for d in dirs:
        segments, info = model.transcribe(
            load_audio(d / "video.mp4"), beam_size=1, vad_filter=False, condition_on_previous_text=True
        )
        segs = [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]
        (d / "transkript.json").write_text(
            json.dumps({"sprache": info.language, "p": info.language_probability, "segmente": segs},
                       ensure_ascii=False, indent=1),
            encoding="utf-8",
        )
        lines = [f"[{ts(s['start'])} - {ts(s['end'])}] {s['text']}" for s in segs]
        (d / "transkript.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(d.name, info.language, len(segs), flush=True)


if __name__ == "__main__":
    main()
