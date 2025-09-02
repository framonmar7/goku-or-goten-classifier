import numpy as np
from PIL import Image, UnidentifiedImageError
from tensorflow.keras.applications.resnet50 import preprocess_input
from .errors import UnsupportedFormat, ImageTooSmall, ImageTooLarge

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
PIL_FORMAT_TO_CONTENT = {"JPEG": "image/jpeg", "PNG": "image/png", "WEBP": "image/webp"}

MIN_W, MIN_H = 100, 100
MAX_W, MAX_H = 2000, 2000

def _ensure_allowed_type(img_file, pil_image):
    ctype = getattr(img_file, "content_type", None)
    if ctype in ALLOWED_CONTENT_TYPES:
        return
    inferred = PIL_FORMAT_TO_CONTENT.get(getattr(pil_image, "format", "") or "", None)
    if inferred not in ALLOWED_CONTENT_TYPES:
        raise UnsupportedFormat("Allowed formats: JPG, PNG, WEBP")

def _ensure_dimension_limits(pil_image):
    w, h = pil_image.size
    if w < MIN_W or h < MIN_H:
        raise ImageTooSmall(MIN_W, MIN_H, w, h)
    if w > MAX_W or h > MAX_H:
        raise ImageTooLarge(MAX_W, MAX_H, w, h)

def load_and_validate_image(img_file):
    try:
        img = Image.open(img_file)
    except UnidentifiedImageError:
        raise UnsupportedFormat("Allowed formats: JPG, PNG, WEBP")
    _ensure_allowed_type(img_file, img)
    _ensure_dimension_limits(img)
    return img

def prepare_tensor_for_resnet(img, target_size):
    img = img.convert("RGB").resize(target_size)
    arr = np.expand_dims(preprocess_input(np.array(img)), axis=0).astype(np.float32)
    return arr
