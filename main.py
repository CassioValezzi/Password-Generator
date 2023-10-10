import random
from tkinter import *
import pyperclip

#função que transforma numeros
def numberConverter(resp):
    if resp.isnumeric():
        num = int(resp)
        return num
    else:
        text_password["text"] = "Digite apenas numeros"


alfabetoMinusculo = []
for letras in range(ord("a"),ord("z")+1):
    alfabetoMinusculo.append(chr(letras))


alfabetoMaiusculo = []
for letras in range(ord("A"),ord("Z")+1):
    alfabetoMaiusculo.append(chr(letras))


numChars = []
for num in range(0,10):
    numChars.append(str(num))
# print(numChars)

charactersTypes = {
    "especial characters" : ["@","#","$","%","&","*","^"],
    "alpha_min characters" : alfabetoMinusculo,
    "alpha_max characters" : alfabetoMaiusculo,
    "num characters" : numChars,
}


janela = Tk()
janela.title("Password Generator")
janela.geometry("350x350")


texto_orientacao = Label(janela,text= "Quantos caracteres?(apenas numeros)")
texto_orientacao.pack(pady=20)


box_text = Entry(janela, width=5)
box_text.pack()

def gerar_senha():
    characters = numberConverter(box_text.get())

    password = []

    for char in range(characters):
            if char % 4 == 0:
                char = 0
            elif (char) % 4 == 1:
                char = 1
            elif (char) % 4 == 2:
                char = 2
            elif (char) % 4 == 3:
                char = 3

            keys = list(charactersTypes.keys())

            randomKey = random.randint(0, len(charactersTypes[keys[char]]) - 1)

            password.append(charactersTypes[keys[char]][randomKey])

    passwordString ="".join(password)

    text_password["text"] = passwordString




botao = Button(janela, text="Gerar senha",command=gerar_senha)
botao.pack(pady=20)

text_aux1 =Label(janela, text="Sua senha é:")
text_aux1.pack()

text_password =Label(janela, text="")
text_password.pack(pady=20)
def copy():
    if text_password["text"] != "" and text_password["text"] != "Digite apenas numeros":
        pyperclip.copy(text_password["text"])
    elif text_password["text"] == "Digite apenas numeros":
        text_aux1["text"] = "Gere a sua senha primeiro"
    else:
        text_aux1["text"] = "Gere a sua senha primeiro"



bottun_copy = Button(janela, text="Copiar senha",command=copy)
bottun_copy.pack()


text_aux1 = Label(janela, text="")
text_aux1.pack(pady=20)


janela.mainloop()