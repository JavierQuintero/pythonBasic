#Funciones
def saludar(username):
    print('Hola', username)

saludar('Javier')

#Funciones de parametros opcionales
def suma(param_uno, param_dos = 50):
    return param_uno + param_dos

resultado = suma(12)
print(resultado)

# * -> Tupla
# ** -> Diccionario

def retornarTupla(*args):
    print(args)
    print(type(args))

retornarTupla(7,8,9,10)

print('-=-=-=-=-=-=-=-=-Promedio-=-=-=-=-=-=')

def promedio(*args):
    return sum(args) / len(args)

resultadoPromedio = promedio(5,7,8,9,10)
print(resultadoPromedio)



def retornarDict(**kwargs):
    print(kwargs)
    print(type(kwargs))

retornarDict(cody='Cody', name="Javi")