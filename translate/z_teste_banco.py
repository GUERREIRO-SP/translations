import sqlite3 as dblite

# conexão com DB
con = dblite.connect('dbtranslations.db')

# Cria Tabelas
create_table_translations = """
CREATE TABLE translations(
    id VARCHAR(36) PRIMARY KEY,
    id_project VARCHAR(36) NOT NULL,	
    strategy VARCHAR(255) NOT NULL,	
    key VARCHAR(255) NOT NULL,		
    language VARCHAR(25) NOT NULL,	
    context VARCHAR(1000),	
    value VARCHAR(1000),	
    override_en VARCHAR(1000),	
    flag_export BOOLEAN);
"""

create_table_language = """
CREATE TABLE language(
    language VARCHAR(25) PRIMARY KEY,	
    dsc_language VARCHAR(100),	
    rtl_direction BOOLEAN);
"""

create_table_project = """
CREATE TABLE project(
    id_project VARCHAR(36) PRIMARY KEY,	
    dsc_project VARCHAR(255) NOT NULL,	
    export_strategy VARCHAR(255));
"""

create_table_project_language = """
CREATE TABLE project_language(
    id VARCHAR(36) PRIMARY KEY,
    id_project VARCHAR(36) NOT NULL,	
    language VARCHAR(25) NOT NULL,	
    txt_limit INT);
"""



# Abre DB, cria tabelas e fecha o DB...
# with con:
#     cur = con.cursor()
    
#     cur.execute(create_table_translations)
#     cur.execute(create_table_language)
#     cur.execute(create_table_project)
#     cur.execute(create_table_project_language)


# Popula tabelas
popula_language = """
INSERT INTO language VALUES
('en-us', 'English - USA', False),
('es-419', 'Spanish - 419', False),
('es-es', 'Spanish - Spain', False),
('fr-ca', 'French - Canada', False),
('ja-jp', 'Japanese - Japan', False),
('pt-br', 'Portugues - Brasil', False);
"""

popula_project = """
INSERT INTO project VALUES
('019184bf-d77a-819e-a0fd-55cfe6f93763', 'NORDICA VILLAGE', '');
"""	

popula_translations = """
INSERT INTO translations VALUES
('019184be-bd1b-7c0f-aa37-a3cf1bc27f51', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'ChatGPT', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', 'pt-br', '', '<color=#808080>Consegui!</color>', '', True),
('019184bf-2efa-7107-8f78-c4f5e69cdfcf', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'ChatGPT', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', 'es-419', '', 'this got it means that I HAVE IT PURCHASED, and keep in english"	<color=#808080>¡Lo conseguí!</color>', '', True),
('019184bf-d77a-819e-a0fd-55cfe6f93456', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'Manual', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', 'en-us', '', 'this got it means that I HAVE IT PURCHASED, and keep the code part in english"	<color=#808080>Got it!</color>', '', True),
('019184bf-d77a-819e-a0fd-55cfe6f93766', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'Google', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', 'pt-br', '', '<color=#808080>Consegui!</color>', '', True);
"""

delete_language = """
    DELETE FROM language WHERE ROWID=7
"""


with con:
    cur = con.cursor()
    # cur.execute(popula_language)
    # cur.execute(popula_project)
    # cur.execute(popula_translations)
    # cur.execute(delete_language)


