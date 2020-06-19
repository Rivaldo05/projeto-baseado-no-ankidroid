from tkinter import *
from adicionar_frases import *
from fontes import *


def janela_dados():
    def ver_dados_salvos():
        try:
            arquivo = open("frases1.txt", "r")
            arquivo_leitura = arquivo.read()
            tex.insert(1.0, arquivo_leitura)
        except:
            bt1["text"] = "ERRO! Documento nao encontrado"



    janela_dados =Tk()
    janela_dados.title("Banco de dados")
    janela_dados.geometry("700x600")
    janela_dados.resizable(FALSE, FALSE)  # impede que a janela seja redimensionada
    janela_dados.configure(bg="gray")
    janela_dados.iconbitmap("imagens/ad_frase.ico")

    bt1 = Button(janela_dados, text="Ver dados", command=ver_dados_salvos)
    bt1.pack()

    tex = Text(janela_dados, font=fonte3, fg="blue")
    tex.place(x=0, y=30, height=580, width=700)


    janela_dados.mainloop()
