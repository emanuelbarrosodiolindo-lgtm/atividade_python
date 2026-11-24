palavra_secreta = "python"
palavra_atual = ["_"] * len(palavra_secreta)
erros = 0
limite_erros = 6

print("JOGO DE ADIVINHAÇÃO DE PALAVRAS\n")

while "_" in palavra_atual and erros < limite_erros:
    print("Palavra:", " ".join(palavra_atual))
    print("Erros:", erros, "/", limite_erros)

    letra = input("\nDigite uma letra: ").lower()

    if len(letra) != 1:
        print("Digite apenas uma letra!")
    elif letra in palavra_secreta:
        print("Você acertou!")

        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_atual[i] = letra
    else:
        erros += 1
        print("Letra incorreta!")

    print()

if "_" not in palavra_atual:
    print("Parabéns! Você venceu!")
else:
    print("Você perdeu!")

print("A palavra era:", palavra_secreta)
