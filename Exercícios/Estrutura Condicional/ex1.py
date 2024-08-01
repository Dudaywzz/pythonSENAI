while True:
    try:
        print("Digite um número para saber se é positivo ou negativo")

        numero = int(input("digite um numero:"))

        if numero > 0:
            print("o numero é positivo")

        else:
            print("o numero é negativo")
        break
    except ValueError:
        print("Digite apenas nuemros")