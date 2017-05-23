import Stack
class Tareas:
    def __init__(self):
        s = Stack()

    def __init__(self, tareas):
        self.s = tareas

    def aTarea(self, tarea):
        self.s.push(tarea)

    def saTarea(self):
        return self.s.pop()
    
