from django.shortcuts import render, redirect
import sqlite3 as dblite
import csv
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



def generate_file(request):
    if request.method == "GET":
        form = ExportCSVForms(request.GET)
        
        str_type = form["type_file"].value()

        print(str_type)
        
        if str_type=="CSV":
            generate_csv(request)
        elif str_type=="JSON":
            generate_JSON(request)
        else:
            generate_TXT(request)


# def generate_csv(request, **kwargs):
def generate_csv11(request):
    if request.method == "GET":
        form = ExportCSVForms(request.GET)
        
        id_prj = form["id_project"].value()

        lst_language = load_language(id_prj)

        lst_translations = load_translations(id_prj)


    return redirect('export_translations')

###############  END CSV  ################
##########################################



##########################################
############  CONSULTA DADOS  ############
##########################################

def load_language111(id_prj):
    # conexão com DB
    con = dblite.connect('db.sqlite3')

    # ..... Valida se há registros (en-US e pt-BR) na tabela ProjectLanguage, e cria caso negativo .....
    setup_new_project(id_prj)

    lista = []
    with con:
        cur = con.cursor()

        my_query = """
            SELECT   id_language  AS  language 
            FROM     translate_projectlanguage
            WHERE    id_project = ?
            ORDER BY id_language;
        """
        cur.execute(my_query, [id_prj])
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append(i[0])

    return lista 



def load_key_translations111(id):
    # conexão com DB
    con = dblite.connect('db.sqlite3')
    
    lista = []
    with con:
        cur = con.cursor()

        my_query = """
               SELECT  DISTINCT tra.key
                 FROM  translate_translations as tra 
                WHERE  tra.id_project = ?  
                  AND  tra.flag_export = true
             ORDER BY  tra.key;
        """
        cur.execute(my_query, [id])
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for line in dados:
            lista.append(line[0])

    return lista 



def load_translations111(id):
    # conexão com DB
    con = dblite.connect('db.sqlite3')
    
    translate_dic = {}

    lst_key = load_key_translations(id)

    lst_language = load_language(id)


    # print(f"LIST-KEY {lst_key}")
    # print(f"LIST-LANGUAGE {lst_language}")


    for id_key in lst_key:

        translate_dic[id_key] = {}

        for id_lang in lst_language:

            # Popula o dicionário com Key e Language (vazio)
            # {'GWA_PURCHASED': {'en-US': '', 'es-419': '', 'fr-FR': '', 'ja-JP': '', 'pt-BR': ''}, 
            #  'PRODUCT_PRICE_KEY': {'en-US': '', 'es-419': '', 'fr-FR': '', 'ja-JP': '', 'pt-BR': ''}}
            translate_dic[id_key][id_lang] = ""  


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

        # ..............  Montagem do CSV  ..............
        with open("csv_file.csv", "w", encoding="utf8", newline="") as csvfile:
            head_file = ("Key", "Language", "Translation")
            writer = csv.writer(csvfile)
            writer.writerow(head_file)

            for line in dados:

                translate_dic[line[0]][line[1]] = line[2]  

                writer.writerow((line[0], line[1], line[2]))

    # print(f"FINAL {translate_dic}")

    return None 







