from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

# ...Importa os modelos das tabelas...
from translate.models import Language, Project, ProjectLanguage, Translations

# ...Importa os campos dos formulários criados...
from translate.forms import RegisterTranslationsForms, RegisterLanguageForms, RegisterProjectForms, RegisterProjectLanguageForms

from .generate_uuid import get_a_uuid

import sqlite3 as dblite



def index(request):
    translations = Translations.objects.all()
    return render(request, 'translate/index.html', {"cards": translations})


def language(request):
    return render(request, 'translate/insert_language.html')


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

    return redirect('list_language')


def project(request):
    return render(request, 'translate/insert_project.html')


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

    return redirect('list_project')


def list_project_language(request):
    project_language = load_project_language()
    
    print(project_language)

    return render(request, 'translate/list_project_language.html', {"project_language":project_language} )


# Acessar dados da tabela translations
def load_project_language():
    # conexão com DB
    con = dblite.connect('db.sqlite3')
    
    lista = []
    with con:
        cur = con.cursor()

        my_query = """
            SELECT  pl.id, prj.name as project_name, lng.name as language_name, pl.txt_limit 
            FROM    translate_language as lng,  translate_project as prj,  translate_projectlanguage as pl
            WHERE   lng.id = pl.id_language  AND  prj.id = pl.id_project   
        """
        cur.execute(my_query)
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append({"id": i[0], "project_name": i[1], "language_name": i[2], "txt_limit": i[3]})

    return lista   


def project_language(request):
    projects = Project.objects.all() 
    languages = Language.objects.all()

    return render(request, 'translate/insert_project_language.html', {"prj":projects, "lng":languages} )


def create_project_language(request):
    if request.method =="POST":
        form = RegisterProjectLanguageForms(request.POST)

        # Valida os campos do formulário
        # if form.is_valid():
        
        id_project = form["id_project"].value()
        id_language = form["id_language"].value()
        txt_limit = form["txt_limit"].value()

        # ..... Grava o registro na tabela, e direciona para a página de login...
        new_project_language = ProjectLanguage.objects.create(
            id_project = id_project,
            id_language = id_language,
            txt_limit = txt_limit
        )
        new_project_language.save()

    return redirect('list_project_language')


def translations(request):
    return render(request, 'translate/insert_translations.html')


def create_translations(request):
    if request.method =="POST":
        form = RegisterTranslationsForms(request.POST)

        # Valida os campos do formulário
        # if form.is_valid():
        project = form["id_project"].value()
        language = form["id_language"].value()
        strategy = form["strategy"].value()
        key = form["key"].value()
        context = form["context"].value()
        value = form["value"].value()
        override_en = form["override_en"].value()
        flag_export = form["flag_export"].value()

        # ..... Grava o registro na tabela, e direciona para a página de login...
        new_translations = Translations.objects.create(
            id_project = project,
            id_language = language,
            strategy = strategy,
            key = key,
            context = context,
            value = value,
            override_en = override_en,
            flag_export = flag_export,
        )
        new_translations.save()

    return redirect('list_translations')



##########  Classes para Views dos registros  ##########
class ListTranslations(ListView):
    model = Translations
    template_name = "translate/list_translations.html"


class ListLanguage(ListView):
    model = Language
    template_name = "translate/list_language.html"


class ListProject(ListView):
    model = Project
    template_name = "translate/list_project.html"


########## UPDATE ########## 
class UpdateLanguage(UpdateView):
    model = Language
    fields = ['id', 'name', 'rtl_direction']
    template_name = "translate/update_form.html"
    success_url = reverse_lazy("list_language")

class UpdateProject(UpdateView):
    model = Project
    fields = ['id', 'name', 'export_strategy']
    template_name = "translate/update_form.html"
    success_url = reverse_lazy("list_project")

class UpdateProjectLanguage(UpdateView):
    model = ProjectLanguage
    fields = ['id_project', 'id_language', 'txt_limit']
    template_name = "translate/update_form.html"
    success_url = reverse_lazy("list_project_language")

class UpdateTranslations(UpdateView):
    model = Translations
    fields = ['id_project', 'id_language', 'strategy', 'key', 'context', 'value', 'override_en', 'flag_export']
    template_name = "translate/update_form.html"
    success_url = reverse_lazy("list_translations")


########## DELETE ########## 
class DeleteLanguage(DeleteView):
    model = Language
    template_name = "translate/delete_form.html"
    success_url = reverse_lazy("list_language")

class DeleteProject(DeleteView):
    model = Project
    template_name = "translate/delete_form.html"
    success_url = reverse_lazy("list_project")

class DeleteProjectLanguage(DeleteView):
    model = ProjectLanguage
    template_name = "translate/delete_form.html"
    success_url = reverse_lazy("list_project_language")

class DeleteTranslations(DeleteView):
    model = Translations
    template_name = "translate/delete_form.html"
    success_url = reverse_lazy("list_translations")

