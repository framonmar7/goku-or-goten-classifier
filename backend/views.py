from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser
from backend.inference.models import goten_model, goku_model, arbiter_model
from backend.docs.schemas import file_param, binary_responses, character_responses
from backend.validators import load_and_validate_image, prepare_tensor_for_resnet

IMG_SIZE = (224, 224)

def index(request):
    return JsonResponse({
        "message": "Welcome to the Goku or Goten API",
        "endpoints": {
            "goten": "/api/classify/goten",
            "goku": "/api/classify/goku",
            "goten-vs-goku": "/api/classify/goten-vs-goku"
        },
        "docs": "/docs"
    })

def classify_image(request, model, formatter):
    image_file = request.FILES.get("image")
    if not image_file:
        return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)

    img = load_and_validate_image(image_file)
    tensor = prepare_tensor_for_resnet(img, IMG_SIZE)

    input_details = model.get_input_details()
    output_details = model.get_output_details()
    model.set_tensor(input_details[0]["index"], tensor)
    model.invoke()
    prediction = float(model.get_tensor(output_details[0]["index"])[0][0])

    return Response(formatter(prediction))

def register_endpoint(name, model, formatter, summary, responses):
    @swagger_auto_schema(
        method="post",
        operation_id=name,
        operation_summary=summary,
        manual_parameters=[file_param],
        consumes=["multipart/form-data"],
        responses=responses,
        tags=["Classification"],
    )
    @api_view(["POST"])
    @parser_classes([MultiPartParser, FormParser])
    def view(request):
        return classify_image(request, model, formatter)
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

classify_goten = register_endpoint(
    "classifyGoten",
    goten_model,
    format_binary_prediction,
    "Classify if the image is Kid Goten",
    binary_responses,
)

classify_goku = register_endpoint(
    "classifyGoku",
    goku_model,
    format_binary_prediction,
    "Classify if the image is Kid Goku",
    binary_responses,
)

classify_goten_vs_goku = register_endpoint(
    "classifyGotenVsGoku",
    arbiter_model,
    format_character_prediction,
    "Classify whether the image shows Kid Goten or Kid Goku",
    character_responses,
)
