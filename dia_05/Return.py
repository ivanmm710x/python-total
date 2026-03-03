# Return devuelve un valor almacenado para utilizarlo en futuras instrucciones
# Metodo 1
def multiplicar(numero1,numero2):
    return numero1*numero2

resultado = multiplicar(10,20)
print(resultado)

# Metodo 2
def multiplicar(numero1,numero2):
    total = numero1*numero2
    print(total) # No es comun, pero nos sirve para ver que hace
    return total
multiplicar(10,20)

