# -*- coding: utf-8 -*-
"""


@author: VICTORMANUEL
"""
from Queue import Queue
class ProductosRemarcados:
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
                         
    def existe(self, codigo):
        lista = self.s.lista()
        i = 0
        while i < len(lista) and codigo != lista[i].getCod_producto():
            i += 1
        if i < len(lista):
            return True
        else: 
            return False
        
    def posicion(self, codigo):
        lista = self.s.lista()
        i = 0
        while i < len(lista) and codigo != lista[i].getCod_producto():
            i += 1
        return 1
        
    def cambiarPrecio(self, codigo, nPrecio):
        if self.existe(codigo) :
            i = self.posicion(codigo)
            lista = self.s.lista()
            lista[i].setPrecio(nPrecio)
            return True
        else:
            return False
        
    def agregarProd(self, producto):
        self.s.enqueue(producto)
        self.ordenar()
        
    def masRemarcados(self, n):
        resp = []
        if self.s.isEmpty():
            lista = self.s.lista()
            for i in len(lista):
                if lista[i].cantRemarcaciones > n:
                    resp.append(lista[i])
        return resp
    
