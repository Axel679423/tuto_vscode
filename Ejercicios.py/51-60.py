#Ejercicio 51: Imprimir los numeros del 1 al 5 con for

for i in range(1,6):
    print(i)
    
#Ejercicio 52:  Sumar los numeros del 1 al 10 con for

suma = 0
for i in range(1,11):
    suma = suma + i
print('La suma es:', suma)

#Ejercicio 53: Imprimir los elementos de una lista dada

lista = [10,20,30,40,50]

for elemento in lista:
    print(elemento)

#Ejercicio 54: Imprimir los caracteres de una cadena utilizando el ciclo for

cadena = 'Buenas chavales'
for caracter in cadena:
    print(caracter)

#Ejercicio 55: Imprimir los numeros pares del 2 al 10 con el ciclo for

for i in range (2,11,2):
    print(i)
    
#Ejercicio 56: Listar 10 numeros y calcular el cuadrado de cada uno e imprimirlos utilizando for

for i in range(1,11):
    cuadrado = i**2
    print(f'El cuadrado de {i} es {cuadrado}')
    
#Ejercicio 57: Imprimir los numeros del 5 al uno en orden descendente
for i in range (5,0,-1):
    print(i)
    
#Ejercicio 58: Multiplicar todos los elementos de una lista por 2

lista1 = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista1)):
    print(lista1[i]*2)
    
#Ejercicio 59: Pedir al usuario un numero e imprimir la tabla de multiplicar del mismo

numero = int(input('Ingrese un numero'))
for i in range(1,11):
    resultado = numero * i
    print(f'{numero} por {i} es igual a {resultado}')
    
#Ejercicio 60: Imprimir la suma de los numeros pares del 1 al 10 utilizando el ciclo for

sumaPares = 0
for i in range(1,11):
    if i % 2 == 0:
        sumaPares = sumaPares + i

print('La suma de pares es: ', sumaPares)