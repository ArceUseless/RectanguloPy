'''
Clase Cuadrado que hereda de "Rectangulo"

@author: Rafael Jesus Nieto Cardador
'''

from Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    
    def __init__(self, lado):
        super().__init__(lado,lado)
        
    def __str__(self):
        return Rectangulo.__str__(self)
    
    def __eq__(self, other):
        return (self.alto == other.alto)
    
    def __lt__(self, other):
        return (self.alto < other.alto)
    
    def __gt__(self, other):
        return (self.alto > other.alto)
    
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
    
    cuadrado4 = Cuadrado(7);
    cuadrado5 = Cuadrado(6);
    cuadrado6 = Cuadrado(1);
    
    print("El cuadrado 4 es mayor que el cuadrado 1: "+str(cuadrado4 > cuadrado1))
    print("El cuadrado 5 es igual que el cuadrado 1: "+str(cuadrado5==cuadrado1))
    print("El cuadrado 6 es menor que el cuadrado 1: "+str(cuadrado6 < cuadrado1))
    print("El cuadrado 6 es mayor que el cuadrado 1: "+str(cuadrado6 > cuadrado1))
    
    '''
    'Constructor'
    def __init__(self, ancho, alto):
        if(self.__validaCuadrado(ancho, alto)):
            self.setAncho(ancho)
            self.setAlto(alto)
        else:
            raise CuadradoIrregularException
        
    'Metodos'
    
    
        Devuelve True si "ancho" y "alto" son iguales y False si no es asi
        
        Parametros
            ancho: Entero que contiene el ancho del cuadrado
            alto: Entero que continene el alto del cuadrado
    
    def __validaCuadrado(self, ancho, alto):
        if(ancho == alto):
            return True
        else:
            return False
    
    
        Compara el "alto" de dos cuadrados y devuelve un mensaje dependiendo de si uno es mayor, menor o igual que el otro.
        
        Parametros
            Cuadrado: Objeto de la clase Cuadrado
            
    def comparaCuadrados(self, Cuadrado):
        if(self.getAlto() < Cuadrado.getAlto()):
            return "El segundo cuadrado es mayor que el primero."
        elif(self.getAlto() > Cuadrado.getAlto()):
            return "El primer cuadrado es mayor que el segundo."
        else:
            return "Ambos cuadrados son iguales."
'''