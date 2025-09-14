from pydub import AudioSegment, silence
from pathlib import Path
from libresubtitles.core.globals import MIN_SILENCE_LEN, SILENCE_THRESH, KEEP_SILENCE


def split_audio(audio_path: str):
    audio = AudioSegment.from_wav(audio_path)

    chunks = silence.split_on_silence(
        audio,
        min_silence_len=MIN_SILENCE_LEN,
        silence_thresh=audio.dBFS - SILENCE_THRESH,
        keep_silence=KEEP_SILENCE,
    )
    return chunks


if __name__ == "__main__":
    split_audio("./data/video.wav")
