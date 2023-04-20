while True:
    try:
        numero = int(input("Entre com um número: "))
        print(numero/2)
        break
    except:
        print("O numero que vocÇe entrou não é valido. Tente novamente")