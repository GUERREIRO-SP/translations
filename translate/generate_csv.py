from django.shortcuts import render, redirect
import sqlite3 as dblite
from django import forms

# ...Importa os modelos das tabelas...
from translate.models import Project
from .views import setup_new_project



class ExportCSVForms(forms.Form):
    id_project = forms.CharField(
        label = "id_project",
        required = True,
        max_length = 36,
    )



##########################################
##############  START CSV  ###############
##########################################
def load_projects(request):
    projects = Project.objects.all() 

    return render(request,'translate/export_translations.html', {"prj":projects})


# def generate_csv(request, **kwargs):
def generate_csv(request):
    if request.method == "GET":
        form = ExportCSVForms(request.GET)
        
        id_prj = form["id_project"].value()

        lst_language = load_language(id_prj)

        lst_translations = load_translations(id_prj)


        print(f"Gerando csv: {id_prj}")
        print(f"List language: {lst_language}")
        print(f"List Translat: {lst_translations}")


    return redirect('export_translations')

###############  END CSV  ################
##########################################



##########################################
############  CONSULTA DADOS  ############
##########################################

def load_language(id_prj):
    # conexão com DB
    con = dblite.connect('db.sqlite3')

    # ..... Valida se há registros (en-US e pt-BR) na tabela ProjectLanguage, e cria caso negativo .....
    setup_new_project(id_prj)


    lista = []
    with con:
        cur = con.cursor()

        my_query = """
            SELECT  id_language  AS  language 
            FROM    translate_projectlanguage
            WHERE   id_project = ?;
        """
        cur.execute(my_query, [id_prj])
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append({i[0]})

    return lista 



def load_translations(id):
    # conexão com DB
    con = dblite.connect('db.sqlite3')
    
    lista = []
    with con:
        cur = con.cursor()

        my_query = """
               SELECT  tra.key, tra.id_language as language, tra.value
                 FROM  translate_translations as tra 
                WHERE  tra.id_project = ?  
                  AND  tra.flag_export = true
             ORDER BY  tra.key, tra.id_language;
        """
        cur.execute(my_query, [id])
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append({"key": i[0], "language": i[1], "value": i[2]})


        # ..............  aqui tratar montagem CSV  ..............


    return lista 







