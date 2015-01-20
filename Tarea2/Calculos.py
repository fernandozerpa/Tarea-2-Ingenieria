'''
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''
import datetime
from datetime import timedelta
  
class Calculos:    
    
    """Funcion que calcula el numero de horas totales"""
    def calcularNroHoras (self, fechaIni,fechaFinal):
        if fechaIni <= fechaFinal:
            nroDias = fechaFinal.day - fechaIni.day
            totalHoras = fechaFinal.hour + nroDias*24 -fechaIni.hour
            totalMinutos = totalHoras*60 + fechaFinal.minute - fechaIni.minute
            totalHoras = totalMinutos/60
            return totalHoras
        else:
            return -1
    
    """Funcion que calcula el monto total a pagar"""   
    def calcularMontoTotal(self, fechaIni, fechaFin, tarifa):
        
        tasaD = tarifa.getTasaDiurna()
        tasaN = tarifa.getTasaNocturna()
        
        montoTotal = 0
        """Datetime auxiliar para calcular ultimos minutos restantes"""
        ultima=datetime.datetime(fechaFin.year,fechaFin.month,fechaFin.day,fechaFin.hour,59,0)
        ultima2 = datetime.datetime(fechaFin.year,fechaFin.month,fechaFin.day,fechaFin.hour,0,0)
        ultima = ultima - ultima2
        
        while (fechaIni < fechaFin):
            
            diferencia = fechaFin - fechaIni
            """Caso para los ultimos minutos restantes"""
            if (diferencia <= ultima): 
                """Caso para ultimos minutos en tarifa Diurna""" 
                if (fechaIni.hour == 17 and diferencia.total_seconds()/60 + fechaIni.minute <= 59):
                    
                    montoTotal = montoTotal + tasaD
                    break
                """Caso para ultimos minutos en tarifa Nocturna""" 
                if (fechaIni.hour == 5 and diferencia.total_seconds()/60 + fechaIni.minute <= 59):
                    
                    montoTotal = montoTotal + tasaN
                    break
            """Caso para tarifa Diurna"""    
            if (6 <= fechaIni.hour <= 16 or (fechaIni.hour == 17 and fechaIni.minute == 0)):
                
                montoTotal = montoTotal + tasaD
                
                """Caso en que se cruzan las tarias Diurna y Nocturna """
            elif (fechaIni.hour == 5 and fechaIni.minute > 0 or(fechaIni.hour == 6 and fechaIni.minute == 0)
                  or (fechaIni.hour == 17 and fechaIni.minute > 0) or(fechaIni.hour == 18 and fechaIni.minute == 0)):
                 
                if (tasaN >= tasaD):
                    montoTotal = montoTotal + tasaN
                else:
                    montoTotal = montoTotal + tasaD
                    
                """Caso para tarifa Nocturna"""
            elif ((18 <= fechaIni.hour or fechaIni.hour <= 4) or (fechaIni.hour == 5 and fechaIni.minute == 0)):
                
                montoTotal = montoTotal + tasaN
                
            fechaIni = fechaIni + timedelta(hours=1)
        return montoTotal