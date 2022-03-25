from CuentaBancaria import CuentaBancaria,fechatostring, compararfechas

class APlazoFijo(CuentaBancaria):
    def __init__(self,id,titular,fecha,numerocuenta,saldo,vencimiento):
        CuentaBancaria.__init__(self,id,titular,fecha,numerocuenta,saldo)
        self.vencimiento=vencimiento

    def retirardinero(self,dinero,fechaactual):
        if(compararfechas(fechaactual,self.vencimiento)<0):
            dinero=dinero*1.05
        CuentaBancaria.retirardinero(self,dinero)

    def cuenta(self):
        cuentastr=CuentaBancaria.cuenta(self)
        return cuentastr + " Cuenta a plazo fijo con vencimento " + fechatostring(self.vencimiento)