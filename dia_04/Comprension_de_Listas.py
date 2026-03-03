# Manera tradicional
palabra = 'Python'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# Agregar letra por letra directamente en la lista con un for
lista = [letra for letra in palabra]
print(lista)

# Con la palabra directamente sin crear variable
lista2 = [letra for letra in 'Python']
print(lista2)

# Con rango
lista3 = [n for n in range(1,20,2)]
print(lista3)

# Ahora ese numero dividido por 2 en ese rango
lista4 = [n / 2 for n in range(1,21,2)]
print(lista4)

# Con condiciones
lista5 = [n if n * 2 > 10 else 'no' for n in range(1,20,2)]
print(lista5)

pies = [10, 20, 30, 40, 50]
# Queremos tener una lista compuesta por pies multiplicados por 3.281 por cada pie que encuentre en la lista pies
metros = [p * 3.281 for p in pies]
print(metros)


