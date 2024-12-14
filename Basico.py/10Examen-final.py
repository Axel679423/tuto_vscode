#El segundo mas grande

lista = [5,7,6,9,3,8,]

lista.sort()
print(lista[-2])

#Conversor de tiempo

Dias = int(input('Ingrese su tiempo en dias'))
Horas = int(input('Ingrese su tiempo en horas'))
Minutos = int(input('Ingrese su tiempo en minutos'))
Segundos = int(input('Ingrese su tiempo en segundos'))

def tiempo(Dias, Horas, Minutos, Segundos):
    return Dias * 8.64e+7 + Horas * 3.6e+6 + Minutos * 60000 + Segundos * 1000

resultado = tiempo(Dias, Horas, Minutos, Segundos)
print(resultado)
print(f'Tu tiempo en milisegundos es de {resultado} milisegundos')

#Contador Fizz Buzz

numero4 = 1
while numero4 <= 100:
    if numero4 % 3 == 0 and numero4 % 5 == 0:
        print('FizzBuzz')
    elif numero4 % 3 == 0:
        print('Fizz')
    elif numero4 % 5 == 0:
        print('Buzz')
    else:
        print(numero4)
    numero4 = numero4 + 1
    