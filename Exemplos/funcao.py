from datetime import datetime

def menu_calculadora():
    print("menu calculadora")
    print("1- adição")
    print("2- subtração")
    print("3- multiplicação")
    print("4- divisão")


#menu_calculadora()


#função com nome
def ola_nome(nome):
    print("Olá", nome)

#ola_nome("Madu")

#função de retornar
def calcula_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def exibir_idade(idade):
    print("a sua idade é", calcula_idade(2008), "anos")

def solicita_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            if ano_nascimento < datetime.now().year:
                return ano_nascimento
            else:
                print("Digite um ano menor que o atual")
        except ValueError:
            print("Digite somente números, ex: 2000")

solicita_ano_nascimento()


__name__=='__main__':
menu_inicial():
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()