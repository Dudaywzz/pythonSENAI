#serve para o computador gerar um número aleatório inteiro
from random import randint
v = 0
while True:
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer Par ou Impar? [P/I]: ')).upper().strip()[0]
    jogador = int(input("Digite um número: "))
    computador = randint(0,10)
    total = jogador + computador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print("")
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
        #par:
    if tipo == 'P':
        if total % 2 == 0:
         print('Você VENCEU!')
         v += 1
        else:
           print('Você PERDEU!')
        break
        #impar:
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break


    print('Vamos jogar novamente!')
    print(f'GAME OVER! Você venceu {v} vezes.')



