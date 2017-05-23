class Movimiento:
    

    def __init__(self, id, cuenta, fecha, saldo, tipo):
        self.id = id
        self.cuenta = cuenta
        self. fecha = fecha
        self.saldo = saldo
        self.tipo = tipo

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def setCuenta(self, cuenta):
        self.cuenta = cuenta

    def getCuenta(self):
        return self.id

    def setFecha(self, fecha):
        self.fecha = fecha

    def getFecha(self):
        return self.fecha

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def __str__(self):
        cadena = "Id: " + self.id + ", Fecha: " + self.fecha + ", saldo: " + self.saldo + ", Tipo: " + self.tipo

        return cadena
