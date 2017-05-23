class Movimiento:
    def __init__(self ):
        self.id = 00
        self. fecha = 00
        self.saldo = 00
        self.tipo = "null"

def __init__(self, id, fecha, saldo, tipo ):
    self.id = id
    self. fecha = fecha
    self.saldo = saldo
    self.tipo = tipo

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetFecha(self, fecha):
        self.fecha = fecha

    def GetFecha(self):
        return self.fecha

    def SetSaldo(self, saldo):
        self.saldo = saldo

    def GetSaldo(self):
        return self.saldo

    def SetTipo(self, tipo):
        self.tipo = tipo

    def GetTipo(self):
        return self.tipo

    def __str__(self):
        cadena = "Id: ",self.id,", Fecha: ",self.fecha,", saldo: ",self.saldo,", Tipo: ",self.tipo
        return cadena
