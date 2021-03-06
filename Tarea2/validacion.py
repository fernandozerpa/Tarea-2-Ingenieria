'''
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

import datetime
from calculo import Calculos
from decimal import Decimal , ROUND_HALF_UP

class Validaciones:
    
    def fechaValida(self, fecha):
        try:
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
        except ValueError:
            raise ValueError("El formato de fecha es incorrecto, el formato es: 'dd/mm/aaaa'")
        
    def horaValida(self, hora):
        try:
            datetime.datetime.strptime(hora, '%H:%M')
        except ValueError:
            raise ValueError("El formato de hora es incorrecto , el formato es 'hh:mm', entre 00:00 y 23:59")
        
    def tasaValida(self,tasa):
        if (tasa < 0):
            raise Exception("La tasa Diurna y Nocturna no pueden ser negativas")
        if (tasa != Decimal(tasa.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))):
            raise Exception("La tasa debe estar expresada en bolivares y centimos(dos digitos), por ejemplo 100.34")
        
    def tiempoReservaValido(self, fechaIni, fechaFin):        
        reserva = Calculos()
        if (reserva.calcularNroHoras(fechaIni, fechaFin) < 0.25 ):
            raise Exception("El tiempo de reservacion minimo es de 15 Minutos")
        if (reserva.calcularNroHoras(fechaIni, fechaFin) > 72):
            raise Exception("El tiempo de reservacion maximo es de 72 Horas")