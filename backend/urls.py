from django.urls import path
from backend.views import index, classify_goten, classify_goku, classify_goten_vs_goku

urlpatterns = [
    path("", index, name="index"),
    path("classify/goten/", classify_goten, name="classify-goten"),
    path("classify/goku/", classify_goku, name="classify-goku"),
    path("classify/goten-vs-goku/", classify_goten_vs_goku, name="classify-goten-vs-goku"),
]
