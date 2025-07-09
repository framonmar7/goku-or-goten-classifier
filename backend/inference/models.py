from tensorflow.keras.models import load_model
from huggingface_hub import hf_hub_download

model_files = {
    "goten_model": "goten_model.keras",
    "goku_model": "goku_model.keras",
    "arbiter_model": "arbiter_model.keras",
}

models = {}

for key, filename in model_files.items():
    path = hf_hub_download(repo_id="framonmar7/goku-or-goten-classifier", filename=filename)
    models[key] = load_model(path)

goten_model = models["goten_model"]
goku_model = models["goku_model"]
arbiter_model = models["arbiter_model"]
