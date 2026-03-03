def comprobar_3_cifras(lista):

    for n in lista:
        if n in range(100,1000):
            return True  # Por mucho que queden elementos en la lista, en cuanto encuentre un numero de 3 cifras se acabo devulve true. El return corta
        else:
            pass # Para que pase y siga el ciclo

resultado = comprobar_3_cifras([55, 99, 999])
print(resultado)
# Nos va a devolver siempre dos valores: True o none



# Y si queremos devolver un false
# Lo primero que pensamos es en esto verdad, pero es erroneo, porque con el primer numero de la lista con el return va a cortar por mucho que despues tengamos uno de 3 cifras
def comprobar_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            return False

resultado = comprobar_3_cifras([55, 99, 999])
print(resultado)


 # Por lo tanto hacemos esto

def comprobar_3_cifras(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False  # Al hacer tres pasadas por la lista y ver que no hay ningun numero de 3 cifras, viene aqui y corta devolviendo el false

resultado = comprobar_3_cifras([55, 99, 999])
print(resultado)

# Y si queremos almacenar todos los numeros que tengan 3 cifras...
def comprobar_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
