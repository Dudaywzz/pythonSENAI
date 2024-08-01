#repetição
while True:
    #comando de exibição dos códigos
    try:
        renda =float(input("Qual o valor da sua renda: "))
        #para a repeticão
        break
    except ValueError:
        print("valor invalido")

if renda <= 56072.00:
    print("desconto de 0%")
elif renda >= 56072.01 and renda <= 238532.0:
    desconto = (7.50 / 100) * renda
    print(f"o seu desconto é de {desconto}")
elif renda >= 238532.01 and renda <= 522400.0:
    desconto = (15 / 100) * renda
    print(f"o seu desconto é de {desconto}")
elif renda >= 522400.01 and renda <= 987600.0:
    desconto = (22.50 / 100) * renda
    print(f"o seu desconto é de {desconto}")
elif renda >= 987600.01:
    desconto = (27.50 / 100) * renda
    print(f"o seu desconto é de {desconto}")




