from datetime import datetime

hora = datetime.now().hour

nome = input("qual seu nome?")
def ola_nome(nome):
    print("Olá", nome)

def define_saudacao(hora_atual):

    if hora >= 0 and hora < 5:
        saudacao = "boa madrugada"

    elif hora >= 5 and hora < 12:
        saudacao = "bom dia"

    elif hora >= 12 and hora < 19:
        saudacao = "boa tarde"

    elif hora >= 19 and hora < 24:
        saudacao = "boa noite"

    return saudacao

ola_nome(nome)
print("agora são:", hora, "horas")




