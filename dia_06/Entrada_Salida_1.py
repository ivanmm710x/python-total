# Lo que hacemos es asignar y abrir en memoria el contenido de prueba.txt a mi archivo
mi_archivo = open('prueba.txt')

# Leer el archivo
print(mi_archivo.read())

# Leer la primera linea del archivo
una_linea = mi_archivo.readline()
print(una_linea)
# O tambien podemos
print(mi_archivo.readline())

# Si volvemos a invocarlo, nos leera la segunda linea y con rstrip añadira un espacio
print(una_linea.rstrip())


# Si volvemos a invocarlo, nos leera la tercera linea y con mayuscula
print(una_linea.upper())

# Con for
for l in mi_archivo:
    print("Aqui dice: " + l)

# En formato lista
todas = mi_archivo.readlines()
print(todas)

todas = todas.pop()


# Cerrar y siempre tenerlo al final despues del open para limpiar memoria
mi_archivo.close()