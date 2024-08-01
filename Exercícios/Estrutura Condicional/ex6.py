while True:
    try:
        numero1 = int(input("Digite o primeiro numero: "))
        numero2 = int(input("Digite o segundo numero: "))
        numero3 = int(input("Digite o terceiro numero: "))

        if numero1 > numero2 and numero1 > numero3:
            maior = numero1

        elif numero2 > numero1 and numero2 > numero3:
            maior = numero2

        else:
            maior = numero3

        print(f"o maior numero é o {maior}")
        break
    except ValueError:
        print("Digite apenas numeros")