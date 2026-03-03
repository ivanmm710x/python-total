def indefinida(*args):
    resultado = False
    numero_anterior = 500
    lista = list(args)
    for arg in lista:
        if arg == 0 and numero_anterior == 0:
            resultado = True
        numero_anterior = arg

    return resultado


print(indefinida(1, 2, 0, 0, 5, 6))

# Como lo ha hecho Federico

def ceros_vecinos(*args):
    contador = 0

    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False
print(ceros_vecinos(1, 2, 3, 4, 5, 6))