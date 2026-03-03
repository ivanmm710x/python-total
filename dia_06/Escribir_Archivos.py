# Aunque viene por defecto
archivo = open('prueba.txt','r')

# Remplaza el contenido del texto por Soy el nuevo texto
archivo = open('prueba.txt','w')

archivo.write('Soy el nuevo texto')


# Crea un nuevo .txt
archivo = open('prueba1.txt','w')

archivo.write('Soy el nuevo texto')

# Con saltos de linea
archivo = open('prueba1.txt','w')

archivo.write('''Hola
mundo
aqui
estoy''')


# Abre el archivo, se situa al final y empieza a escribir
archivo = open('prueba1.txt','a')

archivo.write('Bienvenido')

archivo.close()
