from random import randint

print("")
print("Seja bem vindo ao jogo adivinhacao!")


def numero_aleatorio():
    aleatorio = randint(1, 100)

    print("")
    chute = int(input("Digite um valor entre 1 e 100 para iniciar o jogo: "))
    while True:

        if (chute > 100):
              print("esse número é inválido, tente um menor que 100")



        elif (aleatorio < chute):
            print("o número que você chutou é maior que o número misterioso!")


        elif (aleatorio > chute):
            print("o número que você chutou é menor que o número misterioso!")




        elif (aleatorio == chute):
            print("Parabéns voce acertou o numero misterioso")
            continuar_ou_parar = int(input("Quer continuar o jogo? \nsim = 1 \nnão = 0\n "))





            if continuar_ou_parar == 0:
                print("Fim do jogo")
                break
            if continuar_ou_parar == 1:
                print("Vamos jogar novamente!")
                aleatorio = randint(1, 100)

        chute = int(input("Digite um valor entre 1 e 100 para iniciar o jogo: "))





numero_aleatorio()

