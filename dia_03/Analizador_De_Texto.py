# Pedimos el texto y lo pasamos a minúsculas
texto = input('Introduce una frase: ')
texto = texto.lower()
letras = []

letras.append(input('Introduce la primera letra: ').lower())
letras.append(input('Introduce la segunda letra: ').lower())
letras.append(input('Introduce la tercera letra: ').lower())

print("\n")
print("Cantidad de letras")
cantidad_letra1 = texto.count(letras[0])
cantidad_letra2 = texto.count(letras[1])
cantidad_letra3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida '{cantidad_letra1}' veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida '{cantidad_letra2}' veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida '{cantidad_letra3}' veces")



# 2. Cuantas palabras tiene nuestro texto
print("\n")
print("Cantidad de palabras")

palabras = texto.split()
print(f"Hemos encontrado '{len(palabras)}' palabras en el texto")


# 3. Cual es la primera y la última palabra del texto
print("\n")
print("Primera y ultima letra")
print('La primera letra del texto es: ' + texto[0])
print('La ultima letra del texto es: ' + texto[-1])

# 4. Texto invertido
print("\n")
print("Texto invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves va a decir '{texto_invertido}'")


# 5. Buscando la palabra
print("\n")
print("Buscando la palabra python")

buscar_pyhton = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_pyhton]} se encuentra en el texto")


