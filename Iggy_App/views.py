from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.utils import timezone


from Iggy_App.models import Diario
from Iggy_App.forms import Form_Diario

# Create your views here.

def inicio(request):
    return render(request, "Iggy_App\index.html")

# codigo para el Diario 

def diario(request) :
    if request.method == "POST":
        diario_form = Form_Diario(request.POST)
        if diario_form.is_valid():
            diario_form.save()
            return redirect("inicio")
    else:
        pages = Diario.objects.all()
        
        pages_list = []
    
        for page in pages:
            page_dict = {page.fecha: page.fecha}
            page_dict2 = {page.texto: page.texto}
        
        diario_form = Form_Diario()
        forms= Diario.objects.all()
        date = timezone.now().date()
        month = date.month
        day = date.day
        return render(request, "Iggy_App/Utilities/Diario.html", {"form":diario_form, "forms": forms, "month": month, "day": day, "page_dict": page_dict, "page_dict2": page_dict2})




def diario_text(request) :
    pages = Diario.objects.all()
    pages_specific = []
    
    for page in pages:
        page_dict = {
            "page_date": page.date,
            "page_text": page.texto,
        }
    return render(request, "Iggy_App\index.html")

def diario_detalle(request, id):
    detalles=Diario.objects.get(id=id)
    return render(request, "Iggy_App/Data/show_diario.html", {"detalles":detalles})