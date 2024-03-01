class CuentaAhorros:
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    saldo = 0
    interesMensual = 0

    def consultarSaldo(self):
        return "Su salario actual es: ", self.saldo
    
    def consultarInteresMensual(self):
        return "El interes mesual es de: ", self.interesMensual