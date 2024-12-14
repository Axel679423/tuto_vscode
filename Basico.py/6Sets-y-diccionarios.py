#Sets

mi_set = {}
print(type(mi_set))

mi_set = {'pipi', 'popo', 'caca'}
print(type(mi_set))

print(mi_set)       #Los sets siempre imprimen en orden aleatoreo sus variables, y no puede haber una variable repetida dentro de un 'set'.

mi_otro_set = {'pipi', 'popo', 'caquita'}

mi_set.difference_update(mi_otro_set)
print(mi_set)


#Diccionarios

mi_diccionario = {'a', 'b'}

print(type(mi_diccionario))

mi_diccionario = {'Nombre':'Axel', 'Apellido':'Garcia'}

print(type(mi_diccionario))

print(mi_diccionario['Apellido'])

print(mi_diccionario.keys())
print(mi_diccionario.values())
mi_diccionario = list(mi_diccionario)
print(type(mi_diccionario))



    
    

