while True:
    try:
        dia = int(input("Digite um numero de 1 a 7: "))
        data = "hoje é"

        if dia == 1:
            print(data,"Segunda-Feira")
        elif dia == 2:
            print(data,"Terça-Feira")
        elif dia == 3:
            print(data,"Quarta-Feira")
        elif dia == 4:
            print(data,"Quinta-Feira")
        elif dia == 5:
            print(data,"Sexta-Feira")
        elif dia == 6:
            print(data,"Sabádo")
        elif dia == 7:
            print(data,"Domingo")
        break

    except ValueError:
        print("Digite apenas numeros")