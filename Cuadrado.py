'''
Clase Cuadrado que hereda de "Rectangulo"

@author: Rafael Jesus Nieto Cardador
'''

from Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    
    def __init__(self, lado):
        super().__init__(lado,lado)
    
    def __eq__(self, other):
        return (self.alto == other.alto)
    
    def __lt__(self, other):
        return (self.alto < other.alto)
    
    def __gt__(self, other):
        return (self.alto >= other.alto)
    
    @property
    def lado(self):
        return super.alto
    
    @lado.setter
    def lado(self, lado):
        self.alto=lado
        self.ancho=lado
    
        
if __name__ == "__main__":
    print("Creamos un cuadrado de prueba con los datos correctos e imprimimos su estado.")
    cuadrado1 = Cuadrado(6)
    print(cuadrado1)
    
    print("Ahora creamos un cuadrado con medidas incorrectas.");
    try:
        cuadrado2 = Cuadrado(0)
    except ArithmeticError:
        print("ArithmeticException: Parametro fuera de rango.")
        
    print("\nVamos a crear tres cuadrados:"
        + "\n'cuadrado4' sera mayor que 'cuadrado1'."
        + "\n'cuadrado5' sera menor que 'cuadrado1'."
        + "\n'cuadrado6' sera igual que 'cuadrado1'.\n");
    
    cuadrado3 = Cuadrado(1);
    cuadrado4 = Cuadrado(6);
    cuadrado5 = Cuadrado(9);
    
    print("Cuadrado 1 es mayor o igual que cuadrado 3: ",cuadrado1 > cuadrado3)
    print("Cuadrado 1 es mayor o igual que cuadrado 4: ",cuadrado1 > cuadrado4)
    print("Cuadrado 1 es mayor o igual que cuadrado 5: ",cuadrado1 > cuadrado5,"\n")
    
    print("Cuadrado 1 es menor que cuadrado 3: ",cuadrado1 < cuadrado3)
    print("Cuadrado 1 es menor que cuadrado 4: ",cuadrado1 < cuadrado4)
    print("Cuadrado 1 es menor que cuadrado 5: ",cuadrado1 < cuadrado5,"\n")
    
    print("Cuadrado 1 es igual que cuadrado 3: ",cuadrado1 == cuadrado3)
    print("Cuadrado 1 es igual que cuadrado 4: ",cuadrado1 == cuadrado4)
    print("Cuadrado 1 es igual que cuadrado 5: ",cuadrado1 == cuadrado5)
    
    
    