from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def binary_classification_view(remote_predictor, formatter=None):
    @csrf_exempt
    @api_view(["POST"])
    def view(request):
        image_file = request.FILES.get("image")
        if not image_file:
            return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            image_file.seek(0)
            prediction_data = remote_predictor(image_file)

            if formatter:
                return Response(formatter(prediction_data))
            else:
                return Response(prediction_data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return view

def format_character_prediction(data: dict) -> dict:
    is_goten = data.get("prediction", False)
    confidence = data.get("confidence", 0.0)
    return {
        "character": "Goten" if is_goten else "Goku",
        "confidence": round(confidence, 4)
    }
