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
    
    def test1(self):
        tarif = Tarifas("100","200")
        self.failUnless(10800 == self.reservaciones("01/01/0001","04/01/0001","00:00","00:00",tarif))
        
if __name__ == '__main__':
    unittest.main()   