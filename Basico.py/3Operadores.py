#Operadores aritmeticos

print(6 + 3)        #Suma
print(6 - 3)        #Resta
print(6 * 3)        #Multiplicacion
print(11 / 3)       #Division
print(9 % 3)        #Resto, te da el valor restante de una division
print(4 ** 3)       #Exponente
print(11 // 3)      #Division de flor, convierte los valores decimales o 'float' a valores enteros o 'int'

print('Hola' + 'Mundo')  #Se pueden sumar opalabras y en el monitor serie saldran pegadas
print('Hola'*6)          #Puedes decir cuantas veces quieres que se diga una palabra
print('Hola'+ str(6))    #Si especificas que 6 es un 'String' o palabra el operador imprimira el nuemro 6
print('Hola'+ '6')       #Todo lo que este entre comillas se puede considerar un string

#Booleano: Funcion que pregunta si algo es falso o verdadero.

#Operadores comparativos o 'Booleanos'

print(4 < 8)    #Pregunta si 8 es mayor a 4. Respuesta: True
print(4 > 8)    #Pregunta si 4 es mayor a 8. Respuesta: False
print(4 == 8)   #Pregunta si 4 es igual a 8. Respuesta: False
print(4 <= 8)   #Pregunta si 8 es mayor o igual a 4. Respuesta: True
print(4 >= 8)   #Pregunta si 8 es menor o igual a 4. Respuesta: False
print(4 < 8)    #Pregunta si 8 es mayor a 4. Respuesta: True
print(4 != 8)   #Pregunta si 4 es diferente de 8. Respuesta: True
print(8 != 8)   #Pregunta si 8 es diferente de 8. Respuesta: False

#Tambien se pueden comparar palabras o 'strings'

print('Hola' > 'Mundo')             #Para determinar si una palabra es mayor que otra el operador se basa en la posicion que tienen las letras en el abecedario. Respuesta: False
print(len('Hola') > len('Holas'))   #Para comparar si una palabra es mas grande que otra se utiliza 'len', asi el operador cuenta el numero de letras que tiene cada palabra. Respuesta: True
print('c' > 'b')                    #Preguntamos si 'c' es mayor que 'b'. Respuesta: True

#Operadores logicos

print(4 < 6 and 7 > 9)      #Esto es un 'and', pregunta si ambas variables son verdaderas, si ambas son verdaderas nos arrojara un 'true', si una es verdadera y la otra es falsa nos arrojara un 'false'
print(4 < 6 or 7 > 9)       #Esto es un 'or', pregunta si ambas variables son verdaderas, si una de ellas es verdadera nos arrojara un 'true'.
print(not(4 < 6))           #Esto es un 'not', si la variable es verdadera este operador hace que en lugar de arrojar un 'true', nos arroje un 'false' y viceversa.

print((not(7 != 7) and 6 > 5) and ('rozar' < 'rotar' or not(3 == 5))) #Deducir si la respuesta de este comando es 'true' o 'false'
#La respuesta de este comando es 'true'.
print(True and True) and (False or True) #Esto se transforma en dos 'true'.