import random

print("Gostaria de jogar o dado?(S/N)")
escolha = str.upper(input(""))

while escolha == "S" or "N":
    if escolha == "S":
        resultado = 10 * random.random() #random.random gera numero aleatorio entre 0 e 1(flutuante)
        if resultado <= 6:
            print(f"{resultado:.0f}")
            print("Gostaria de jogar o dado novamente?(S/N)")
            escolha = str.upper(input(""))
    else:
        print("Gostaria de jogar o dado?(S/N)")
        escolha = str.upper(input(""))
