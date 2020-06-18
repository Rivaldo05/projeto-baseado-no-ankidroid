from tkinter import *
from adicionar_frases import *


def nova_frase():
	add()


janela = Tk()
janela.geometry("400x300")
janela.title("Projeto_anki")
janela.configure(bg="gray")

# criando menu
barra_menu = Menu(janela)  # menu ligado a janela

# para cada menu que for feito tem que repetir o mesmo processo
menu_opcao = Menu(barra_menu, tearoff=0)  # retira umas linhas que fazem o menu sair fora do programa
menu_opcao.add_command(label="Adicionar", command=nova_frase)
menu_opcao.add_command(label="Pesquisar", command="")  # adicionar comando para pesquisar uma frase especifica
menu_opcao.add_separator()  # adiciona uma linha separando os contatos
menu_opcao.add_command(label="Fechar", command=janela.quit)
# define o nome do menu
barra_menu.add_cascade(label="Opções", menu=menu_opcao)

# menu manutenção
menu_manutencao = Menu(barra_menu, tearoff=0)  # retira umas linhas que fazem o menu sair fora do programa
menu_manutencao.add_command(label="Banco de dados", command="")  # adicionar comando para ´ver os dados cadastrados
barra_menu.add_cascade(label="Manutenção", menu=menu_manutencao)

# menu "sobre"
menu_sobre = Menu(barra_menu, tearoff=0)
menu_sobre.add_command(label="projeto 1.0", command="")
barra_menu.add_cascade(label="Sobre", menu=menu_sobre)


janela.config(menu=barra_menu)

janela.mainloop()
