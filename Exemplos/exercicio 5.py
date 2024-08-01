def imc(peso, altura):
    resultado = peso / (altura * altura)
    return resultado


def peso_ideal(imc):
    if imc < 18.5:
        print("Você esta abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Você esta na faixa de peso normal")
    elif 25 <= imc < 30:
        print("Você esta em sobrepeso")
    elif 30 <= imc < 40 and imc < 65:
        print("Você esta em obesidade")


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
print("seu imc é", imc(peso, altura))


imc = imc(peso, altura)
peso_ideal(imc)

