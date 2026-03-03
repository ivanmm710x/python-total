def contar_primos(num):
    i = 0
    for n in range(3, num):
        if num % n == 0:
            print(n)
            i += 1
    print(f'La cantidad de numeros primos que hay es de: {i}')
contar_primos(150)

# Como lo ha hecho Federico
def contar_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
            else:
                primos.append(iteracion)
                iteracion += 2
    print(primos)
    return len(primos)

