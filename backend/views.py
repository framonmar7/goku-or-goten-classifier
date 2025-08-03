import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

IMG_SIZE = (224, 224)

def binary_classification_view(model, formatter):
    @csrf_exempt
    @api_view(["POST"])
    def view(request):
        image_file = request.FILES.get("image")
        if not image_file:
            return Response({"error": "No image provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            image = Image.open(image_file).convert("RGB")
            image = image.resize(IMG_SIZE)
            array = np.array(image)
            array = preprocess_input(array)
            array = np.expand_dims(array, axis=0).astype(np.float32)
            
            input_details = model.get_input_details()
            output_details = model.get_output_details()
            
            model.set_tensor(input_details[0]['index'], array)
            model.invoke()
            prediction = float(model.get_tensor(output_details[0]['index'])[0][0])
            
            return Response(formatter(prediction))
        
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
