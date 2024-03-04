from CuentaAhorro import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    def __init__(self, cedula, nombre, mesActual, tipoCliente):
        self.cedula = cedula
        self.nombre = nombre
        self.mesActual = mesActual

##### ---TIPO CLIENTE--------------------------------------------------------------
        self.tipoCliente = tipoCliente
#### -------------------------------------------------------------------------------
        
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    ahorros = CuentaAhorros()
    corriente = CuentaCorriente()
    cdt = CDT()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def calcularSaldoToTal(self):
        return self.ahorros.consultarSaldo() + self.corriente.consultarSaldo()
        
    def consignarCuentaCorriente(self, monto):
        self.corriente.consignarMonto(monto)
        
    def consignarCuentaAhorros(self, monto):
        self.ahorros.consignarMonto(monto)
    
    def transferirAhorrosACorriente(self):
        self.consignarCuentaCorriente(self.ahorros.consultarSaldo())
        self.ahorros.retirarMonto(self.ahorros.consultarSaldo())
    
    def duplicarAhorro(self):
        self.consignarCuentaAhorros(self.ahorros.consultarSaldo())
    
    def retirarCuentaCorriente(self, monto):
        self.corriente.retirarMonto(monto)
    
    def retirarCuentaAhorros(self, monto):
        self.ahorros.retirarMonto(monto)
    
    def retirarTodo(self):
        total = self.CalcularSaldoToTal()
        self.TransferirAhorrosACorriente()
        self.RetirarCuentaCorriente(total)
        
        return total
    
#### ---CAMBIAR TIPO DE CLIENTE-----------------------------------------------------------------------------
    def cambiarTipoCliente(self, nuevoTipoCliente):
        self.tipoCliente = nuevoTipoCliente

    def consultarSaldoCorriente(self):
        return self.corriente.consultarSaldo()
#### --------------------------------------------------------------------------------

    
    