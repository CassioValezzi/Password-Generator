import random
def numberConverter(frase):
    resp = input(frase)
    if resp.isnumeric():
        num = int(resp)
        return num
    else:
        print("não é um numero")
        numberConverter(frase)

characters = numberConverter("quantos caracteres\n")


alfabetoMinusculo = []
for letras in range(ord("a"),ord("z")+1):
    alfabetoMinusculo.append(chr(letras))


alfabetoMaiusculo = []
for letras in range(ord("A"),ord("Z")+1):
    alfabetoMaiusculo.append(chr(letras))


numChars = []
for num in range(0,10):
    numChars.append(num)
# print(numChars)

charactersTypes = {
    "especial characters" : ["@","#","$","%","&","*","^"],
    "alpha_min characters" : alfabetoMinusculo,
    "alpha_max characters" : alfabetoMaiusculo,
    "num characters" : numChars,
}
# print(len(charactersTypes["especial characters"]))
password = []

# print(list(charactersTypes.keys()))
for char in range(characters):
    if char % 4 == 0:
        char = 0
    if (char) % 4 == 1:
        char = 1
    if (char) % 4 == 2:
        char = 2
    if (char) % 4 == 3:
        char = 3
    # print(f"variavel char = {char}")
    keys = list(charactersTypes.keys())
    # print(keys)
    randomKey = random.randint(0, len(charactersTypes[keys[char]]) - 1)
    # print(randomKey)
    password.append(charactersTypes[keys[char]][randomKey])
    # print(password)

for i in password:
    print(i,end="")


