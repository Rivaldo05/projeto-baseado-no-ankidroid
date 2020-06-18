from tkinter import *
import os

# caminho do programa agenda
c = os.path.dirname(__file__)
nome_arquivo= c+"\\frases1.txt"


def add():

    janela_add_frase = Tk()
    janela_add_frase.geometry("500x300")
    janela_add_frase.title("projeto_anki")
    janela_add_frase.configure(bg="grey")


    # criando labels
    lb1 = Label(janela_add_frase, text="Insira a frase:", bg="grey", fg="blue", anchor="w")
    lb2 = Label(janela_add_frase, text="Tradução da frase:", bg="grey", fg="blue", anchor="w")
    lb3 = Label(janela_add_frase, text="OBS:", bg="grey", fg="blue", anchor="w")

    # criando caixa de texto com multi linhas (entry - 1 linha, text - varias linhas)
    frase = Text(janela_add_frase)
    caixa_traducao = Text(janela_add_frase)
    caixa_obs = Text(janela_add_frase)

    # inserindo componentes na tela
    lb1.place(x=10, y=10, width=100, height=20)
    frase.place(x=10, y=30, width=300, height=30)

    lb2.place(x=10, y=70, width=100, height=20)
    caixa_traducao.place(x=10, y=90, width=300, height=30)

    lb3.place(x=10, y=130, width=100, height=20)
    caixa_obs.place(x=10, y=150, width=300, height=50)



    def criar_arquivo():
        frase_entrada = frase.get("0.0", END)
        traducao = caixa_traducao.get("0.0", END)
        observacao = caixa_obs.get("0.0", END)

        arquivo = open(nome_arquivo, "a")
        arquivo.write(f"\nFrase: {frase_entrada}\n")
        arquivo.write(f"Tradução: {traducao}\n")
        arquivo.write(f"Obs: {observacao}\n")
        arquivo.write("**"*30)

        arquivo.close()

    # inserindo botões
    bt_salvar = Button(janela_add_frase, text="adicionar dados", fg="blue", anchor="w", command=lambda: criar_arquivo())
    bt_salvar.place(x=10, y=250, width=100, height=20)

    # janela_add_frase.	mainloop()