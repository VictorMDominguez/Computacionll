# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:50:30 2017

@author: VICTORMANUEL
"""
from  Utileria import leerEntero
from  Utileria import leerCadena
from  Empleados import Empleados
from Empleado import Empleado
from Tarea import Tarea
def main():
    cont = True
    empleados = Empleados()
    while cont:
        mens = "1.-Agregar empleado \n"
        mens += "2.-Agregar tarea\n"
        mens += "3.-Tarea completada\n"
        mens += "4.-Salir\n"
        resp = leerEntero(mens)
        if resp == 1:
            codigo = leerEntero("Digite el codigo de empleado: \n")
            empleados.push(Empleado(codigo))
            
        if resp == 2:
            area = leerCadena("Digite el area de la tarea: \n")
            descripcion = leerCadena("Digite la descripcion: \n")
            tarea = Tarea(area, descripcion)
            empleados.agTarea(tarea)
            
        if resp == 3:
            empleado = leerCadena("Digite el numero de empleado: \n")
            if empleados.existe(empleado):
                empleados.tareaComp(empleado)
            
        if resp == 4:
            break
        else:
            print "Respuesta no valida"