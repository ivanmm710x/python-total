from unittest import case


# Tenemos dos variables
cliente = {'nombre': 'Ivan',
           'edad': 20,
           'puesto': 'Programador'}

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'Keanu Reeves',
                              'director': 'Lana y Lilly Waschoswski'}}

# Añadimos una lista con los dos elementos que hemos creado mas uno que no existe
elementos = [cliente, pelicula, 'libro']

# Vamos a repasar cada uno de los elementos que hay en la lista elementos
for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad': edad,
              'puesto': puesto,}:
            print('Es un cliente')
            print(nombre, edad, puesto)
        case {'titulo': titulo,
              'ficha_tecnica': {'protagonista': protagonista,
                                'director': director}}:
            print('Es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print('No se que es esto')


