lista = ['Hola', 'Mundo', 'Chanchito feliz']
lista2 = lista.copy()
list = ['Andres','Gallo','Parra']
lista.append('Chanchito triste')
# lista.clear()
print(lista, lista2.count(3))
print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

print(largoLista, largoLista2)

print(lista[2])

# lista.pop() # este elimina el último elemento de la lista
# lista.remove('Hola') # este elimina un elemento por su valor
list.pop
lista.reverse()
lista.sort()
tupla = ('hola', 'mundo', 'somos', 'tupla')
listaDeTupla = list(tupla) #transformar una tuple en lista para poder modificar con el metodo append
listaDeTupla.append('chanchito')
print(listaDeTupla)

rango = range(6)
print(rango)