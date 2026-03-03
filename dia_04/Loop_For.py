lista = ['a','b','c']

for letra in lista:
    print("Letra: " + letra)

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista = {'Ivan', 'Andrea', 'Susana', 'Raul'}

for nombre in lista:
    if nombre.startswith('I'):
        print(nombre)
    else:
        print('Nombre que no comienza con I')

numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor += numero
# Aqui nos fijamos que el print al estar al mismo nivel que el for, se imprime cuando acaba el loop
print(mi_valor)

for numero in numeros:
    mi_valor += numero
    print(mi_valor) # Aqui nos fijamos que si se va mostrando en cada vuelta que hace el loop


palabra = 'python'
for letra in palabra:
    print(letra)

# Tambien sirve de esta forma
for letra in 'python':
    print(letra)

# Tambien sirve de esta forma
for letra in [1, 2, 3]:
    print(letra)

# Tambien podemos listas, tuplas...
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

# Con diccionarios
dic = {'clave1': 'a','clave2': 'b', 'clave3': 'c'}

for a,b in dic.items():
    print(a,b)