class Tarea:
    
    def __init__(self, area, descripcion):
        self.area = area
        self.descripcion = descripcion

    def __str__(self):
        return "Area: " + self.area + "Descripcion: " + self.descripcion

    def setArea(self, area):
        self.area = area

    def getArea(self):
        return self.area

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self):
        return self.descripcion
