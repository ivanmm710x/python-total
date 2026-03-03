monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas monedas")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n) ")
else:
    print("Gracias")

# Pass: Generar un espacio para el programador
while respuesta == 's':
    pass

print("Hola")

# Si queremos que el programa se interrumpa cuando llegue a la V
nombre = input("Ingrese su nombre: ")

for letra in nombre:
    if letra == 'v':
        break
    print(letra)

# Similar al break lo que sucede que continua
for letra in nombre:
    if letra == 'v':
        continue
    print(letra)