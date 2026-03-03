menor = min(58, 96, 72, 64, 35)
mayor = max(58, 96, 72, 64, 35)

print(mayor)

lista = [58, 96, 72, 64, 35]
print(max(lista))
print(f'El menor de la lista es {min(lista)} y el mayor es {max(lista)}')

nombres = ['juan', 'pablo', 'alicia', 'carlos']
print(min(nombres))

# Me va indicar la primera letra del abecedario que salga en el nombre
nombre = 'ivan'
print(min(nombre))

# Sin embargo, con la V mayúscula, el orden va de mayusculas a luego minusculas
nombre = 'iVan'
print(min(nombre))

# Pasarlo a minusculas
nombre = 'iVan'
print(min(nombre).lower())


dic = {'C1':45, 'C2': 11}
# Nos trae el valor de los indices
print(min(dic))
# Nos trae el valor de los valores
print(min(dic.values()))