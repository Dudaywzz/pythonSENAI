while True:
    try:
        ano = int(input("Digite seu ano de nascimento: "))
        idade = 2024 - ano

        if idade > 18:
            final = "adulto"
        elif idade == 18:
            final = "maior de idade"
        elif idade < 0:
            final = "idade invalida"

        elif ano > 2024:
            final = "ano invalido, coloque novamente"

        else:
            idade < 18
            final = "menor de idade"

        print("você tem", idade, "anos,", final)
        break
    except ValueError:
        print("Digite apenas numeros. ex: 1,2,3")