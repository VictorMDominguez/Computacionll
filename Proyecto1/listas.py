# -*- coding: utf-8 -*-
"""
Created on Tue May 23 19:38:02 2017

@author: VICTORMANUEL
"""
from os import walk
import os.path
import numpy
import matplotlib.pyplot  as plt
import matplotlib.image as mpimg

import os
from os import walk
from PIL import Image
from Imagen import *


def diccionario():
    imagenes = {}
    
    for (ruta,carpeta,imagen) in walk("C:\Users\VICTORMANUEL\Desktop\Imagenes"):
        imagenes[ruta] = imagen
    return imagenes
            
def listaImg():
    imagenes = diccionario()
    lista = []
    for ce in imagenes:
        for me in imagenes[ce]:
            if me.endswith(('.png', '.jpg', '.gif')):
                lista.append( ce + "\\" + me )
    return lista
            


def mostrar():
    
    img = mpimg.imread("C:\Users\VICTORMANUEL\Desktop\Imagenes\Nueva carpeta (2)\1.jpg")
    plt.imshow(img)
    img.show()
    

def main():
    Lista_imagen = listaImg()
    for i in Lista_imagen:
        if i.endswith(('.png', '.pnj', '.gif')):
            ficheros = os.listdir("C:\Users\VICTORMANUEL\Desktop\Imagenes\Nueva carpeta (2)\1.jpg")
            mi_imagen= Image.open(ficheros)
            mi_imagen.show()
