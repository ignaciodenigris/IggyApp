from django import forms
from Iggy_App.models import Diario, Matematica, Lengua, Economia, Programacion, Extra_materia

class Form_Diario(forms.ModelForm):
    class Meta: 
        model = Diario 
        fields = "__all__"

class Form_Matematica(forms.ModelForm):
    class Meta: 
        model = Matematica 
        fields = "__all__"

class Form_Lengua(forms.ModelForm):
    class Meta: 
        model = Lengua 
        fields = "__all__"

class Form_Economia(forms.ModelForm):
    class Meta: 
        model = Economia 
        fields = "__all__"

class Form_Programacion(forms.ModelForm):
    class Meta: 
        model = Programacion 
        fields = "__all__"

class Form_extra(forms.ModelForm):
    class Meta: 
        model = Extra_materia 
        fields = "__all__"