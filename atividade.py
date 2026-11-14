import random

while True:
    nomes = []

    while True:
        nome = input("Nome do comprador (Enter para encerrar): ")
        if nome == "":
            break
        nomes.append(nome)

    if len(nomes) > 0:
        print("O ganhador é:", random.choice(nomes))
    else:
        print("Nenhuma rifa vendida.")

    de_novo = input("Fazer outro sorteio? (sim/não): ")
    if de_novo != "sim":
        break
