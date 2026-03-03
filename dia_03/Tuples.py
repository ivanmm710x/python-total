# Las tuplas no permiten asignación
mi_tuple = (1, 2, 3, 4)
mi_tuple[0] = 5

print(mi_tuple[0])

#Se pueden visualizar
mi_tuple = (1, 2, (10, 20), 4)

print(mi_tuple[2][0])

# Al tener la misma cantidad se pueden asignar los valores
t = (1,2,3)
x, y, z = t
print(x, y, z)

# Count Me cuenta cuantas veces sale el 1
t = (1,2,3,1)
print(t.count(1))

#index En que posición se situa el 2
t = (1,2,3,1)
print(t.index(2))