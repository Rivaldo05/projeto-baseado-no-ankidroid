from tkinter import *
import os
from fontes import *

'''
minsize = define a altura e largura minima da janela
maxsize = define a altura e largura maxima da janela
resizeable = recebe dois valores (true e false) e defeni se a janela pode ou não ser redefinida

'''


# caminho do programa agenda
c = os.path.dirname(__file__)
nome_arquivo = c + "\\frases1.txt"


def add():
    janela_add_frase = Tk()
    janela_add_frase.geometry("500x300")
    janela_add_frase.title("projeto_anki")
    janela_add_frase.configure(bg="grey")
    janela_add_frase.iconbitmap("imagens/ad_frase.ico")
    janela_add_frase.resizable(FALSE, FALSE)

    # criando labels
    lb1 = Label(janela_add_frase, text="Insira a frase:", bg="grey", fg="blue", anchor="w", font=fonte2)
    lb2 = Label(janela_add_frase, text="Tradução da frase:", bg="grey", fg="blue", anchor="w", font=fonte2)
    lb3 = Label(janela_add_frase, text="OBS:", bg="grey", fg="blue", anchor="w", font=fonte2)

    # criando caixa de texto com multi linhas (entry - 1 linha, text - varias linhas)
    frase = Text(janela_add_frase, font=fonte2)
    caixa_traducao = Text(janela_add_frase, font=fonte2)
    caixa_obs = Text(janela_add_frase, font=fonte2)

    # inserindo componentes na tela
    lb1.place(x=10, y=10, width=100, height=20)
    frase.place(x=10, y=30, width=470, height=30)

    lb2.place(x=10, y=70, width=150, height=20)
    caixa_traducao.place(x=10, y=90, width=470, height=30)

    lb3.place(x=10, y=130, width=100, height=20)
    caixa_obs.place(x=10, y=150, width=470, height=50)

    def criar_arquivo():

        if frase.get("1.0", END) and caixa_traducao.get("1.0", END) != "":

            frase_entrada = frase.get("0.0", END)
            traducao = caixa_traducao.get("0.0", END)
            observacao = caixa_obs.get("0.0", END)

            arquivo = open(nome_arquivo, "a")
            arquivo.write(f"\nFrase: {frase_entrada}\n")
            arquivo.write(f"Tradução: {traducao}\n")
            arquivo.write(f"Obs: {observacao}\n")
            arquivo.write("**" * 30)

            arquivo.close()

            # depois de salvar os dados, delete o que estava escrito nas caixas de texto
            frase.delete("0.0", END)
            caixa_traducao.delete("0.0", END)
            caixa_obs.delete("0.0", END)

        else:
            print("ERRO")

    # inserindo botões
    bt_salvar = Button(janela_add_frase, text="adicionar dados", fg="blue", anchor="w", font=fonte,
                       command=lambda: criar_arquivo())
    bt_salvar.place(x=10, y=250, width=150, height=20)

