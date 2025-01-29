
from django.urls import path
from Iggy_App.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('diario/', diario, name="diario"),
    path('diario_text/', diario_text, name="diario_text"),
    path('diario_detalle/<int:id>', diario_detalle, name="diario_detalle")
]
