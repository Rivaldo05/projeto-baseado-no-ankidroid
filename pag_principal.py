from tkinter import *

from adicionar_frases import *
from banco_dados import *


def nova_frase():
    add()


def tudo_certo():
    print(f"essa mensagem indica qeu o botão \"pesquisar\"funciona")


def ver_dados():
    janela_dados()


janela = Tk()
janela.geometry("400x400")
janela.title("Projeto_anki")
janela.configure(bg="gray")
janela.minsize(200, 200)
janela.maxsize(600, 500)

# definindo icone da pagina principal
janela.iconbitmap("imagens/icone_principal.ico")

# criando menu
barra_menu = Menu(janela, font=fonte3)  # menu ligado a janela

# para cada menu que for feito tem que repetir o mesmo processo
menu_opcao = Menu(barra_menu, tearoff=0)  # retira umas linhas que fazem o menu sair fora do programa
menu_opcao.add_command(label="Adicionar", command=nova_frase, font=fonte3)
menu_opcao.add_command(label="Pesquisar", command=tudo_certo, font=fonte3)  # adicionar comando para pesquisar uma frase especifica
menu_opcao.add_separator()  # adiciona uma linha separando os contatos
menu_opcao.add_command(label="Fechar", command=janela.quit,font=fonte3)
# define o nome do menu
barra_menu.add_cascade(label="Opções", menu=menu_opcao)

# menu manutenção
menu_manutencao = Menu(barra_menu, tearoff=0)  # retira umas linhas que fazem o menu sair fora do programa
menu_manutencao.add_command(label="Banco de dados",
                            command=ver_dados, font=fonte3)  # adicionar comando para ver os dados cadastrados
barra_menu.add_cascade(label="Manutenção", menu=menu_manutencao)

# menu "sobre"
menu_sobre = Menu(barra_menu, tearoff=0)
menu_sobre.add_command(label="projeto 1.0", font=fonte3)
barra_menu.add_cascade(label="Sobre", menu=menu_sobre)

janela.config(menu=barra_menu)

janela.mainloop()
