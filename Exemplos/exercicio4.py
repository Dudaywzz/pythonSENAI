def coloque_primeiro_lado():
    while True:
        try:
            lado1 = int(input('Digite o valor do primeiro lado: '))
            return lado1
        except ValueError:
            print('Tente novamente e digite um valor valido, Ex: 1,2,3,4')

def coloque_segundo_lado():
    while True:
        try:
            lado2 = int(input('Digite o valor do segundo lado: '))
            return lado2
        except ValueError:
            print('Tente novamente e digite um valor valido, Ex: 1,2,3,4')

def coloque_terceiro_lado():
    while True:
        try:
            lado3 = int(input('Digite o valor do terceiro lado: '))
            return lado3
        except ValueError:
            print('Tente novamente e digite um valor valido, Ex: 1,2,3,4')

def verificar_lados(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "Equilatero"
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        return "Escaleno"
    else:
        return "Isosceles"

lado1 = coloque_primeiro_lado()
lado2 = coloque_segundo_lado()
lado3 = coloque_terceiro_lado()
resultado = verificar_lados(lado1, lado2, lado3)
print("o resultado do triangulo é {}".format(resultado))