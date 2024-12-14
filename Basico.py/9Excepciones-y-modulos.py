#Excepciones

try:                        #Esta funcion se utiliza para comprobar si una funcion sirve, si no sirve nos lleva directamente al except, y si sirve simplemente se ejecuta
    print(5 + '3')
except NameError as error:
    print('Error de tipo NameError')
    print(error)
except TypeError:
    print('Error de tipo TypeError')
else:
    print('Si jalaaa')
finally:
    print('Esta funcion siempre se va a ejecutar sin importar si la funcion sirvio o no')

try:
    print(5 + 3)
except NameError as error:
    print('Error de tipo NameError')
    print(error)
except TypeError:
    print('Error de tipo TypeError')
else:
    print('Si jalaaa')
finally:
    print('Esta funcion siempre se va a ejecutar sin importar si la funcion sirvio o no')

#Modulos

from 8Funciones import Panchito

Panchito(5,10)

#Los modulos se utilizan para importar funciones de otros ficheros al fichero en el que estamos trabajando.
