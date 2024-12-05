#Condicionales

numero = 7

Si = 'ola'

if 4 > 6 or numero ==7:
    print('4 es menor que 6')
  
if len(Si) < 2:
         print('buenas tardes')
elif numero == 7:
    print('numero es igual a 7')
else: 
    print('no se cumplio ninguna de las condiciones')
    
    
#Bucles

numero = 0

while numero < 10:
    numero += 1
    print(numero) 
    if numero < 5:
        print('es menor que 5')
        break


lista = [2,4,6,8,10,12,14,16,18,20]
    
for n in range(101):
    print(n)
    if numero < 5:
        print('es menor que 5')
        break
    
lista_2 = ['a', 'b', 'c', 'd']
for c in lista_2:
    print(c)