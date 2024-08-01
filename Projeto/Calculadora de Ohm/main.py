print("Calculadora de Ohm")
print("**")
print("0 - Sair")
print("1 - Resistencia")
print("2 - Tensão")
print("3 - Corrente")
print("4 - Resistencia necessária para um resistor")
print("**")


opcao = int(input("Digite o número da escolha desejada: "))

while opcao != 0:
    if opcao == 1:
        print("Resistencia")
        print("**")
        while True:
            try:
                tensao = float(input("Digite a tensão em volts: "))
                if tensao > 0:
                    break
            except ValueError:
                print("Valor invalido, Digite um número utilizando o ponto como separador. Ex: 1.0")
        while True:
            corrente = float(input("Digite a corrente em amperes: "))
            if corrente > 0:
                break
        resistencia = tensao / corrente

        print(f"A resistencia é de {resistencia} Ω")

    elif opcao == 2:
        print("Tensão")
        print("**")

        resistencia = float(input("Digite a resistencia em ohms: "))
        corrente = float(input("Digite a corrente em amperes: "))

        tensao = resistencia * corrente

        print(f"A tensão é de {tensao} volts")

    elif opcao == 3:
        print("Corrente")
        print("**")

        tensao = float(input("Digite a tensão em volts: "))
        resistencia = float(input("Digite a resistencia em ohms: "))

        corrente = tensao / resistencia

        print(f"A corrente é de {corrente} amperes")

    elif opcao == 4:
        print("Resistencia resistor")
        print("**")
        tensao_fonte = float(input("Digite a tensao da fonte em volts: "))
        tensao_dispositivo = float(input("Digite a tensao da dispositivo em volts: "))
        corrente = float(input("Digite a corrente em ampares: "))

        resistencia_resistor = (tensao_fonte - tensao_dispositivo) / corrente

        print(f"A resistencia necessaria desse resistor é de {resistencia_resistor} Ω")
    else:
        print("opcao invalida")

    print("**")
    print("Escolha outra opcao")
    print("0 - Sair")
    print("1 - Resistencia")
    print("2 - Tensão")
    print("3 - Corrente")
    print("4 - Resistencia necessária para um resistor")
    print("**")

    opcao = int(input("Digite o número da escolha desejada: "))

