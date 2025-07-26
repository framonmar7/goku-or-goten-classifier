import requests

API_ENDPOINTS = {
    "goten_model": "https://goten-detector.framonmar7.dev/api/classify/",
    "goku_model": "https://goku-detector.framonmar7.dev/api/classify/",
    "arbiter_model": "https://goku-vs-goten-arbiter.framonmar7.dev/api/classify/",
}

def remote_predictor(endpoint: str):
    def predict(image_file):
        response = requests.post(endpoint, files={"image": image_file})
        response.raise_for_status()
        return response.json()
    return predict

goten_model = remote_predictor(API_ENDPOINTS["goten_model"])
goku_model = remote_predictor(API_ENDPOINTS["goku_model"])
arbiter_model = remote_predictor(API_ENDPOINTS["arbiter_model"])
