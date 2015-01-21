'''
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

import unittest
from decimal import Decimal
from reserva import Reservas
from tarifa import *
from xmlrpc.client import MAXINT

class CasosDePrueba(unittest.TestCase):
    
    
    def reservaciones(self,fechaIni,fechaFin,horaIni,HoraFin,tarifa):
        res = Reservas(fechaIni,fechaFin,horaIni,HoraFin,tarifa)
        return res.main()
    
    def testMaximoNroHoras(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","23/01/2015","00:00","00:00",tarif), 10800) 
    
    def testCruzadoTarifaDiurnaMayor(self):
        tarif = Tarifas("300","200")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","5:45","06:01",tarif),300)
        
    def testCruzadoTarifaNocturnaMayor(self):
        tarif = Tarifas("100","500")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","5:45","06:01",tarif),500)
    
    def testMinimoNroHorasDiurna(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","8:00","8:15",tarif), 100)
        
    def testMinimoNroHorasNocturna(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","00:00","00:15",tarif), 200)
        
    def testFechaMinima(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("01/01/0001","01/01/0001","00:00","00:15",tarif), 200)
        
    def testFechaMaxima(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("31/12/9999","31/12/9999","06:00","06:15",tarif), 100)
        
    def testTarifaMinima(self):
        tarif = Tarifas("0","0")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","06:00","06:15",tarif), 0)
        
    def testTarifaMaxima(self):
        tarif = Tarifas(MAXINT,MAXINT)
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","06:00","06:15",tarif), MAXINT)
        
    def testTarifaMinimaMaxima(self):
        tarif = Tarifas("0",MAXINT)
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","06:00","06:15",tarif), 0)
        tarif = Tarifas(MAXINT,"0")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","06:00","06:15",tarif), MAXINT)
        
    def testHoraMinimaMaxima(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","00:00","23:59",tarif), 3600)
    
    def testTodoDiurno(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","06:00","18:00",tarif), 1200)    
        
    def testTodoNocturno(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","21/01/2015","18:00","6:00",tarif), 2400)
        
    def testTodoDiurnoMasNocturno(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","20/01/2015","06:00","18:01",tarif), 1400)    
        
    def testTodoNocturnoMasDiurno(self):
        tarif = Tarifas("100","200")
        self.assertEqual(self.reservaciones("20/01/2015","21/01/2015","18:00","6:01",tarif), 2500) 
    
    def testTarifasConCentimos(self):
        tarif = Tarifas("100.55","200.00")
        self.assertEqual(self.reservaciones("20/01/2015","21/01/2015","18:00","6:01",tarif), Decimal('2500.55')) 
        
if __name__ == '__main__':
    unittest.main()   