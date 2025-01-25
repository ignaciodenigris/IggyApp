
from django.urls import path
from Iggy_App.views import *

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
]
