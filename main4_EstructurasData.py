# Estruscturas de datos
# Listas

#indice:   0 1 2 3 4
numeros = [1,2,3,4,5] #basico
#numero = [1,2,3,4,5, 'String', True, [1,2,3]] 
print(numeros)
print(type(numeros))

print(numeros[0])

# Modificando los indices
numeros[0] = 100
print(numeros[0])

#-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#             0         1         2      3        4       5
cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Rust', 'Rails']
primeros_cursos = cursos[0:3] #star and end
#primeros_cursos = cursos[:3] 
print(primeros_cursos)

#Obtener el ancho de la lista desde un determinado indice
primeros_cursos = cursos[1:] 
print(primeros_cursos)

#Sublistas con saltos
primeros_cursos = cursos[1:6:2] 
print(primeros_cursos)

#Que pasa si imprimo [::] = copia lista
primeros_cursos = cursos[::] 
print(primeros_cursos)

#Invertir lista
primeros_cursos = cursos[::-1] 
print(primeros_cursos)

"""
Metodos de las listas
"""
print('Metodos para las listas')
#len() => Conocer la longitud de la lista
print(len(cursos))

#Ordenar la lista
cursos.sort()
print(cursos)

#Ordenar desendente
cursos.sort(reverse=True)
print(cursos)

#anadir elementos a la lista
cursos.append('MongoDB')
print(cursos)
cursos.insert(0, 'MSQL')
print(cursos)

#Remover elementos
cursos.remove('Ruby')
print(cursos)

#=-=-=-=-=-=-=-=-= Tuplas -=-=-=-=-=-=-=-=-=-=-
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-Tuplas=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

configuracion = (27019, True, 'Localhost')
print(configuracion)

#Acceder a los indices
print(configuracion[0])

# =-==-=-=-=-=-=-=-=-Diccionarios
print('==-=-=-=-=-=-=-=-=-=-=-Diccionario=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
"""
    Objetos inmutables
        - String
        - Enteros
        - Flotantes
        - Bool
        - Tuplas
"""

usuario = { 
    'nombre' : 'Javi',
    'edad'   : 27,
    (1,2,3)  : 'Esta es una Tupla',
    10       : 'Entero',
    3.14     : 'Float'
    }
print(usuario)
"""
    Metodos de los Diccionarios
"""
print('Metodos para los Diccionarios')

#Imprimir las llaves
print(usuario.keys())
#Convertir a lista
print(list(usuario.keys()))
#Convertir a Tupla
print(tuple(usuario.keys()))

#Obtener los valores
print(tuple(usuario.values()))

#Obtener llave y valor
print(tuple(usuario.items()))