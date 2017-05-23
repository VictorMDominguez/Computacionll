import Stack
import Movimiento

class Banco:
    def __init__(self):
        s = Stack():

    def __str__(self):
        lista = self.lista()
        salida = ""
        for mov in lista:
            salida += lista[mov]
    return salida

    def lista(self):
        return s.lista()

    def movimiento(self, movimiento):
        s.push(movimiento)

    def edodeCuenta(self, cuenta):
        lista = s.lista()
        saldoTotal = 0.0
        for i in lista:
            if lista[i].cuenta == cuenta:
                if lista[i].tipo in "Dd":
                    saldoTotal += lista[i].saldo
                if lista[i].tipo in "Rr":
                    saldoTotal -= lista[i].saldo
    return saldoTotal

    
