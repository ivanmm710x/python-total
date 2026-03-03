mi_set = set([1, 2, 3, 4, 5]) # Tambien se pueden poner asi mi_set = set({1, 2, 3, 4, 5})
print(type(mi_set))
print(mi_set)

# Los sets no se pueden modificar ni acceder a ellos
print(mi_set[0])
mi_set[0] = 5

# No admite ni listas ni diccionarios, pero SI Tuplas
mi_set = ((1,2,3),(4,5,6),(7,8,9))
print(mi_set)

# Se encuentra el 2 en mi set?
mi_set = (1, 2, 3, 4, 5, 6)
print(2 in mi_set)

# Union, podemos unirlos y vemos que el 3 no se repite en la ejecucion: {1, 2, 3, 4, 5}
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

# Agregar y eliminar, pero no puedes agregar nº repetidos ni eliminar
s1 = {1, 2, 3}
s1.add(4)
s1.remove(3)

# Discard - En este caso, si no puede descartar el 5, porque no esta, seguimos adelante y asi no nos da error
s1.discard(5)

# pop Lo que nos va a hacer el pop es eliminar un numero aleatorio lo que puede ser muy interesante
s1.pop()

#Clear Limpiartelo todo
s1.clear()