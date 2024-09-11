from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView

# ...Importa os modelos das tabelas...
from translate.models import Language, Project, ProjectLanguage, Translations

# ...Importa os campos dos formulários criados...
from translate.forms import RegisterTranslationsForms, RegisterLanguageForms, RegisterProjectForms, RegisterProjectLanguageForms
from translate.forms import UpdateLanguageForms, UpdateTranslationsForms

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

        # ..... Grava o registro na tabela, e direciona para o list...
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

        # ..... Grava o registro na tabela, e direciona para o list...
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
            FROM    translate_language AS lng,  translate_project AS prj,  translate_projectlanguage AS pl
            WHERE   lng.id = pl.id_language  AND  prj.id = pl.id_project   
        """
        cur.execute(my_query)
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append({"id": i[0], "project_name": i[1], "language_name": i[2], "txt_limit": i[3]})

    return lista   



def list_translations(request):
    translations = load_translations()
    
    # print(translations)
    return render(request, 'translate/list_translations.html', {"translations":translations} )


def load_translations():
    # conexão com DB
    con = dblite.connect('db.sqlite3')
    
    lista = []
    with con:
        cur = con.cursor()

        my_query = """
            SELECT  tra.id, tra.id_project, prj.name AS project_name, tra.strategy, tra.key, tra.id_language AS language_name, 
                    tra.context, tra.value, tra.flag_export, tra.override_en 
            FROM    translate_translations AS tra, translate_project AS prj
            WHERE   tra.id_project = prj.id   
        """
        cur.execute(my_query)
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        
        
        
        print(f"QUERY TRANSLATIONS: {dados}")



        for i in dados:
            lista.append({"id": i[0], "id_project": i[1], "project_name": i[2], "strategy": i[3], "language_name": i[5], "key": i[4], "override_en": i[9]})

    return lista   








def project_language(request):
    projects = Project.objects.all() 
    languages = Language.objects.all()

    return render(request, 'translate/insert_project_language.html', {"prj":projects, "lng":languages})


def create_project_language(request):
    if request.method =="POST":
        form = RegisterProjectLanguageForms(request.POST)

        # Valida os campos do formulário
        # if form.is_valid():
        
        id_project = form["id_project"].value()
        id_language = form["id_language"].value()
        txt_limit = form["txt_limit"].value()

        # ..... Grava o registro na tabela, e direciona para o list...
        new_project_language = ProjectLanguage.objects.create(
            id_project = id_project,
            id_language = id_language,
            txt_limit = txt_limit
        )
        new_project_language.save()

    return redirect('list_project_language')


def translations(request):
    projects = Project.objects.all() 
    languages = Language.objects.all()

    return render(request, 'translate/insert_translations.html', {"prj":projects, "lng":languages})


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

        # ..... Grava o registro na tabela, e direciona para o list...
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


def update_language(request, id):
    if request.method =="POST":
        form = UpdateLanguageForms(request.POST)
        
        id_language = id
        name_language = form["name"].value()
        rtl_direction = form["rtl_direction"].value()

        print(f"Language - DIRECTION: {rtl_direction}")

        # ..... Grava o registro na tabela, e direciona para o list...
        # upd_language = 
        Language.objects.filter(id=id_language).update(
            name = name_language,
            rtl_direction = rtl_direction
        )

    return redirect('list_language')
    


def update_project(request, pk):
    pass


def update_projectlanguage(request, pk):
    pass


def update_translations(request, pk):
    if request.method =="POST":
        form = UpdateTranslationsForms(request.POST)

        id_translations = id
        id_project = form["id_project"].value()
        key = form["key"].value()
        strategy = form["strategy"].value()
        id_language = form["id_language"].value()
        context = form["context"].value()
        value = form["value"].value()
        override_en = form["override_en"].value()
        flag_export = form["flag_export"].value()

        # ..... Grava o registro na tabela, e direciona para o list...
        upd_translations = Translations.objects.filter(id=id_translations).update(
            id_project = id_project,
            key = key,
            strategy = strategy,
            id_language = id_language,
            context = context,
            value = value,
            override_en = override_en,
            flag_export = flag_export
        )

    return redirect('list_language')
    


########### MONTAGEM DAS TELAS ###########
def tela_update_language(request, **kwargs):
    print(kwargs)
    id = kwargs["id"]
    lng = Language.objects.get(id=id)
    
    return render(request, 'translate/update_language.html', {"lng":lng})


def tela_update_translations(request, **kwargs):
    projects = Project.objects.all() 
    languages = Language.objects.all()

    print(kwargs)
    id = kwargs["id"]
    tra = Translations.objects.get(id=id)
    
    return render(request, 'translate/update_translations.html', {"tra":tra, "prj":projects, "lng":languages})



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
    fields = ['name', 'rtl_direction']
    template_name = "translate/update_language.html"
    success_url = reverse_lazy("list_language")

class UpdateProject(UpdateView):
    model = Project
    fields = ['name', 'export_strategy']
    template_name = "translate/update_project.html"
    success_url = reverse_lazy("list_project")

class UpdateProjectLanguage(UpdateView):
    model = ProjectLanguage
    fields = ['id_project', 'id_language', 'txt_limit']
    template_name = "translate/update_project_language.html"
    success_url = reverse_lazy("list_project_language")

class UpdateTranslations(UpdateView):
    model = Translations
    fields = ['id_project', 'id_language', 'strategy', 'key', 'context', 'value', 'override_en', 'flag_export']
    template_name = "translate/update_translations.html"
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

