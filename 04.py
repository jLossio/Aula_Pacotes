while True:
    try: 
        numero = int(input('Entre com um valor inteiro: '))
        print(5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print("Valor errado ou não é possível dividir por 0")
    except:
        print("Desculpe, algo deu errado...")