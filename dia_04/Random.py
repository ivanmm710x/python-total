from random import *  # Importamos todo

aleatorio = randint(1,10)
print(aleatorio)

# Nº decimal aleatorio
aleatorio = uniform(1,5)
print(aleatorio)

# Nº decimal aleatorio con un decimal
aleatorio_con_un_decimal = round(uniform(1,5),1)
print(aleatorio_con_un_decimal)

# Nº aleatorio entre 0 y 1
aleatorio = random()
print(aleatorio)

# Aleatorio pero con listas
colores = ['azul', 'verde', 'rojo', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

# Cambia el orden de la lista
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
