#Strings
mi_primer_string = 'Mi string con comillas dobles'
mi_segundo_string = 'Mi string con comillas simples'

print(mi_primer_string, mi_segundo_string)  #Aqui se estan poniendo dos variables, una a un lado de la otra. 
print(f'este texto es parte de una variable {mi_segundo_string} hola buenas tardes')    #Aqui se esta colocando texto y variables comibados, a esto se le llama concatenar.

tercer_string = 'Hola'  

a,b,c,d = tercer_string

print(a)
print(b)
print(c)
print(d)

print(f'{a},{b},{c},{d}')

print(mi_primer_string.upper())           #upper pone todo en mayusculas.
print(mi_primer_string.capitalize())      #pone la primera letra en mayusculas.
print(mi_primer_string.lower())           #pone todo en minusculas.
print(len(mi_primer_string))              #cuenta la cantidad de caracteres.
print(mi_primer_string.find('r'))         #encuentra el caracter que buscamos.
print(mi_primer_string.count('l'))        #cuenta la cantidad de veces que aparece el caracter que buscamos en la variable.
print(mi_primer_string.upper().isupper()) #pregunta si todo esta escrito en mayusculas.