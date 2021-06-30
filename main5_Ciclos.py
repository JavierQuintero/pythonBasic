#Ciclos
    #While
contador = 0
while contador <= 10:
    print(contador)
    contador += 1
else:
    print('Contador no es menor o igual que 10')

    #For
#Iterando un string
mensaje = 'Los string son objetos iterables'
for caracter in mensaje:
    print(caracter)

usuario = {
    'userName': 'Javier',
    'email': 'elkinDeveloper@gmail.com'
}
for key in usuario:
    valor = usuario[key]
    print(valor)

#Desempaquetar
print('=-=-=-=-=-=-=-Desempaquetar=-=-=-=-=-=-=-=-=-=-=--')
for llave, valor in usuario.items():
    print(llave,' - ',valor)
    