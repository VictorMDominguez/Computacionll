# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:23:52 2017

@author: VICTORMANUEL
"""

 def __init__(self):
     self. img = self.diccionario()
     
     
def dicciionario():
    imagenes = {}
    imagenes.
    for (ruta,carpeta,imagen) in walk("C:\Users\VICTORMANUEL\Desktop\Imagenes"):
        imagenes[ruta] = imagen
    return imagenes