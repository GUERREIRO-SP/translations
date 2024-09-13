from django.shortcuts import render, redirect
import sqlite3 as dblite
from django import forms

# ...Importa os modelos das tabelas...
from translate.models import Project


class ExportForms(forms.Form):
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
        form = ExportForms(request.GET)
        
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
##########  CRIA TB TEMPORARIA  ##########
##########################################

def load_language(id):
    # conexão com DB
    con = dblite.connect('db.sqlite3')
    
    lista = []
    with con:
        cur = con.cursor()

        my_query = """
            SELECT  id_language  AS  language 
            FROM    translate_projectlanguage
            WHERE   id_project = ?;
        """
        cur.execute(my_query, [id])
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append({i[0]})
            # lista.append({"language": f("{i[0]} VARCHAR(255), ")})

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
             ORDER  BY tra.key, tra.id_language;
        """
        cur.execute(my_query, [id])
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append({"key": i[0], "language": i[1], "value": i[2]})


        # ..............  aqui tratar montagem CSV  ..............


    return lista 



def create_table_export_csv_tmp(lst_language):
    # conexão com DB
    con = dblite.connect('db.sqlite3')
    cur = con.cursor()

    sql_drop = "DROP TABLE IF EXISTS export_csv_tmp;";
    con.execute(sql_drop);

    # qtd = cur.execute("SELECT count(*) FROM db.sqlite3 WHERE type='table' AND name='export_csv_tmp';").fetchmany()

    # Cria Tabelas
    create_table_csv_tmp = """
    CREATE TABLE IF NOT EXISTS export_csv_tmp(
        project(255) PRIMARY KEY,
        key VARCHAR(255) NOT NULL,		
        {lst_language});
    """
    with con:
        cur = con.cursor()
        cur.execute(create_table_csv_tmp)

    cur.commit()
    cur.close()




