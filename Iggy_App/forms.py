from django import forms
from Iggy_App.models import Diario

class Form_Diario(forms.ModelForm):
    class Meta: 
        model = Diario 
        fields = "__all__"