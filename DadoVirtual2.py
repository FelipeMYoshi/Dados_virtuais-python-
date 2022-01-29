import random

print("Gostaria de jogar o dado?(S/N)")
escolha = str.upper(input(""))

while escolha == "S" or "N":
    if escolha == "S":
        print(random.choice([1, 2, 3, 4, 5, 6])) #random.choice escolhe numero aleatorio da lista declarada.
        print("Deseja jogar novamente?(S/N)")
        escolha = str.upper(input(""))
    else:
        if escolha == "N":
            print("FIM!")
            break
        else:
            print("Digite apenas S ou N!")
            escolha = str.upper(input(""))
