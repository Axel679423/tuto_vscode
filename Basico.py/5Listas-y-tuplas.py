#Listas

mi_lista = ['python', 53, False] #hacemos una lista.

print(type(mi_lista))            #pedimos que imprima el tipo de variable que es 'mi_lista'.

print(mi_lista)                  #pedimos que imprima 'mi_lista' en el monitor serie.
print(mi_lista[-1])              #pedimos que imprima el ultimo elemento de la lista.
mi_lista.append(53)            #'append' agrega un elemento al final de la losta, en este caso, agrego el numero 53
print(mi_lista)                  #pedimos que imprima la lista modificada
mi_lista.insert(3, True)         #'insert' agrego el termino 'true' despues del tercer lugar de la lista
print(mi_lista)                  #pedimos que imprima la lista modificada
mi_lista.remove(53)              #'remove' elimina el elemento que elegimos, en este caso el 53
print(mi_lista)                  #pedimos que imprima la lista modificada
print(mi_lista.pop(2))           #'pop' elimina el termino que est en la posicion que queremos de la lista, en este caso el elemento que esta en la posicion 2 de la lista
print(mi_lista)                  #pedimos que imprima la lista modificada
print(mi_lista.count(53))        #este comando cuenta la cantidad de veces que existe el mismo termino en la misma lista
mi_lista.reverse                 #este comando invierte el orden de los terminos de la lista
print(mi_lista)                  #imprimimos la lista nueva
mi_lista.clear                   #este comando elimina todos los terminos de la lista
print(mi_lista)                  #imprimimos la lista modificada


#Tuplas

mi_tupla = (53, 'gato', 7.4, 'True')    #generamos nuestra tupla.
print(type(mi_tupla))                   #pedimos que nos diga el tipo de variable que es 'mi_tupla'.

print(mi_tupla[1])                      #le pedimos que solo imprima el primer elemento de la tupla.
print(mi_tupla.count(53))               #pedimos que nos diga cuantos '53' hay en la tupla.
print(mi_tupla.index(7.4))              #le pedimos que nos diga en que posicion de la tupla esta el termino 7.4.
mi_tupla = list(mi_tupla)               #covertimos la tupla a una lista.
print(type(mi_tupla))                   #le pedimos que nos diga que tipo de variable es la tupla, la cual se convirtio en una lista.
mi_tupla.pop()                          #le pedimos que nos elimine el ultimo termino de la tupla.
print(mi_tupla)                         #pedimos que imprima la tupla modificada.
mi_tupla = tuple(mi_tupla)              #convertimos la tupla a una tupla nuevamente.
print(type(mi_tupla))                   #preguntamos que tipo de variable es la tupla.
print(mi_tupla)                         #pedimos que imprima la tupla.