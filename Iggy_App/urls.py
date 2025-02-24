
from django.urls import path
from Iggy_App.views import *

urlpatterns = [
    
    # Diario
    
    path('inicio/', inicio, name="inicio"),
    path('diario/', diario, name="diario"),
    path('diario_text/', diario_text, name="diario_text"),
    path('diario_detalle/<int:id>', diario_detalle, name="diario_detalle"),
    
    # Colegio
    
    path('colegio/', colegio, name="colegio"),
    
    path('lengua_form/', lengua_form, name="lengua_form"),
    path('lengua_form_delete/<int:id>', lengua_form_delete, name="lengua_form_delete"),
    
    path('matematica_form/', matematica_form, name="matematica_form"),
    path('matematica_form_delete/<int:id>', matematica_form_delete, name="matematica_form_delete"),
    
    path('economia_form/', economia_form, name="economia_form"),
    path('economia_form_delete/<int:id>', economia_form_delete, name="economia_form_delete"),
    
    path('programacion_form/', programacion_form, name="programacion_form"),
    path('informatica_form_delete/<int:id>', informatica_form_delete, name="informatica_form_delete"),
    
    path('extra_form/', extra_form, name="extra_form"),
    path('extra_form_delete/<int:id>', extra_form_delete, name="extra_form_delete"),
    
    path('login_view/', login_view, name = "login_view"),
    path('logout_view/', logout_view, name = "logout_view"),
]
