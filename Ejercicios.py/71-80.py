'''
Ejercicio 71: Crear un rectangulo con los siguientes atributos:
base : base del rectangulo
altura : altura del rectangulo
la clase debe de tener los siguientes metodos:
**_init_(self, base, altura): inicializa los atributos de la clase
**calcular_area(self): calcula y devuelve el area del triangulo
**calcilar_perimetro(self): calcula y devuelve el perimetro del 
rectangulo
'''

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base * self.altura
        
    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)
    
rect1 = Rectangulo(5,3)
print (f'El area es {rect1.calcularArea()}')
print (f'El perimetro es {rect1.calcularPerimetro()}')

'''
Ejercicio 72: Crear una clase Circulo con los siguientes atributos:
*radio : radio del circulo
La clase debe tener los siguientes metodos:
*__init__(self, radio) : inicializa los atributos de la clase
*calcularArea(self) : calcula y devuelve el area del circulo
*calcularPerimetro(self) : calcula y devuelve el perimetro del circulo
'''
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def CalcularAreaC(self):
        return self.radio ** 2 * math.pi
    
    def CalcularPerimetroC(self):
        return 2 * self.radio * math.pi

Circulo1 = Circulo(10)

print (f'El area es {Circulo1.CalcularAreaC()}')
print (f'El perimetro es {Circulo1.CalcularPerimetroC()}')