while True:
    try:
        mes = int(input("Digite um numero de 1 a 12: "))
        data = "Estamos no mês de"

        if mes == 1:
            print(data, "Janeiro")
        elif mes == 2:
            print(data, "Fevereiro")
        elif mes == 3:
            print(data, "Março")
        elif mes == 4:
            print(data, "Abril")
        elif mes == 5:
            print(data, "Maio")
        elif mes == 6:
            print(data, "Junho")
        elif mes == 7:
            print(data, "Julho")
        elif mes == 8:
            print(data, "Agosto")
        elif mes == 9:
            print(data, "Setembro")
        elif mes == 10:
            print(data, "Outubro")
        elif mes == 11:
            print(data, "Novembro")
        elif mes == 12:
            print(data, "Dezembro")
        else:
            print("mês invalido. Digite novamente: ")

    except ValueError:
        print("Digite um numero inteiro valido")