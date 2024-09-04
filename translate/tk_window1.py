

from tkinter import *

class exemplo:
    def __init__(self, tk):
        self.frame1 = Frame(tk)
        self.frame2 = Frame(tk)
        self.frame3 = Frame(tk)

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()

        self.Botao1 = Button(self.frame1, text='Clique nesse botão para alterar.', command=self.alterar, bg='green')
        self.entrada1 = Label(self.frame2, text='Usuário:', width=8, height=2)
        self.entrada2 = Entry(self.frame2)

        self.Botao1.pack()
        self.entrada1.pack(side=LEFT)
        self.entrada2.pack(side=LEFT)

    def alterar(self):
        self.Botao1.pack_forget() #Retiro todos esses
        self.entrada1.pack_forget() #Retiro todos esses
        self.entrada2.pack_forget() #Retiro todos esses

        # E no frame aonde os três acima estavam, eu coloquei esses:
        self.Botao2 = Button(self.frame3, text='Clique nesse botão para voltar.', command=self.reverter, bg='darkgray')
        self.entrada3 = Label(self.frame2, text='Digite algo acima', height=2)
        self.entrada4 = Entry(self.frame1)

        self.Botao2.pack()
        self.entrada3.pack(side=LEFT)
        self.entrada4.pack(side=LEFT)

    def reverter(self):
        self.Botao1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada1.pack() # Para reverter eu simplesmente dei .pack() nesses
        self.entrada2.pack() # Para reverter eu simplesmente dei .pack() nesses

        self.Botao2.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
        self.entrada3.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
        self.entrada4.pack_forget() # e "eliminei esses". Se isso não for feito, ambos ocupam o mesmo Frame.
ex = Tk()
exemplo(ex)
ex.mainloop()

####################################################################
# import tkinter

# raiz = None
# janelas = []

# def criar():
#     janela = tkinter.Toplevel(raiz)
#     janela.title("janela  {}".format(len(janelas)))
#     janelas.append(janela)

# def destruir():
#     janelas.pop(0).destroy()

# def principal():
#     global raiz
#     raiz = tkinter.Tk()
#     bt_criar = tkinter.Button(raiz, text="criar", command=criar)
#     bt_destruir = tkinter.Button(raiz, text="destruir", command=destruir)
#     bt_criar.pack(side="left")
#     bt_destruir.pack(side="right")

# principal()
# tkinter.mainloop()
####################################################################
