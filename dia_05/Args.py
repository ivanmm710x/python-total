# Si a la hora de llamar una función queremos ponerle datos indefinidos utilizamos *args
# args es una nomenclatura tradicional, podriamos poner *gato, pero por legibilidad
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(1,2,3,4,5,6))

# El código pero más facil
def suma(*args):
    return sum(args)


