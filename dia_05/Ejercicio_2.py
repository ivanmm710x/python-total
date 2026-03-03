def letras(palabra):
    resultado = set()
    for letra in palabra:
        resultado.add(letra)

    resultado = list(resultado)
    resultado.sort()

    return resultado
print(letras('ivan'))


