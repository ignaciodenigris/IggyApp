from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.utils import timezone

from django.db.models import Avg

from django.db.models.functions import Round

from Iggy_App.models import Diario, Matematica, Lengua, Economia, Programacion, Extra_materia
from Iggy_App.forms import Form_Diario, Form_Matematica, Form_Lengua, Form_Economia, Form_Programacion, Form_extra

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm,  PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login_view")
def inicio(request):
    return render(request, "Iggy_App\index.html")

# codigo para el Diario 
@login_required(login_url="login_view")
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

@login_required(login_url="login_view")
def diario_text(request) :
    pages = Diario.objects.all()
    pages_specific = []
    
    for page in pages:
        page_dict = {
            "page_date": page.date,
            "page_text": page.texto,
        }
    return render(request, "Iggy_App\index.html")

@login_required(login_url="login_view")
def diario_detalle(request, id):
    detalles=Diario.objects.get(id=id)
    return render(request, "Iggy_App/Data/show_diario.html", {"detalles":detalles})

# Codigo para colegio

from django.db.models import Avg
from django.shortcuts import render
from .models import Matematica



def calculate_score(average):
        if average is None:
            return 0
        elif 5.75 <= average < 6.25:
            return 6
        elif 6.25 <= average < 6.75:
            return 6.5
        elif 6.75 <= average < 7.25:
            return 7
        elif 7.25 <= average < 7.75:
            return 7.5
        elif 7.75 <= average < 8.25:
            return 8
        elif 8.25 <= average < 8.75:
            return 8.5
        elif 8.75 <= average < 9.25:
            return 9
        elif 9.25 <= average < 9.75:
            return 9.5
        elif average >= 9.75:
            return 10
        return 0


def get_average_score(answer):
    # Calculate average for the given answer group (A, B, or C)
        group = Matematica.objects.filter(answer=answer)
        avg_score = group.aggregate(Avg('nota'))['nota__avg']
        return avg_score


def get_average_score_lengua(answerL):
    groupL = Lengua.objects.filter(answerL = answerL)
    avg_scoreL = groupL.aggregate(Avg('notaL'))['notaL__avg']
    return avg_scoreL


def get_average_score_extra(answerEx):
    groupEx = Extra_materia.objects.filter(answerEx = answerEx)
    avg_scoreEx = groupEx.aggregate(Avg('notaEx'))['notaEx__avg']
    return avg_scoreEx


def get_average_score_economia(answerE):
    groupE = Economia.objects.filter(answerE = answerE)
    avg_scoreE = groupE.aggregate(Avg('notaE'))['notaE__avg']
    return avg_scoreE


def get_average_score_programacion(answerP):
    groupP = Programacion.objects.filter(answerP = answerP)
    avg_scoreP = groupP.aggregate(Avg('notaP'))['notaP__avg']
    return avg_scoreP


def get_final_scores():
        score_M = calculate_score(get_average_score("A"))
        score_Mat_Seg = calculate_score(get_average_score("B"))
        score_Mat_Ter = calculate_score(get_average_score("C"))

        score_L = calculate_score(get_average_score_lengua("D"))
        score_Len_Seg = calculate_score(get_average_score_lengua("E"))
        score_Len_Ter = calculate_score(get_average_score_lengua("F"))
    
        score_Ex = calculate_score(get_average_score_extra("G"))
        score_Ex_Seg = calculate_score(get_average_score_extra("H"))
        score_Ex_Ter = calculate_score(get_average_score_extra("I"))
        
        score_Eco = calculate_score(get_average_score_economia("J"))
        score_Eco_Seg = calculate_score(get_average_score_economia("K"))
        score_Eco_Ter = calculate_score(get_average_score_economia("L"))
        
        score_Pro = calculate_score(get_average_score_programacion("M"))
        score_Pro_Seg = calculate_score(get_average_score_programacion("N"))
        score_Pro_Ter = calculate_score(get_average_score_programacion("O"))
    
        return score_M, score_Mat_Seg, score_Mat_Ter, score_L, score_Len_Seg, score_Len_Ter, score_Ex, score_Ex_Seg, score_Ex_Ter, score_Eco, score_Eco_Seg, score_Eco_Ter, score_Pro, score_Pro_Seg, score_Pro_Ter

@login_required(login_url="login_view")
def colegio(request):
        score_M, score_Mat_Seg, score_Mat_Ter, score_L, score_Len_Seg, score_Len_Ter, score_Ex, score_Ex_Seg, score_Ex_Ter, score_Eco, score_Eco_Seg, score_Eco_Ter, score_Pro, score_Pro_Seg, score_Pro_Ter = get_final_scores()
    
        return render(request, "Iggy_App/Utilities/Colegio.html", {
            "score_M": score_M,
            "score_Mat_Ter": score_Mat_Ter,
            "score_Mat_Seg": score_Mat_Seg,
            "score_L": score_L,
            "score_Len_Seg": score_Len_Seg,
            "score_Len_Ter": score_Len_Ter,
            "score_Ex": score_Ex,
            "score_Ex_Seg": score_Ex_Seg,
            "score_Ex_Ter": score_Ex_Ter,
            "score_Eco": score_Eco,
            "score_Eco_Seg": score_Eco_Seg,
            "score_Eco_Ter": score_Eco_Ter,
            "score_Pro": score_Pro,
            "score_Pro_Seg": score_Pro_Seg,
            "score_Pro_Ter": score_Pro_Ter
        })

