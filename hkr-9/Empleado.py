from Stack import Stack
class Empleado:
    
    def __init__(self, codigo):
        pTareas = Stack()
        self.codigo = 0
        self.pTareas = pTareas
        self.canTareas = len(self.pTareas)

    def __init__(self, codigo, pTareas):
        self.codigo = 0
        self.pTareas = pTareas
        self.canTareas = len(self.pTareas)
        

    def setCodigo(self, codigo):
        self.codigo = codigo
        
    def getCodigo(self):
        return self.codigo

    def setPTareas(self, tareas):
        self.pTareas = tareas

    def getPTareas(self):
        return self.pTareas
    
    def getCanTareas(self):
        return self.pTareas
    
    def tareaRea(self):
        self.pTareas.pop()
