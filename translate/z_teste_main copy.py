from tkinter import ttk
from tkinter.ttk import *       # ...Uso do combobox...
from tkinter import font
from tkinter import messagebox
from tkinter import *

from z_teste_view import *  # ...Importar views...
import uuid6        # ...Importar uuID...

# Variável global...
global tree 


################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue


# Criar janelas
janela = Tk()
janela.title("")
janela.geometry('1355x670')
janela.configure(background=co1)
janela.resizable(width=False, height=False)


img = PhotoImage(file='logo_kbanner_pq.png')
# lbl_image = Label(janela, image=img, bg='#001831').pack

# tkimage = ImageTk.PhotoImage(Image.open("bola.jpg"))
# tk.Label(janela, image=tkimage).pack()
# logo = ImageTk.PhotoImage(r'logo_kbanner_pq.png')


# Dividindo a tela para os elementos
# frame_superior = Frame(janela, width=300, height=70, bg='#001831', relief='flat')
frame_superior = Frame(janela, width=300, height=40, bg=co1, relief='flat')
frame_superior.grid(row=0, column=0)

# frame_filtro = Frame(janela, width=300, height=50, bg=co1, relief='flat')
# frame_filtro.grid(row=0, column=0, sticky=NSEW, padx=0, pady=1)

frame_inferior = Frame(janela, width=300, height=400, bg=co1, relief='flat')
frame_inferior.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=1100, height=600, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, sticky=NSEW, padx=1, pady=0) 


# Label tela
# lbl_tela = Label(frame_superior, image=img, anchor=NW, bg='#001831', relief='flat')
# lbl_tela.place(x=1, y=1)
# lbl_filtro = Label(frame_filtro, text='Filtro Id_Project:', anchor=NW, font=('Ivy 13 bold'), bg=co1, fg=co0, relief='flat')





def display_dados():

    global tree

    # lista = [
    #     [1, '019184be-bd1b-7c0f-aa37-a3cf1bc27f51', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'ChatGPT', 'pt-br', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', '<color=#808080>Consegui!</color>', True],
    #     [2, '019184bf-2efa-7107-8f78-c4f5e69cdfcf', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'ChatGPT', 'es-419', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', ' <color=#808080>¡Lo conseguí!</color>', True],
    #     [3, '019184bf-d77a-819e-a0fd-55cfe6f93456', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'Manual', 'en-us', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', ' <color=#808080>Got it!</color>', True],
    #     [4, '019184bf-d77a-819e-a0fd-55cfe6f93766', '019184bf-d77a-819e-a0fd-55cfe6f93763', 'Google', 'pt-br', 'GWA_PURCHASED_PRODUCT_PRICE_KEY', '<color=#808080>Consegui!</color>', True]
    #     ]

    lista = select_translations()

    # lista table head
    tabel_head = ['id', 'Id_Project', 'Strategy', 'Language', 'Key', 'Value', 'Exp.']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabel_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd= ["nw", "nw", "nw", "nw", "nw", "nw", "center"]
    h = [200, 200, 60, 60, 180, 150, 50]
    n=0

    for col in tabel_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n] ,anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)




    

def insert_dados_tela():
    
    # Valida se é Insert ou Updade do registro...
    id_trans = e_id_trans.get()
    if id_trans == "":
        # Gera o uuid do registro...
        id_trans = str(uuid6.uuid7())


    id_proj = e_id_proj.get() 
    strategy = cbo_strategy.get() 
    language = cbo_language.get() 
    export = option_chk_export.get()       
    key = e_key.get() 
    context = e_context.get() 
    value = e_value.get() 
    override = e_override.get() 

    lista = [id_trans, id_proj, strategy, key, language, context, value, override, export]

    if id_trans == "":
        messagebox.showerror('Erro', 'Informe o id Translator')
    else:
        insert_translations(lista)
        messagebox.showerror('Sucesso', 'Dados inseridos com sucesso...')

        e_id_trans.delete(0, 'end') 
        e_id_proj.delete(0, 'end') 
        e_key.delete(0, 'end')
        e_context.delete(0, 'end')
        e_value.delete(0, 'end')
        e_override.delete(0, 'end')
        cbo_strategy.delete(0, 'end')
        cbo_language.delete(0, 'end')
        option_chk_export.set(False)
        

    for widget in frame_direita.winfo_children():
        widget.destroy()


    # Chamada da função que monta a tela...
    display_dados()




