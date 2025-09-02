from django.urls import path, include
from frontend.views import index

urlpatterns = [
    path("api/", include("backend.urls")),
    path('', index),
]
