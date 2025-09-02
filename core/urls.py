from django.urls import path, include
from frontend.views import index
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Goku or Goten API",
        default_version='v1',
        description="API for image classification that distinguishes between Goku and Goten using trained AI models.",
        contact=openapi.Contact(email="framonmar7@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/", include("backend.urls")),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', index),
]
