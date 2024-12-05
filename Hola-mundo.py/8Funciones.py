#Funciones

def Panchito(numero_1, numero_2 = 10):
    print(numero_1 + numero_2)
    return(numero_1 + numero_2)
result = Panchito(50, 60)
Panchito(10, 20)
Panchito(5, 10)
Panchito(8)

print(result)


#Clases

class unHumano:
    def __init__(self, altura, edad, peso):
        self.altura = altura
        self.edad = edad
        self.peso = peso
    def comer(self):
        print(f'el humano de {self.edad} años esta comiendo')
humano_1 = unHumano(1.80, 23, 87)

print(f'el humano 1 mide {humano_1.altura}, pesa {humano_1.peso}kilos, y tiene {humano_1.edad}años')
humano_1.comer()