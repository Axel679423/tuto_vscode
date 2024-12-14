#Ejercicio 41:Imprime los numeros del 10 al 1 en orden descendente

contador = 10
while contador > 0:
    print(contador)
    contador -=1;
    
#Ejercicio 42: Solicita al usuario ingrear un numero N y luego imprime la suma de todos los numeros desde 1 hasta N

numero = int(input('Ingrese un numero'))
suma = 0
i = 1
while i <= numero: 
    suma += i
    i +=1
print('La suma es', suma);

#Ejercicio 43:Solicite al usuario ingresar un numero N e imprime el factorial de ese numero

numero1 = int(input('Ingrese un numero'))
factorial = 1
i = 1
while i <= numero1:
    factorial = factorial * i
    i = i + 1
print('El factorial es', factorial)

#Ejercicio 44:Genera un numero aleatoreo entre 1 y 10 y luego pide al usuario que lo adivine hasta que lo haga correctamente

import random 
numeroSecreto = random.randint(1,10)
intentos = 0

while True:
    intento = int(input('Adivina el numero'))
    intentos = intentos + 1
    if intento == numeroSecreto:
        print(f'Adivinaste el numero, te tomo {intentos} intentos :D')
        break
    
#Ejercicio 45:Imprime la tabla de  multiplicar del numero ingresado por el usuario

numero2 = int(input('Ingrese un numero'))
i = 1
while i <= 10:
    print(f'{numero2} x {i} = {numero2 * i}')
    i = i + 1
    
#Ejercicio 46: Solicita al usuario ingresar un numero y cuenta cuantos digitos tiene

numero3 = int(input('Ingrese un numero'))
contador1 = 0
while numero3 != 0:
    numero3 = numero3 // 10
    contador1 = contador1 + 1
print('Los digitos son', contador1)

#Ejercicio 47:Hacer un menu de opciones que incluya la opcion de salir del programa

while True:
    print('1 - Suma')
    print('2 - Restar')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Salir')
    
    opcion = int(input('Escribe tu opcion'))
    
    if opcion == 1:
        print('Usted esta sumando')
    elif opcion == 2:
        print('Usted esta restando')
    elif opcion == 3:
        print('Usted esta multiplicando')
    elif opcion == 4:
        print('Usted esta dividiendo')
    elif opcion == 5:
        break
    else:
        print('No es una opcion valida')
print('Vuelve pronto')

#Ejercicio 48: Simula un volado con el lanzamiento de una moneda
import random

while True:
    moneda = random.randint(1,2)
    if moneda == 1:
        print('Cara')
    else:
        print('Cruz')
    jugar = input('Tirar de nuevo (S/N)')
    if jugar.lower() == 'n':
        break
print('Gracias por jugar')

#Ejercicio 49: Simular el lanzamiento de un dado hasta obtener un 6
import random

while True:
    dado = random.randint(1,6)
    if dado == 1:
        print('1')
    elif dado == 2:
        print('2')
    elif dado == 3:
        print('3')
    elif dado == 4:
        print('4')
    elif dado == 5:
        print('5')
    else:
        print('6')
    jugar = input('Tirar de nuevo (S/N)')
    if jugar.lower() == 'n':
        break
print('Gracias por jugar')

#Ejercicio 50: Mostrar los numeros del 1 al 100 pero reemplazando los multiplos de 3 por 'Fizz' y los multiplos de 5 por 'Buzz

numero4 = 1
while numero4 <= 100:
    if numero4 % 3 == 0 and numero4 % 5 == 0:
        print('FizzBuzz')
    elif numero4 % 3 == 0:
        print('Fizz')
    elif numero4 % 5 == 0:
        print('Buzz')
    else:
        print(numero4)
    numero4 = numero4 + 1