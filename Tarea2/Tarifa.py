'''
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

class Tarifa:
    
    def __init__(self, tasaDiurna, tasaNocturna):
        self.tasaDiurna = tasaDiurna
        self.tasaNocturna = tasaNocturna
    
    """Dar o Actualizar valor de la Tasa Diurna"""    
    def setTasaDiurna(self,tasaD):
        self.tasaDiurna =  tasaD
    
    """Dar o Actualizar valor de la Tasa Nocturna"""    
    def setTasaNocturna(self,tasaN):
        self.tasaNocturna = tasaN 
        
    """Obtener tasa Diurna"""    
    def getTasaDiurna(self):
        return self.tasaDiurna
    
    """Obtener tasa Nocturna"""    
    def getTasaNocturna(self):
        return self.tasaNocturna 
    