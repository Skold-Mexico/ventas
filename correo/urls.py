from django.urls import path
from .views import api_enviar_correo

urlpatterns = [
    path('enviar-correo/', api_enviar_correo),
]
