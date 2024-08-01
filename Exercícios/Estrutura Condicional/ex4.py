while True:
   try:
      numero1 = int(input("Digite o primeiro numero: "))
      numero2 = int(input("Digite o segundo numero: "))

      if numero1 > numero2:
         print("o numero ", numero1, "é maior que o numero ", numero2)

      else:
         print("o numero", numero2,"menor que o numero ", numero1)
         break
   except ValueError:
      print("digite apenas numeros")