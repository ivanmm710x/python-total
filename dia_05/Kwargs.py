def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es: {num1}")
    print(f"El segundo valor es: {num2}")

    for arg in args:
        print(f"args: {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave}, {valor}")

prueba(15, 50, 200, 300, 400, 500, x = 'Uno', y = 'Dos', z = 'Tres')


# Otra forma de hacerlo

def prueba2(num1, num2, *args, **kwargs):

    print(f"El primer valor es: {num1}")
    print(f"El segundo valor es: {num2}")

    for arg in args:
        print(f"args: {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave}, {valor}")

# Podemos llamarlo de cualquier forma
perro = [100, 200, 300, 400]
kwargs = {'x': 'Uno', 'y': 'Dos', 'z': 'Tres'}

# Y nos va a funcionar, pero por nomenclatura habria que poner *args
prueba2(15, 50, *perro, **kwargs)
