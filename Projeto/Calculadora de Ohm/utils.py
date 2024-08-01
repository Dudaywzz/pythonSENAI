def calcular_resistencia():
    tensao = float(input("Digite o valor da tensao: "))
    corrente = float(input("Digite o valor da corrente: "))
    return tensao / corrente

def calcular_tensao():
    corrente = float(input("Digite o valor da corrente: "))
    resistencia = float(input("Digite o valor da resistencia: "))
    return corrente * resistencia

def calcular_corrente():
    tensao = float(input("Digite o valor da tensao: "))
    resistencia = float(input("Digite o valor da resistencia: "))
    return tensao / resistencia

def calcular_resistor():
    tensao_fonte = float(input("Digite o valor da tensao: "))
    tensao_dispositivo = float(input("Digite o valor do dispositivo: "))
    corrente_dispositivo = float(input("Digite o valor da corrente: "))
    return (tensao_fonte - tensao_dispositivo) / corrente_dispositivo






