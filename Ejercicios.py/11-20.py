#Ejercicio 11: Calcula el area de un rectangulo pide base y altura al usuario
base = int(input('Ingresa base'))
altura = int(input('Ingresa altura'))
area = base * altura
print('El area del rectangulo es', area)

#Ejercicio 12: Convierte un numero entero en cadena

numero = 40
print(type(numero))
cadena = str(numero)
print(type(cadena))

#Ejercicio 13: Reemplaza un caracter en una cadena

cadena = 'pene'
nueva_cadena = cadena.replace('e', 'no')
print('La nueva cadena es', nueva_cadena)

#Ejercicio 14: Pasa una cadena de mayusculas a minusculas
mayus = 'HOLAAAA'
minus = mayus.lower()

print('Minusculas', minus)

#Ejercicio 15: Ordena una lista de numeros de menor a mayor

lista = [3,5,8,6,4,2,7,0,9]
lista.sort()
print('La lista ordenada es', lista)

#Ejercicio 16: Calcula 2 elevado a la cuarta potencia sin utilizar el operador **

resultado = pow(2, 4)
print('El resultado es', resultado)

#Ejercicio 17: Extrae una subcadena de una cadena dada
cadena1 = 'Hola'
subcadena = cadena1[2:4]
print('La subcadena es', subcadena)

#Ejercicio 18: Convierte un numero decimal a un numero entero

decimal = 4.5
entero = int(decimal)
print('El numero entero es', entero)

#Ejercicio 19: Cuenta las ocurrencias de un caracter especifico en una cadena

cadena2 = 'sexo'
ocurrencias = cadena2.count('e')

print('Las ocurrencias son', ocurrencias)

#Ejercicio 20: Encuentra y muestra el ultimo caracter de una cadena

cadena3 = 'Hola buenas tardes'
ultimoCaracter = cadena3[-1]

print('El ultimo caracter de la cadena es', ultimoCaracter)
