# captura de informacion de parte del cliente
edad = input('Ingresa tu edad: ')
print(type(edad))

# Modificar el string apartir del entero
edad = int(edad)
print(type(edad))

#Condiciones
if edad >= 18 and edad <= 59:
    print('Eres mayor de edad":-)"')
elif edad > 80:
    print('Eres mayor de edad y eres adulto mayor":-s"')
else:
    print('No eres mayor edad')
