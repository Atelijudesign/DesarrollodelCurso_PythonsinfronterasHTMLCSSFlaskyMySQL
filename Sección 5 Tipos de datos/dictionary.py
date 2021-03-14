#dictionary
diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

print(diccionario)
print(diccionario['nombre'])
print(diccionario['raza'])
print(diccionario.get('nombre'))
diccionario['nombre'] = 'Fluffy'

# print(len(diccionario))

diccionario['ronronea'] = 'Si'

print(diccionario)
diccionario.pop('ronronea')
diccionario.popitem()
copiaGatito = diccionario.copy()
copiaGatito = dict(diccionario)
#del diccionario['ronronea']
diccionario.clear()
print(diccionario, copiaGatito)

fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}

mamba = {
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy": fluffy,
    "Mamba": mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6) #
print(perritos)

#booleans, solo puede tener 2 tipo de valores (true,false)
verdadero = True
falso = False

print(verdadero, falso)