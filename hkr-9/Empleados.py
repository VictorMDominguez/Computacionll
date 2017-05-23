from Stack import Stack
class Empleados:
    def __init__(self):
        self.t = Stack()
        
    def agEmpleado(self, empleado):
        self.t.push(empleado)
        
    def agTarea(self, tarea):
        menos = 0
        j = 0
        lista = self.t.lista()
        for i in lista:
            if lista[i].canTareas < menos:
                j = i
                menos = lista[i].canTareas
        lista[j].pTareas.push(tarea)
        if not self.t.isEmpty():
            self.t.items = []
        for i in lista:
            self.t.push(lista[i])
    
    def lista(self):
        return list(self.t.items)
    
    def existe(self, empleado):
        lista = self.lista
        enc = False
        for i in lista:
            if lista[i].codigo == empleado:
                enc = True
        return enc
    
    def tareaComp(self, empleado):
        lista = self.lista()
        for i in lista:
            if lista[i].codigo == empleado:
                lista[i].pTareas.pop()
                break
    #def
        
            
    