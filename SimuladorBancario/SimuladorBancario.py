from CDT import CDT
from CuentaAhorro import CuentaAhorros
from CuentaCorriente import CuentaCorriente

class SimuladorBancario:
    
    # aqui va el codigo

    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    cedula = ''
    nombre = ''
    mesActual = 0

    '''-----------------------------------------------------------------
    # Asociaciones
    -----------------------------------------------------------------'''
    cedete = CDT()
    ahorros = CuentaAhorros()
    corriente = CuentaCorriente()

    '''-----------------------------------------------------------------
    # Metodos
    -----------------------------------------------------------------'''
    def consultarSaldoAhorros(self):
        return self.ahorros.consultarSaldo()
    
    def consultarSaldoCorriente(self):
        return self.corriente.consultarSaldo()
    
    def consignarCuentaCorriente(self, nValor):
        self.corriente.consultarSaldo() + nValor
        return self.corriente.consultarSaldo()

    def duplicarSaldoAhorros(self):
        self.ahorros.saldo *= 2
        return  self.ahorros.saldo

    def retirarTodoAhorros(self):
        retiroAhorros = self.ahorros.saldo
        self.ahorros.saldo = 0
        return "Se retiraron: ", retiroAhorros, "Su saldo actual es de: ", self.ahorros.saldo
    
    def retirarTodoCorriente(self):
        retiroCorriente = self.corriente.saldo
        self.corriente.saldo = 0
        return "Se retiraron: ", retiroCorriente, "Su saldo actual es de: ", self.corriente.saldo