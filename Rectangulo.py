'''
Clase Rectangulo cuyos parametros son "ancho" y "alto"

*Nota: Se que los getters y los setters se hacen de otra forma, pero debido a algunos problemas he decidido hacerlos 
por el metodo mas basico.

@author: Rafael Jesus Nieto Cardador
'''

class Rectangulo(object):
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        if not Rectangulo.__validaParametros(self, alto):
            raise ArithmeticError
        else:
            self.__alto = alto
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if Rectangulo.__validaParametros(self, ancho) == False:
            raise ArithmeticError
        else:
            self.__ancho = ancho
    
    
        
    def __str__(self):
        cadena = ""
        for i in range(self.alto):
            for j in range(self.ancho):
                if(i == 0 or i == self.alto-1):
                    cadena = cadena + "##"
                elif(j == 0 or j == self.ancho-1):
                    cadena = cadena + "##"
                else:
                    cadena += "  "
            cadena = cadena + "\n"
        return cadena
    '''
    Devuelve True si los parametros estan en el rango correcto y False si no es asi.
        
        Parámetros:
            parametro: Puede representar tanto a "ancho" como "alto"
    
    '''
    @staticmethod
    def __validaParametros(self, parametro):
        if(parametro <= 0 or parametro >10):
            return False
        else:
            return True
    
if __name__ == "__main__":
    print("Creamos un rectangulo de prueba con los datos correctos e imprimimos su estado.")
    rectangulo1 = Rectangulo(6,7)
    print(rectangulo1)
    
    print("Ahora creamos un rectangulo con medidas incorrectas.");
    try:
        rectangulo2 = Rectangulo(0, 12)
    except ArithmeticError:
        print("ArithmeticException: Parametro fuera de rango.")

