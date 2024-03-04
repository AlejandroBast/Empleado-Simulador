class CuentaAhorros:
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    saldo = 0
    interesMensual = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    def consultarSaldo(self):
        return self.saldo
    
    def consultarInteresMensual(self):
        return self.interesMensual
    
    def consignarMonto(self, monto):
        self.saldo += monto
        
    def retirarMonto(self, monto):
        self.saldo -= monto