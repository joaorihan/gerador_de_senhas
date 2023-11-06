from tkinter import *

teclas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '`', '-', '=', '[', ']', ';', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '"', '<', '>', '?']


def gerar_senha():
    import random
    try:
        tamanho = int(entry1.get())
        senha = ""
        if tamanho == "" or tamanho > 1000:
            rotulo_output.insert(0, "Erro!")   
            raise ValueError
        for i in range(tamanho):
            senha += random.choice(teclas)
        rotulo_output.insert(0, senha)
    except ValueError:
        rotulo_output.insert(0, "Erro!")
        print("Por favor, insira somente números!") 


window = Tk()
window.title("Gerador de senhas aleatório")
window.geometry("400x350+450+200")  

titulo_pag = Label(window, text="Gerador de senhas aleatório:", font="Arial 16 bold", padx=10, pady= 20)
titulo_pag.pack()

container1 = Frame(window, pady=10)
container1.pack()

rotulo1 = Label(container1, text="Digite o número de caracteres da sua senha", font="Arial 10", pady=10)
rotulo1.pack()

entry1 = Entry(container1, font=("Times New Roman", "16"), width=6)
entry1.pack()

container2 = Frame(window)
container2.pack()

rotulo2 = Label(container2, text="Output:", font="Arial 12 bold", pady=10)
rotulo2.pack()

rotulo_output = Text(container2, font="Arial 12 bold", width=32, height=1, wrap=WORD)
rotulo_output.pack()

container_botao = Frame(window, pady=10, padx=15)
container_botao.pack()

botao = Button(container_botao, text="Gerar", padx=8, pady=4, bg="purple", fg="white")
botao["font"] = ("Courrier New", "16")
botao["command"] = gerar_senha
botao.pack()



window.mainloop()


