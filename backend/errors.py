from rest_framework.exceptions import APIException
from rest_framework import status

class UnsupportedFormat(APIException):
    status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

    def __init__(self, detail="Unsupported image format. Allowed formats: JPG, PNG, WEBP."):
        super().__init__({"error": detail})

class ImageTooSmall(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, min_w, min_h, got_w, got_h):
        msg = f"Minimum {min_w}x{min_h}px; got {got_w}x{got_h}px"
        super().__init__({"error": msg})

class ImageTooLarge(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, max_w, max_h, got_w, got_h):
        msg = f"Maximum {max_w}x{max_h}px; got {got_w}x{got_h}px"
        super().__init__({"error": msg})
