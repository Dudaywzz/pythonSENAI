def menu_temperatura():
    print("Menu de temperatura")
    print("1- Fahrenheit")
    print("2- Kelvin")

def solicita_celsius():

    graus_celsius = float(input("Digite o valor de graus Celsius: "))
    return graus_celsius

def solicite_entrada():
    entrada = float(input("Digite o valor de entrada, EX: 1 ou 2: "))
    return entrada

def entrada_menu(entrada,graus_celsius):

    if entrada == 1:
        entrada = graus_celsius * 1.8 + 32

    else:
        entrada = graus_celsius + 273.15

    return entrada

def exibir_mensagem():
    print(solicite_entrada(), "em Fahrenheit e", solicita_celsius(), "em Kelvin")

menu_temperatura()
exibir_mensagem()

