#Lista comprimida

listaNormal = [1,2,3,4,5,6,7,8,9,10]
print(listaNormal)

listaComprimida = [i for i in range(8)]
print(listaComprimida)

miString = 'Joel homosexual'

listaComprimida = [i for i in miString]
print(listaComprimida)

def sumaDeNumeros(numero):
    numero += 'Si'
    return numero

miString = 'Joel joto'
listaComprimida = [sumaDeNumeros(i) for i in miString]
print(listaComprimida)

#Lambdas

miLambda = lambda num1, num2: num1 + num2
miLambda(5,4)
print(miLambda(5,4))

def defLambda(value):
    return lambda number: value + number

print(defLambda(5)(5))