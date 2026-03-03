texto = "Este es el texto de Ivan"

resultado = texto.upper()

#  La T se haria mayuscula T
resultado = texto[2].lower()

# SPLIT

# ['Este', 'es', 'el', 'texto', 'de', 'Ivan']
resultado = texto.split()

# ['Es', 'e es el ', 'ex', 'o de Ivan']
resultado = texto.split("t")

print(resultado)

# JOIN
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a, b, c, d])
# Aprender Python es genial

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = "-".join([a, b, c, d])
# Aprender-Python-es-genial


print(e)

# FIND
texto = "Este es el texto de Ivan"

resultado = texto.find("Ivan")

print(resultado) #  Te devulve la posición, si no lo encuentra te devuelve -1


# REMPLAZAR
texto = "Este es el texto de Ivan"

resultado = texto.replace("Ivan", "Ivancin")

print(resultado) #  Este es el texto de Ivancin
