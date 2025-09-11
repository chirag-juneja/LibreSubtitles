import whisper
import os
from libresubtitles.core.globals import MODEL_DIR


def load_model(model_name="tiny"):
    os.makedirs(MODEL_DIR, exist_ok=True)
    os.environ["XDG_CACHE_HOME"] = MODEL_DIR
    model = whisper.load_model(model_name, device="cpu")
    return model


def transcribe_audio(file_path: str) -> str:
    model = load_model()
    result = model.transcribe(file_path, fp16=False)
    print(result["segments"])
    return result["text"]


if __name__ == "__main__":
    text = transcribe_audio("./data/sample.wav")
    print(text)
