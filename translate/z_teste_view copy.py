import sqlite3 as dblite

# conexão com DB
con = dblite.connect('dbtranslations.db')


# Acessar dados da tabela translations
def select_translations():
    lista = []
    with con:
        cur = con.cursor()

        my_query = """
            SELECT  id,	id_project, strategy, language,	
                    key, value, flag_export, context, override_en
            FROM translations
        """
        cur.execute(my_query)
        dados = cur.fetchall()      # Retorna todos os registros da tabela
        
        for i in dados:
            lista.append(i)

    return lista        


# Inserir dados na tabela
def insert_translations(dados):
    with con:
        cur = con.cursor()

    # lista = [id_trans, id_proj, strategy, key, language, context, value, override, export]

        my_query = """
                INSERT INTO translations (
                    id,
                    id_project,	
                    strategy,	
                    key,		
                    language,	
                    context,	
                    value,	
                    override_en, 
                    flag_export)	
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(my_query, dados)


# Atualizar dados da tabela
def update_translations(dados):
    
    with con:
        cur = con.cursor()

            # lista = [id_trans, id_proj, strategy, key, language, context, value, override, export, id_registro]

        my_query = "UPDATE translations  SET  (id=?, id_project=?, strategy=?, key=?, language=?, context=?, value=?, override_en=?, flag_export=?)  VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?)  WHERE id=?"

        # my_query = """
        #     UPDATE translations  
        #     SET  (id=?, 
        #           id_project=?, 
        #           strategy=?, 
        #           key=?, 
        #           language=?, 
        #           context=?, 
        #           value=?, 
        #           override_en=?, 
        #           flag_export=?)  
        #     VALUES  (?, ?, ?, ?, ?, ?, ?, ?, ?)  
        #     WHERE id=?
        #     """

        print(my_query)
        print(dados)

        cur.execute(my_query, dados)


# Deletar dados da tabela
def delete_translations(dados):
    with con:
        cur = con.cursor()

        my_query = "DELETE FROM translations WHERE id=?"
        cur.execute(my_query, dados)


# Acessar dados da tabela language
def Load_language():
    lista = []
    with con:
        cur = con.cursor()

        my_query = "SELECT  DISTINCT  language  FROM  language  ORDER BY  language"
        cur.execute(my_query)
        dados = cur.fetchall()      # Retorna os registros da tabela
        
        for i in dados:
            lista.append(i)

    return lista


# Acessar dados da tabela project
def Load_project(): 
    lista = []
    with con:
        cur = con.cursor()

        # my_query = "SELECT  DISTINCT  id_project, dsc_project  FROM  project  ORDER BY  dsc_project"
        my_query = "SELECT  DISTINCT  dsc_project, id_project  FROM  project  ORDER BY  dsc_project"
        cur.execute(my_query)
        dados = cur.fetchall()      # Retorna os registros da tabela
        
        for i in dados:
            lista.append(i)

    return lista

