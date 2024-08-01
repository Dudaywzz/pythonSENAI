nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

resultado_media = ((nota1 + nota2) /2)

print("o resultado da média é",resultado_media)

if resultado_media >= 70:
    print("o aluno foi aprovado")

elif resultado_media < 70:
    print("o aluno foi reprovado")

else:
    print("nota não identificada")

