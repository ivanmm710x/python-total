mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2

mi_lista3[0] = "alfa"

mi_lista3.append("g")
mi_lista3.pop() #  Eliminar el ultimo de los elementos
mi_lista3.pop(0) #  Eliminar el primero de los elementos

#  Mostrar el elemento eliminado
eliminado = mi_lista3.pop(0)
print(eliminado)

print(mi_lista3)


resultado = len(mi_lista)


lista = ['g', 'o', 'i', 'm', 'b']
lista.sort() # Ordenar
lista.reverse() # Al reves

print(lista)