@login_required(login_url="login_view")
def matematica_form(request):
    if request.method == "POST":
        matematica_form = Form_Matematica(request.POST)
        if matematica_form.is_valid():
            matematica_form.save()
            return redirect("inicio")
    else:
        score_M = calculate_score(get_average_score("A"))
        score_Mat_Seg = calculate_score(get_average_score("B"))
        score_Mat_Ter = calculate_score(get_average_score("C"))
        list_m = Matematica.objects.all()
        matematica_form = Form_Matematica()
        return render(request, "Iggy_App/Data/matematica.html", {"form": matematica_form, "list_m": list_m, "score_M":score_M, "score_Mat_Seg": score_Mat_Seg, "score_Mat_Ter": score_Mat_Ter})

@login_required(login_url="login_view")
def lengua_form(request):
    if request.method == "POST":
        lengua_form = Form_Lengua(request.POST)
        if lengua_form.is_valid():
            lengua_form.save()
            return redirect("inicio")
    else:
        score_L = calculate_score(get_average_score_lengua("D"))
        score_Len_Seg = calculate_score(get_average_score_lengua("E"))
        score_Len_Ter = calculate_score(get_average_score_lengua("F"))
        list_l = Lengua.objects.all()
        lengua_form = Form_Lengua()
        return render(request, "Iggy_App/Data/lengua.html", {"form": lengua_form, "score_L": score_L, "score_Len_Seg": score_Len_Seg, "score_Len_Ter": score_Len_Ter, "list_l": list_l })

@login_required(login_url="login_view")
def economia_form(request):
    if request.method == "POST":
        economia_form = Form_Economia(request.POST)
        if economia_form.is_valid():
            economia_form.save()
            return redirect("inicio")
    else:
        score_Eco = calculate_score(get_average_score_economia("J"))
        score_Eco_Seg = calculate_score(get_average_score_economia("K"))
        score_Eco_Ter = calculate_score(get_average_score_economia("L"))
        list_e = Economia.objects.all()
        economia_form = Form_Economia()
        return render(request, "Iggy_App/Data/economia.html", {"form": economia_form, "score_Eco": score_Eco, "score_Eco_Seg": score_Eco_Seg, "score_Eco_Ter": score_Eco_Ter, "list_e": list_e })

@login_required(login_url="login_view")
def programacion_form(request):
    if request.method == "POST":
        programacion_form = Form_Programacion(request.POST)
        if programacion_form.is_valid():
            programacion_form.save()
            return redirect("inicio")
    else:
        score_Pro = calculate_score(get_average_score_programacion("M"))
        score_Pro_Seg = calculate_score(get_average_score_programacion("N"))
        score_Pro_Ter = calculate_score(get_average_score_programacion("O"))
        list_p = Programacion.objects.all()
        programacion_form = Form_Programacion()
        return render(request, "Iggy_App/Data/programacion.html", {"form": programacion_form, "score_Pro": score_Pro, "score_Pro_Seg": score_Pro_Ter, "list_p": list_p})

@login_required(login_url="login_view")
def extra_form(request):
    if request.method == "POST":
        extra_form = Form_extra(request.POST)
        if extra_form.is_valid():
            extra_form.save()
            return redirect("inicio")
    else:
        score_Ex = calculate_score(get_average_score_extra("G"))
        score_Ex_Seg = calculate_score(get_average_score_extra("H"))
        score_Ex_Ter = calculate_score(get_average_score_extra("I"))
        list_ex = Extra_materia.objects.all()
        extra_form = Form_extra()
        return render(request, "Iggy_App/Data/extra.html", {"form": extra_form, "score_Ex": score_Ex, "score_Ex_Seg": score_Ex_Seg, "score_Ex_Ter": score_Ex_Ter, "list_ex": list_ex})

# eliminar datos

@login_required(login_url="login_view")
def matematica_form_delete(request, id):
    dato = Matematica.objects.get(id=id)
    dato.delete()
    return render(request, "Iggy_App/Utilities/Colegio.html")

@login_required(login_url="login_view")
def lengua_form_delete(request, id):
    dato = Lengua.objects.get(id=id)
    dato.delete()
    return render(request, "Iggy_App/Utilities/Colegio.html")

@login_required(login_url="login_view")
def economia_form_delete(request, id):
    dato = Economia.objects.get(id=id)
    dato.delete()
    return render(request, "Iggy_App/Utilities/Colegio.html")

@login_required(login_url="login_view")
def extra_form_delete(request, id):
    dato = Extra_materia.objects.get(id=id)
    dato.delete()
    return render(request, "Iggy_App/Utilities/Colegio.html")

@login_required(login_url="login_view")
def informatica_form_delete(request, id):
    dato = Programacion.objects.get(id=id)
    dato.delete()
    return render(request, "Iggy_App/Utilities/Colegio.html")

#log in, registrer, logout  

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
    else: 
        return render(request, "Iggy_App/Utilities/log_in.html");

def logout_view(request):
    logout(request)
    return redirect('inicio')