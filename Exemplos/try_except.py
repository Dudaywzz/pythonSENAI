# O while repete tudo que esta dentro dele
while True:
    try:
        # O try vai tentar executar esse bloco de código
        idade = int(input("Digite sua idade: "))
        # O if verifica se idade é valida
        if idade > 0 and idade <= 100:
            print("idade:", idade)
            # O break sai do while
            break
        else:
            print("idade invalida")
    except ValueError:
        # Caso der erro executa aqui
        print("Digite sua idade em numero. EX: 26")