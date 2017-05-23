# -*- coding: utf-8 -*-
"""


@author: VICTORMANUEL
"""
from Queue import Queue
class AgendasMedicas:
    def __init__(self):
        self.s = Queue()
        
    def ordenar(self):
        lista = self.s.lista()
        for i in len(lista):
            for j in len(lista):
                if lista[j] > lista[j+1]:
                    k = lista[j+1]
                    lista[j+1] = lista[j]
                    lista[j] = k
        self.s.setLista(lista)
   
    def agregar(self, AgendaMedica):
        self.s.enqueue(AgendaMedica)
        self.ordenar()
    
    def VerifTurno(self, codigoMedico, fechAtencion):
        resp = False
        if not self.s.isEmpty() and self.existe(codigoMedico):
            lista = self.s.lista()
            i = 0
            while i < len(lista) and not resp:
                if lista[i].codigoMedico == codigoMedico:
                    resp = True
                else:
                    i += 1
        return resp
    
    def existe(self, codigoMedico):
        lista = self.s.lista()
        resp = False
        i = 0
        while i < len(lista) and not resp:
            if lista[i].codigoMedico == codigoMedico:
                resp = True
            else:
                i += 1
        return resp 