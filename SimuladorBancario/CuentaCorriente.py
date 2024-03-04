class CuentaCorriente:
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    saldo = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    def consultarSaldo(self):
        return self.saldo
    
    def consignarMonto(self, monto):
        self.saldo += monto

#### --- METODO MODIFICADO-----------------------------------------------------------------------------
    def retirarMonto(self, monto):
        precioRetiro = monto * 0.01
        retiro = monto + precioRetiro
        self.saldo -= retiro
        return self.saldo
#### --------------------------------------------------------------------------------
