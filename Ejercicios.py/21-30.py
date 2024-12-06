#Ejercicio 21: Multiplica una cadena por un numero entero

cadena = 'Malas tardes'
Mult = cadena*5

print('La cadena multiplicada es', Mult)

#Ejercicio 22:Divide una cadena en una lista de subcadenas

cadena1 = 'Bla bla bla bla bla'
division = cadena1.split()

print('La cadena dividida es', division)

#Ejercicio 23: Verifica si una palabra es un palindromo

palabra = 'aibofobia'
esPalindromo = palabra == palabra[::-1]

print('Es palindromo', esPalindromo)

#Ejercicio 24: Elimina un elemento especifico de una lista

lista = [1.5, 10, 'Hola', True]
lista.remove('Hola')

print('Resultado', lista)

#Ejercicio 25:Genera una lista de numeros del 1 al 200

numeros = list(range(1,201))

print (numeros)

#Ejercicio 26:Intercambia los valores de dos variables con asignacion multiple

a = 8
b = 9

a,b = b, a
print(a,b)

#Ejercicio 27: Realiza operaciones basicas con conjuntos union e interseccion

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}
union = conjunto1 | conjunto2
interseccion = conjunto1 & conjunto2

print('La union es', union)
print('La interseccion es', interseccion)

#Ejercicio 28: Extrae un elemento especifico de una tupla

tupla = ('si', 106, True)
elemento = tupla[2]

print('El elemento es', elemento)

#Ejercicio 29: Combina dos listas en pares usando la funcion zip()
lista1 = [1,2,3]
lista2 = ['a','b','c']
pares = list(zip(lista1,lista2))

print('La lista combinada es', pares)

#Ejercicio 30: Elimina duplicados de una lista

lista3 = [1,2,3,4,4,5,5,6]

sinDuplicados = list(set(lista3))

print('La lista sin duplicados es', sinDuplicados)