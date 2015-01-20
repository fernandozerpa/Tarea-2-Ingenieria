'''
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

class Reserva:
    
    def __init__(self, fechaIni,fechaFin, horaIni , horaFin , tasaDiurna, tasaNocturna):
        self.tasaDiurna = tasaDiurna
        self.tasaNocturna = tasaNocturna
        self.fechaIni = fechaIni
        self.fechaFin = fechaFin
        self.horaIni = horaIni
        self.horaFin = horaFin