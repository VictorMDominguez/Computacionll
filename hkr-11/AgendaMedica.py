# -*- coding: utf-8 -*-
"""


@author: VICTORMANUEL
"""
class AgendaMedica:
    def __init__(self, codigoMedico, fechAtencion, turnosLibres, turnosOcupados):
        self.codigoMedico = codigoMedico
        self.fechAtencion = fechAtencion
        self.turnosLibres =  turnosLibres
        self.turnosOcupados = turnosOcupados
        
    def setCodigoMedico(self, codigoMedico):
        self.codigoMedico = codigoMedico
        
    def getCodigoMedico(self):
        return self.codigoMedico
        
    def setFechAtencion(self, fechAtencion):
        self.fechAtencion = fechAtencion
        
    def getFechAtencion(self):
        return self.fechAtencion
        
    def setTurnosLibres(self, turnosLibres):
        self.turnosLibres =  turnosLibres        
        
    def getTurnosLibres(self):
        return self.turnosLibres
        
    def setTurnosOcupados(self, turnosOcupados):
        self.turnosOcupados = turnosOcupados
        
    def getTurnosOcupados(self):
        return self.turnosOcupados