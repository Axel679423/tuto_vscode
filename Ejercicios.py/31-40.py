#Ejercicio 31: Pide un numero y verifica si es positivo o negativo o 0

numero = int(input('Escribe un numero'))

if numero > 0:
    print('Positivo')
elif numero < 0:
    print('Negativo')
else:
    print('cero')
    
#Ejercicio 32: Pide un numero y comprueba si es par o impar utilizando if y modulo.

numero1 = int(input('Ingresa un numero'))
if numero1% 2 == 0:
    print('Es un numero par')
else:
    print('Es un numero impar')
    
#Ejercicio 33: Determina si un año es bisiesto
#Regla de negocio: Es divisible por 4, no es divisible por 100 y es divisible por 400

año = 2024
if(año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print('El año es bisiesto')
else:
    print('No es un año bisiesto')

#Extra

año1 = int(input('Ingresa un año'))
if(año1 % 4 == 0 and año1 % 100 != 0) or (año1 % 400 == 0):
    print('El año es bisiesto')
else:
    print('El año no es bisiesto')
    
#Ejercicio 34: Verifica si una cadena es mayor o igual a 10 caracteres

cadena = 'Buenas tardeeeees'
if len(cadena) >= 10:
    print('La cadena tiene 10 o mas caracteres')
else:
    print('La cadena tiene menos de 10 caracteres')
    
#Extra

cadena1 = (input('Ingresa un texto'))
if len(cadena1) >= 10:
    print('La cadena tiene 10 caracteres o más')
else:
    print('La cadena tiene menos de 10 carateres')

#Ejercicio 35:Compreuba si un numero esta en el rango de 1 y 100
numero2 = int(input('Ingrea un numero'))

if 1 <= numero2 <= 100:
    print('Esta en el rango de 1 al 100')
else: 
    print('No esta en el rango')
    
#Ejercicio 36:Pide un caracter y determina si es una vocal

caracter = input('Ingresa un caracter')
vocales = ['a', 'e', 'i', 'o', 'u']

if caracter.lower() in vocales:
    print('La letra es una vocal')
else:
    print('No es una vocal')

#Ejercicio 37: Calcula el maximo de 3 numeros

numero3 = 4 
numero4 = 5
numero5 = 10

maximo = max(numero3, numero4, numero5)
print('El numero maximo es:', maximo)

#Extra

numero6 = int(input('Ingrese un numero'))
numero7 = int(input('ingrese un numero'))
numero8 = int(input('ingrese un numero'))

maximo1 = max(numero6, numero7, numero8)
print('El numero maximo es', maximo1)

#Ejercicio 38: Determina si un numero es divisible entre 5 y 7

numero9 = int(input('Ingrese un numero'))
if numero9 % 5 == 0 and numero9 % 7 == 0:
    print('El numero es divisible entre 5 y 7')
else:
    print('El numero no es divisible entre 5 y 7')
    
#Ejercicio 39:Verifica si la palabra ingresada es Python

palabra = input('Ingresa palabra')

if palabra.lower() == 'python':
    print('La palabra es python')
else:
    print('La palabra no es python')
    
 #Ejercicio 40: Calcular el IMC e interpretarlo
    
peso = int(input('Ingrese su peso en kilogramos: '))
altura = float(input('Ingrese su altura en metros: '))
imc = peso / (altura ** 2)
print (imc)

if imc < 18.5:
    print('Bajo peso')
elif imc < 25:
    print('Peso normal')
elif imc <30:
    print('Sobrepeso')
elif imc <35:
    print('Obesidad grado 1')
elif imc <40:
    print('Obesidad grado 2')
else: 
    print('Obesidad grado 3')