# Atualiza registros
def atualiza_dados_tela():
    try:
        dados_selecionados = tree.focus()
        dados_dicionario = tree.item(dados_selecionados)
        dados_lista = dados_dicionario['values']

        id_registro = str(dados_lista[0])

        e_id_trans.delete(0, 'end') 
        e_id_proj.delete(0, 'end') 
        e_key.delete(0, 'end')
        e_context.delete(0, 'end')
        e_value.delete(0, 'end')
        e_override.delete(0, 'end')
        cbo_strategy.delete(0, 'end')
        cbo_language.delete(0, 'end')
        option_chk_export.set(False) 


        # Habilita preenchimento do campo...
        e_id_trans["state"] = "normal"

        e_id_trans.insert(0, dados_lista[0]) 
        e_id_proj.insert(0, dados_lista[1]) 
        e_key.insert(0, dados_lista[4])
        e_value.insert(0, dados_lista[5])
        e_context.insert(0, dados_lista[7])
        e_override.insert(0, dados_lista[8])
        cbo_strategy.insert(0, dados_lista[2])
        cbo_language.insert(0, dados_lista[3])
        option_chk_export.set(dados_lista[6])

        # Inibe edição do campo...
        e_id_trans["state"] = "disabled"

        # Atualiza registro...
        def update_registro():
            id_trans = e_id_trans.get() 
            id_proj = e_id_proj.get() 
            key = e_key.get() 
            context = e_context.get() 
            value = e_value.get() 
            override = e_override.get() 
            strategy = cbo_strategy.get() 
            language = cbo_language.get() 
            export = option_chk_export.get()
        
            lista = [id_trans, id_proj, strategy, key, language, context, value, override, export, id_registro]

            print(lista)

            if id_trans == "":
                messagebox.showerror('Erro', 'Informe o id Translator')
            else:
                update_translations(lista)
                messagebox.showerror('Sucesso', 'Dados atualizados com sucesso...')

                e_id_trans.delete(0, 'end') 
                e_id_proj.delete(0, 'end') 
                e_key.delete(0, 'end')
                e_context.delete(0, 'end')
                e_value.delete(0, 'end')
                e_override.delete(0, 'end')
                cbo_strategy.delete(0, 'end')
                cbo_language.delete(0, 'end')
                option_chk_export.set(False)        

            for widget in frame_direita.winfo_children():
                widget.destroy()


        b_confirma = Button(frame_inferior, command=update_registro, text='Confirma', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirma.place(x=155, y=350)


        # Chamada da função que monta a tela...
        display_dados()



    except IndexError:
        messagebox.showerror('Erro', 'Selecione registro na lista...')



# Atualiza registros
def deleta_dados_tela():
    try:
        dados_selecionados = tree.focus()
        dados_dicionario = tree.item(dados_selecionados)
        dados_lista = dados_dicionario['values']

        # Atribui o vlr registro como lista []
        id_registro = [str(dados_lista[0])]

        delete_translations(id_registro)

        messagebox.showerror('Sucesso', 'Dados deletados com sucesso...')
        
        for widget in frame_direita.winfo_children():
            widget.destroy()


        # Chamada da função que monta a tela...
        display_dados()


    except IndexError:
        messagebox.showerror('Erro', 'Selecione registro na lista...')




# Alterna/Captura valor do flag_export
def opt_chk_export():

    option_chk_export.get()






# Frame superior
#  l_id_proj = Label(frame_superior, text='Filtro Project:', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
#  l_id_proj.place(x=0, y=20)
# lbl_tela = Label(frame_superior, anchor=NW, bg='#001831', relief='flat')
lbl_tela = Label(frame_superior, text='Filtro Id_Project:', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
lbl_tela.place(x=0, y=1)

cbo_project = Combobox(frame_superior)
cbo_project['values'] = Load_project()
cbo_project.current(0)     # Posiciona no 1º item do combo
cbo_project.grid(row=0, column=0, padx=0, pady=20, sticky=NSEW)

# Frame inferior
l_id_trans = Label(frame_inferior, text='ID Translation *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_id_trans.place(x=10, y=10)
e_id_trans = Entry(frame_inferior, width=60, justify='left', relief='solid', state='disabled')
e_id_trans.place(x=16, y=30)

l_id_proj = Label(frame_inferior, text='ID Project *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_id_proj.place(x=10, y=50)
e_id_proj = Entry(frame_inferior, width=60, justify='left', relief='solid')
e_id_proj.place(x=16, y=70)

l_key = Label(frame_inferior, text='Key ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_key.place(x=10, y=90)
e_key = Entry(frame_inferior, width=60, justify='left', relief='solid')
e_key.place(x=16, y=110)

l_context = Label(frame_inferior, text='Context ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_context.place(x=10, y=130)
e_context = Entry(frame_inferior, width=60, justify='left', relief='solid')
e_context.place(x=16, y=150)

l_value = Label(frame_inferior, text='Value ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_value.place(x=10, y=170)
e_value = Entry(frame_inferior, width=60, justify='left', relief='solid')
e_value.place(x=16, y=190)

l_override = Label(frame_inferior, text='Override ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_override.place(x=10, y=210)
e_override = Entry(frame_inferior, width=60, justify='left', relief='solid')
e_override.place(x=16, y=230)


# Campos originais para strategy e language
# l_strategy = Label(frame_inferior, text='Strategy *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
# l_strategy.place(x=10, y=250)
# e_strategy = Entry(frame_inferior, width=16, justify='left', relief='solid')
# e_strategy.place(x=16, y=270)

# l_language = Label(frame_inferior, text='Language *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
# l_language.place(x=150, y=250)
# e_language = Entry(frame_inferior, width=16, justify='left', relief='solid')
# e_language.place(x=156, y=270)




# Cobobox strategy e language
l_strategy = Label(frame_inferior, text='Strategy *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_strategy.place(x=10, y=250)
cbo_strategy = Combobox(frame_inferior)
cbo_strategy['values'] = ('ChatGPT', 'Google', 'Manual')
cbo_strategy.current(0)     # Posiciona no 1º item do combo
cbo_strategy.grid(row=1, column=16, padx=16, pady=270, sticky=NSEW)

l_language = Label(frame_inferior, text='Language *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_language.place(x=230, y=250)
cbo_language = Combobox(frame_inferior)
cbo_language['values'] = Load_language()       # ('en-us', 'es-419', 'pt-br')
cbo_language.current(0)     # Posiciona no 1º item do combo
cbo_language.grid(row=1, column=90, padx=60, pady=270, sticky=NSEW,)


# l_id_proj = Label(frame_inferior, text='ID Project *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
# l_id_proj.place(x=10, y=300)
# cbo_project = Combobox(frame_inferior)
# cbo_project['values'] = Load_project()
# cbo_project.current(0)     # Posiciona no 1º item do combo
# cbo_project.grid(row=1, column=16, padx=16, pady=320, sticky=NSEW)

option_chk_export = BooleanVar()
chk_export = Checkbutton(frame_inferior, var=option_chk_export, onvalue=1, offvalue=0, command=opt_chk_export, text='Flag_Export ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
chk_export.place(x=16, y=300)



# Botoes
b_ins = Button(frame_inferior, command=insert_dados_tela, text='Insert', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_ins.place(x=70, y=330)

b_upd = Button(frame_inferior, command=atualiza_dados_tela, text='Update', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_upd.place(x=155, y=330)

b_del = Button(frame_inferior, command=deleta_dados_tela, text='Delete', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_del.place(x=240, y=330)





# Chamada da função que monta a tela...
display_dados()



janela.mainloop()

