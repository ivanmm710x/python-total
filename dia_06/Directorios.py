import os

# Obtener la ruta de trabajo actual
ruta = os.getcwd()

print(ruta)

# Obtener otra ruta de trabajo
ruta = os.chdir('C:\\Users\\ivan7\\Desktop\\Cursos\\Python_Total\\dia_06')

archivo = open('alternativo.txt', 'r')
print(archivo.read())

# Crear directorios
ruta = os.makedirs('C:\\Users\\ivan7\\Desktop\\Cursos\\Python_Total\\dia_06\\otra')

ruta = ('C:\\Users\\ivan7\\Desktop\\Cursos\\Python_Total\\dia_06\\alternativo.txt')

# El nombre de base de nuestro elemento: Nos devuelve alternativo.txt
elemento = os.path.basename(ruta)
print(elemento)

# La primera parte de nuesto directorio
elemento = os.path.dirname(ruta)
print(elemento)

from pathlib import Path

# Nos sirve para abrir otras carpetas ya sea windows o Mac
carpeta = Path('C:/Users/ivan7/Desktop/Cursos/Python_Total/dia_06')
archivo = carpeta / 'alternativo.txt'

mi_archivo = open(archivo)
print(mi_archivo.read())

# Otra forma
carpeta = Path('C:/Users/ivan7/Desktop/Cursos/Python_Total/dia_06') / 'alternativo.txt'
mi_archivo = open(carpeta)
print(mi_archivo.read())

# Lo primero y la base
elemento = os.path.split(ruta)
print(elemento)

# Borrar carpetas
os.rmdir('C:\\Users\\ivan7\\Desktop\\Cursos\\Python_Total\\dia_06\\otra')