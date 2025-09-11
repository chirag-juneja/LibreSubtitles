import whisper
import os
from libresubtitles.core.global import MODEL_DIR


def load_model(model_name="tiny"):
    os.makedirs(MODEL_DIR, exist_ok=True)
    os.environ["XDG_CACHE_HOME"] = MODEL_DIR

    model = whisper.load_model(model_name)
    return model

load_model()
