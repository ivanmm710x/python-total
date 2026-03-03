# De esta forma funciona pero no es correcta
lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice, item)
    indice = indice + 1
# --------------------------------------------
# Estas si

lista = ['a', 'b', 'c']

for item in enumerate(lista):
    print(item)
    # (0, 'a')
    # (1, 'b')
    # (2, 'c')

for indice, item in enumerate(lista):
    print(indice, item)
    # 0 a
    # 1 b
    # 2 c

for indice, item in enumerate(range(50,55)):
    print(indice, item)
    # 0 50
    # 1 51
    # 2 52
    # 3 53
    # 4 54

mis_tuples = list(enumerate(lista))
print(mis_tuples)
# [(0, 'a'), (1, 'b'), (2, 'c')]
