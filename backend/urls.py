from django.urls import path
from backend.views import (
    binary_classification_view,
    format_binary_prediction,
    format_character_prediction
)
from backend.inference.models import goten_model, goku_model, arbiter_model

urlpatterns = [
    path("classify/goten/", binary_classification_view(goten_model, format_binary_prediction)),
    path("classify/goku/", binary_classification_view(goku_model, format_binary_prediction)),
    path("classify/goten-vs-goku/", binary_classification_view(arbiter_model, format_character_prediction)),
]
