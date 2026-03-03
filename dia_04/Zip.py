# Combinar listas, se pueden las que sean pero que coincida
nombre = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Madrid', 'Barcelona', 'Valencia']

# Importante castearlo para que podamos visualizarlo bien
combinados = list(zip(nombre, edades, ciudades))

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")