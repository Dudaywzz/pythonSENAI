from utils import *

print("Calculadora de Ohm")
print("**********************************************")
print("MENU:")
print("0 - Sair")
print("1 - Resistencia")
print("2 - Tensão")
print("3 - Corrente")
print("4 - Resistencia necessária para um resistor")
print("**********************************************")

while True:
    try:

        calculo = input("qual calculo você quer fazer?: ")

        if calculo == "1":
            resistencia = calcular_resistencia()
            print(f"A resistencia é: {resistencia}")
        elif calculo == "2":
            tensao = calcular_tensao()
            print(f"A tensao é {tensao}")
        elif calculo == "3":
            corrente = calcular_corrente()
            print(f"A corrente é {corrente}")
        elif calculo == "4":
            resistor = calcular_resistor()
            print(f"O resistor deve ser o de {resistor} Ohm")
        elif calculo == "0":
            print("")
            print("Saindo da Calculadora de Ohm...")
            break

    except ValueError:
        print("Digite apenas numeros")

