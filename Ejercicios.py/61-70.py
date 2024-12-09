#Ejercicio 61: Crea una funcion para sumar dos numeros

def sumar(numero1,numero2):
    return numero1 + numero2
print(sumar(50,102))

#Ejercicio 62: Crea una funcion para calcular el area de un circulo

import math
def areaCirculo(radio):
    return math.pi * radio**2
resultado = areaCirculo(5)
print(resultado)

#Extra

import math
radio1 = float(input('Ingrese un radio'))
def areaCirculo1(radio1):
    return math.pi * radio1 ** 2

area = areaCirculo1(radio1)
print(area)

#Ejercicio 63: Escribe una funcion para imprimir un mensaje de salido

def saludar(nombre):
    print('Bienvenido', nombre)
    
saludar('Axelin')

#Extra

nombre = (input('Ingrese un nombre'))
def saludar(nombre):
    print('Bienvenido', nombre)
    
saludar(nombre)
def saludar(nombre):
    print('Bienvenido', nombre)

#Ejercicio 64: Escribe una funcion para verificar si un numero es par o impar

def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
resultado = esPar(7)

print(resultado)

#Extra
numero = int(input('Ingrese un numero'))
def esPar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
resultado = esPar(numero)

print(resultado)

#Ejercicio 65: Escribe una funcion para escribir grados celsius a fahrenheit

def celsiusAFahrenheit(gradosC):
    return (gradosC*9/5) + 32

resultado = celsiusAFahrenheit(30)

print(resultado)

#Extra

gradosC1 = float(input('Ingrese temperatura en grados celsius'))

def CelsiusAFarenjeit(gradosC1):
    return (gradosC1*9/5) + 32
temperatura = CelsiusAFarenjeit(gradosC1)
print(f'La temperatura en grados Fahrenheit es de {temperatura}')

#Ejercicio 66: Escribe una funcion para calcular el promedio de una lista de numeros

def promedio(lista):
    return sum(lista) / len(lista)

resultado = promedio([1,2,3,4,5,6,7,8,9,10])    

print(resultado)

#Ejercicio 67: Escribe una funcion para calcular el volumen de un cilindro

import math

def Volumen(radio, altura):
    return math.pi*radio**2 * altura

resultado = Volumen(3,5)
print(resultado)

#Ejercicio 68: Escribe una funcion que pida por teclado la distancia y la velocidad para poder calcular el tiempo del viaje

Distancia = float(input('Ingrese la distancia en metros'))
Velocidad = float(input('Ingrese la velocidad en metros por segundo'))

def tiempoDeViaje():
    return Distancia/Velocidad

resultado = tiempoDeViaje()

print(f'el tiempo que dura tu viaje es de {resultado} segundos')

#Ejercicio 69: Escribe una funcion para calucular la tasa de desempleo

def tasaDeDesempleo(noEmpleados, siEmpleados):
    return (noEmpleados/siEmpleados) * 100

resultado = tasaDeDesempleo(500000, 20000)

print(resultado)

#Ejercicio 70: Escribe una funcion para claificar si una sustancia es acida, basica, o neutra a partir de su pH

def Alcalinidad(pH):
    if pH < 7:
        return 'Acida'
    elif pH > 7:
        return 'Basica'
    else:
        return 'Neutra'
resultado = Alcalinidad(7)
print(resultado)