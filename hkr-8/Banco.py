import Stack

class Banco:
    def __init__(self):
        self.s = Stack()

    def __str__(self):
        return self.s.items
        
    def lista(self):
        return self.s.lista()

    def saldo(self, cuenta):
        lista = self.lista()
        saldoTotal = 0.0
        for i in lista:
            if lista[i].cuenta == cuenta:
                if lista[i].tipo in "d":
                    saldoTotal += lista[i].saldo
                if lista[i].tipo == "r":
                    saldoTotal -= lista[i].saldo
        return saldoTotal

    def depositos(self, inf, sup):
        lista = self.lista()
        depositos = 0.0
        n = 0
        for i in lista:
            if lista[i].tipo in "d" and lista[i].fecha >= inf and lista[i].fecha <= sup:
                n += 1
                depositos += lista[i].saldo
        return "Numero de depositos: " + n + "\nCantidad depositada: " + depositos

    def retiros(self, inf, sup):
        lista = self.lista()
        retiros = 0.0
        n = 0
        for i in lista:
            if lista[i].tipo in "r" and lista[i].fecha >= inf and lista[i].fecha <= sup:
                n += 1
                retiros -= lista[i].saldo
        return "Numero de retiros: ",n,"\nCantidad retirada: ",retiros

    def mov(self, movimiento):
        self.s.push(movimiento)

    def aStack(self, lista):
        if not self.s.isEmpty():
            self.s.items = []
        for i in lista:
            self.s.push(lista[i])
