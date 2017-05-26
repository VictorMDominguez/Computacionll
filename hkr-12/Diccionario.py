# -*- coding: utf-8 -*-
"""
Created on Thu May 25 22:22:22 2017

@author: VICTORMANUEL
"""

class Diccionario():
    def __init__(self):
        self.dix = {}
        lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in lista:
            self.dix[i] = []
        
    def __str__(self):
        print self.dix
        
    def agregar(self, palabra):
        palabra = palabra.upper()
        if self.dix.has_key(palabra[0]):
            self.dix[palabra[0]].append(palabra)
            return True
        else:
            return False
            
        