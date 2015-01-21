'''
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

import unittest
from reserva import Reservas
from tarifa import *

class CasosDePrueba(unittest.TestCase):
    
    
    def reservaciones(self,fechaIni,fechaFin,horaIni,HoraFin,tarifa):
        res = Reservas(fechaIni,fechaFin,horaIni,HoraFin,tarifa)
        return res.main()
    
    def testMaximoNroHoras(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","23/01/2015","00:00","00:00",tarif), 10800) 
        
    def testMinimoNroHorasNocturna(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","00:00","00:15",tarif), 200) 
        
        
if __name__ == '__main__':
    unittest.main()   