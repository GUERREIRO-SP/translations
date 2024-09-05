from django.shortcuts import render, redirect
from django.http import HttpResponse

# ...Importa os modelos das tabelas...
from translate.models import Translations, Language, Project
# ...Importa os campos do formulário criado...
from translate.forms import RegisterForms, RegisterLanguageForms, RegisterProjectForms

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


def language(request):
    return render(request, 'translate/language.html')

def create_language(request):
    if request.method =="POST":
        form = RegisterLanguageForms(request.POST)

        # Valida os campos do formulário
        # if form.is_valid():
        
        id_language = form["id"].value()
        name_language = form["name"].value()
        rtl_direction = form["rtl_direction"].value()

        # ..... Grava o registro na tabela, e direciona para a página de login...
        new_language = Language.objects.create(
            id = id_language,
            name = name_language,
            rtl_direction = rtl_direction
        )
        new_language.save()

    return redirect('language')


def project(request):
    return render(request, 'translate/project.html')

def create_project(request):
    if request.method =="POST":
        form = RegisterProjectForms(request.POST)

        # Valida os campos do formulário
        # if form.is_valid():
        
        # id_project = form["id"].value()
        name_project = form["name"].value()
        export_strategy = form["export_strategy"].value()

        # ..... Grava o registro na tabela, e direciona para a página de login...
        new_project = Project.objects.create(
            # id = id_project,
            name = name_project,
            export_strategy = export_strategy
        )
        new_project.save()

    return redirect('project')




def proj_lang(request):
    return render(request, 'translate/proj_lang.html')

def change(request):
    return render(request, 'translate/change.html')

def export(request):
    return render(request, 'translate/export.html')


##########  Lista Campos  ##########
class RegisterList(ListView):
    model = Translations
    template_name = "translate/list.html"

