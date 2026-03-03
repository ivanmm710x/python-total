nombre = input("Ingrese su nombre: ")
ventas = int(input("Ingrese el numero de ventas: "))
comision = round(ventas * 13 / 100, 2)

print(f"Hola {nombre}, tus comisiones de este mes son de {comision}")