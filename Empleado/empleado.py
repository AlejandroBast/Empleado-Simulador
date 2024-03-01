from fecha import Fecha

class Empleado:

    #aqui va el codigo

    '''-------------------------------------
    # Atributos
    -------------------------------------'''
    nombres = ''
    apellidos = ''

    '''-------------------------------------
    # 1 = Masculino y 2 = Femenino
    -------------------------------------'''
    sexo=0
    salario=0
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    def CambiarSalario(self, nSalario):
        # Aqui va el codigo
        self.salario = nSalario 
        return "Su nuevo salario es: ", self.salario
    
    def ConsultarSalario(self):
        # Aqui va el codigo
        return self.salario
    
    def AumentoSalario(self):
        # aqui va el codigo

        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario
        
    def DuplicarSalario(self):
        nuevoSalario = self.salario * 2
        self.salario = nuevoSalario
        
    def CalcularSalarioAnual(self):
        salarioAnual=self.salario*12
        return salarioAnual
    
    def ConsultarDiaCumpleanios(self):
        return self.fechaNacimiento.ConsultarDia()
    
    def CalcularImpuesto(self):
        #Forma 1
        total = self.CalcularSalarioAnual()
        total = total * 0.195
        return total
