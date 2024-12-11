animal = '   Gaxiola chistoso   '
print(animal.upper())              #Pone todo en mayusculas
print(animal.lower())              #Pone todo en minusculas
print(animal.strip().capitalize()) #Elimina los espacios en blanco y pone la primera letra en mayuscula
print(animal.title())              #Pone la primera letra de cada palabra en mayuscula
print(animal.strip())              #Elimina todos los espacios que hay antes y despues del string
print(animal.lstrip())             #Elimina todos los espacios en blanco a la izquierda del string
print(animal.rstrip())             #Elimina todos los espacios en blanco a la derecha del string
print(animal.find('xio'))          #Encuentra la posicion de las letras que queremos encontrar
print(animal.replace('xio', 'lol'))#Reemplaza los caracteres que nosotros queramos
print('xio' in animal)             #Sirve para saber si un caracter o una cadena de caracteres se encuetnra dentro de una variable
print('xio' not in animal)         #Sirve para saber si un caracter o una cadena de carateres se encuentra dentro de una variable


