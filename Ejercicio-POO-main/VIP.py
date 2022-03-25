from CuentaBancaria import CuentaBancaria

class VIP(CuentaBancaria):
    def __init__(self,id,titular,fecha,numerocuenta,saldo,negativo):
        CuentaBancaria.__init__(self,id,titular,fecha,numerocuenta,saldo)
        self.negativo=negativo

    def retirardinero(self,dinero):
        if(self.saldo+self.negativo>=dinero):
            self.saldo=self.saldo-dinero
        else:
            print("Error, el dinero a retirar está fuera de tu limite")

    def transferirdinero(self,dinero,cuenta):
        if (self.saldo+self.negativo>=dinero):
            self.saldo=self.saldo-dinero
            cuenta.saldo=cuenta.saldo+dinero
        else:
            print("Error, el dinero a transferir está fuera de tu limite")

    def cuenta(self):
        cuentastr=CuentaBancaria.cuenta(self)
        return cuentastr + " Cuenta VIP con limite negativo de " + str(self.negativo)