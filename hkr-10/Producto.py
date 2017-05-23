# -*- coding: utf-8 -*-
"""


@author: VICTORMANUEL
"""
class Producto:
    def __init__(self, cod_producto, precio, cantRemarcaciones):
        self.cod_producto = cod_producto
        self.precio = precio
        self.cantRemarcaciones = cantRemarcaciones
    
    def setCod_producto(self, cod_producto):
        self.cod_producto = cod_producto
        
    def getCod_producto(self):
        return self.cod_producto 
    
    def setPrecio(self, precio):
        self.precio = precio
        self.cantRemarcaciones += 1
        
    def getPrecio(self):
        return self.precio
    
