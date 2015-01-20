'''
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

import datetime
from tarifa import Tarifas
from calculo import Calculos
from validacion import Validaciones
from decimal import Decimal , ROUND_HALF_UP


class Reservas:
    
    def __init__(self, fechaIni,fechaFin, horaIni , horaFin , tarifa):
        self.fechaIni = fechaIni
        self.fechaFin = fechaFin
        self.horaIni = horaIni
        self.horaFin = horaFin
        self.tasaDiurna = tarifa.getTasaDiurna()
        self.tasaNocturna = tarifa.getTasaNocturna()
        
    def setFechaIni(self, fechaI):
        self.fechaIni = fechaI
    
    def setFechaFin(self, fechaF):
        self.fechaFin = fechaF
    
    def setHoraIni(self, horaI):
        self.horaIni = horaI
    
    def setHoraFin(self, horaF):
        self.horaFin = horaF
    
    def setTasaDiurna(self, tasaD):
        self.tasaDiurna = tasaD
    
    def setTasaNocturna(self, tasaN):
        self.tasaNocturna = tasaN    
    
    def getFechaIni(self):
        return self.fechaIni
    
    def getFechaFin(self):
        return self.fechaFin
    
    def getHoraIni(self):
        return self.horaIni
    
    def getHoraFin(self):
        return self.horaFin
    
    def getTasaDiurna(self):
        return self.tasaDiurna
    
    def getTasaNocturna(self):
        return self.tasaNocturna

    def main(self):
        
        """verificamos si los datos de entrada son correctos"""
        verificar = Validaciones()
        verificar.fechaValida(self.getFechaIni())
        verificar.fechaValida(self.getFechaFin())
        verificar.horaValida(self.getHoraIni())
        verificar.horaValida(self.getHoraFin())
        tasaDecimalDiurna = Decimal(self.getTasaDiurna())
        verificar.tasaValida(tasaDecimalDiurna)
        tasaDecimalNocturna = Decimal(self.getTasaNocturna())
        verificar.tasaValida(tasaDecimalNocturna)
        
        """creamos el datetime de la fecha de inicio"""
        formatoFechaIni = self.getFechaIni() + self.getHoraIni()
        fechaIniCompleta= datetime.datetime.strptime(formatoFechaIni, "%d/%m/%Y%H:%M")
        
        """creamos el datetime de la fecha final"""
        formatoFechaFin = self.getFechaFin() + self.getHoraFin()
        fechaFinCompleta= datetime.datetime.strptime(formatoFechaFin, "%d/%m/%Y%H:%M")
        
        """creamos el bojeto de tarifa con tipo Decimal, con dos digitos para centimos"""
        tarifas = Tarifas(Decimal(tasaDecimalDiurna.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)),Decimal(tasaDecimalNocturna.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        
        """verificamos si el tiempo de reserva es valido"""
        verificar.tiempoReservaValido(fechaIniCompleta, fechaFinCompleta)
        
        """calculamos el monto final a pagar"""
        montoAPagar = Calculos()
        print(montoAPagar.calcularMontoTotal(fechaIniCompleta, fechaFinCompleta, tarifas))
        return montoAPagar.calcularMontoTotal(fechaIniCompleta, fechaFinCompleta, tarifas) 
        
        