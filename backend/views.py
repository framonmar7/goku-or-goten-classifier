from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def binary_classification_view(remote_predictor, formatter):
    @csrf_exempt
    @api_view(["POST"])
    def view(request):
        image_file = request.FILES.get("image")
        if not image_file:
            return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            prediction_data = remote_predictor(image_file)
            return Response(formatter(float(prediction_data["confidence"]) if "confidence" in prediction_data else 0.0))
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return view

def format_binary_prediction(p: float) -> dict:
    prediction = p >= 0.5
    confidence = p if prediction else 1 - p
    return {
        "prediction": prediction,
        "confidence": round(confidence, 4)
    }

def format_character_prediction(p: float) -> dict:
    is_goten = p >= 0.5
    confidence = p if is_goten else 1 - p
    return {
        "character": "Goten" if is_goten else "Goku",
        "confidence": round(confidence, 4)
    }
