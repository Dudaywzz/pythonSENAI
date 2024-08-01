import datetime
#alimentar variavel com o tempo "agora"
tempo = datetime.datetime.now()

mes = tempo.month
ano = tempo.year
dia = tempo.day
hora = tempo.hour
minuto = tempo.minute
segundo = tempo.second
data = ""
semana = ""

if mes == 1:
    data = 'Janeiro'
elif mes == 2:
    data = 'Fevereiro'
elif mes == 3:
    data == 'Março'
elif mes == 4:
    data = 'Abril'
elif mes == 5:
    data = 'Maio'
elif mes == 6:
    data = 'Junho'
elif mes == 7:
    data = 'Julho'
elif mes == 8:
    data = 'Agosto'
elif mes == 9:
    data = 'Setembro'
elif mes == 10:
    data = 'Outubro'
elif mes == 11:
    data = 'Novembro'
elif mes == 12:
    data = 'Dezembro'
else:
    print("erro")

if dia == 1:
    semana = "Segunda-Feira"
elif dia == 2:
    semana = "Terça-Feira"
elif dia == 3:
    semana = "Quarta-Feira"
elif dia == 4:
    semana = "Quinta-Feira"
elif dia == 5:
    semana = "Sexta-Feira"
elif dia == 6:
    semana = "Sabádo"
elif dia == 7:
    semana = "Domingo"



if hora < 12:
    saudação = ("bom dia usuário")
elif hora >= 12 and hora < 18:
    saudação = ("boa tarde usuário")
else:
    comprimento = ("boa noite usuário")

print(f"{saudação} hoje é dia {dia} {semana} do mes {mes} {data} do ano de {ano}, agora são {hora}:{minuto}:{segundo} horas")


