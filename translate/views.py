from django.shortcuts import render, redirect
from django.http import HttpResponse
from translate.models import Translations
from translate.forms import RegisterForms   # Importa os campos do formulário criado
from .generate_uuid import get_a_uuid
from django.views.generic.list import ListView

def index(request):
    translations = Translations.objects.all()
    return render(request, 'translate/index.html', {"cards": translations})

def register(request):
    form = RegisterForms()

    # Gera o uuid do registro...
    uuid7 = get_a_uuid()

    return render(request, 'translate/register.html', {"form": form})

def ins_register(request):
    form = RegisterForms()
    if request.method =="POST":
        form = RegisterForms(request.POST)

        # Valida os campos do formulário
        if form.is_valid():
            
            id = form["id"].value()
            id_project = form["id_project"].value()
            strategy = form["strategy"].value()
            key = form["key"].value()
            language = form["language"].value()
            context = form["context"].value()
            value = form["value"].value()
            override_en = form["override_en"].value()
            flag_export = form["flag_export"].value()

            # Gera o uuid do registro...
            uuid7 = get_a_uuid()

            # ..... Grava o registro na tabela, e direciona para a página de login...
            register = Translations.objects.create_xxxxxxxx(
                username = nome,
                email = email,
                password = senha
            )
            translations.save()
            return redirect("register")

    return render(request, 'translate/register.html', {"form": form})


def change(request):
    return render(request, 'translate/change.html')


def export(request):
    return render(request, 'translate/export.html')

##########  Lista Campos  ##########
class RegisterList(ListView):
    model = Translations
    template_name = "translate/list.html"
