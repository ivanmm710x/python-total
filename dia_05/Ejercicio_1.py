# Como yo lo he hecho
def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]
    mayor = max(lista)
    menor = min(lista)
    mediano = 0
    if num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
        mediano = num1
    elif num2 > num1 and num2 < num3 or num2 > num3 and num2 < num1:
        mediano = num2
    else:
        mediano = num3

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    else:
        return mediano
print(devolver_distintos(2, 4, 3))


# Como federico lo ha hecho
def devolver_distintos(a, b, c):
    suma = a + b + c
    lista = [a, b, c]

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]

