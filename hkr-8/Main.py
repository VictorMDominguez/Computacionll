from Utileria import leerEntero
from Utileria import leerChar
import Movimiento
import Banco
class Main:
    def main():
        cont = True
        banco = Banco()
        while cont:
            inicio = "1.-Agragar Movimiento\n"
            inicio += "2.-Saldo de cuenta\n"
            inicio += "3.-Depositos\n"
            inicio += "4.-Retiros\n"
            inicio += "5.-Salir\n"
            resp = leerEntero("Digite su respuesta\n")
            
            
            if resp == 1:
                id = leerEntero("Digite el id")
                cuenta = leerEntero("Digite el Numero de cuneta")
                fecha = leerEntero("Digite la fecha")
                saldo = leerEntero("Digite ls cantidad de dinero")
                tipo = leerChar("Digite el tipo de cuenta")
                movimiento = Movimiento(id, cuenta, fecha, saldo, tipo)
                banco.mov(movimiento)
                
                
            if resp == 2:
                sCuenta = leerEntero("digite un numero de cuenta")
                print banco.saldo(sCuenta)
            
            
            if resp == 3:
                inf = leerEntero("Digite el limite inferior de la busqueda")
                sup = leerEntero("Digite el limite superior de la busqueda")
                if sup < inf :
                    print "Intervalo no valido"
                else:
                    print banco.retiros(inf, sup)
                    
                    
            if resp == 4:
                inf = leerEntero("Digite el limite inferior de la busqueda")
                sup = leerEntero("Digite el limite superior de la busqueda")
                if sup < inf :
                    print "Intervalo no valido"
                else:
                    print banco.depositos(inf, sup)
                    
                    
            if resp == 5:
                cont = False
        