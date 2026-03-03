from random import randint

nombre = input('Ingresa tu nombre: ')
print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

contador = 0
revancha = 's'
numero = 0
premio = randint(1,100)


while revancha == 's':
    numero = int(input("Introduce el numero: "))
    contador += 1

    if numero not in range(1,101):
        print('Numero no permitido')
    elif contador < 8 and numero < premio:
        print('Respuesta incorrecta❌. Has elegido un número menor al número secreto')
    elif contador < 8 and numero > premio:
        print('Respuesta incorrecta❌. Has elegido un número mayor al número secreto')
    elif contador < 8 and numero == premio:
        print(f'Respuesta correcta {nombre}!!✅, Enhorabuena!!, Solo te ha llevado {contador} intentos')
        break
    elif contador == 8:
        print("Has gastado todos tus intentos")
        revancha = input('S/N: ').lower()
        if revancha == 's':
            contador = 0
        else: contador += 1





