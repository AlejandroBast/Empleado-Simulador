from fecha import Fecha

class Empleado:
    #aqui va el codigo
    
    '''-----------------------------------------------------------------
    #     Atributos
    -----------------------------------------------------------------'''
    
    def __init__(self, nombres, apellidos, salario, numeroHijosEmpleado, sexo):
        self.nombres=nombres
        self.apellidos=apellidos
        self.salario=salario
        self.sexo = sexo  # 1 Masculino y 2 Femenino

######## ----------------------------------------------------------------------------------------------------------------------
        self.numeroHijosEmpleado = numeroHijosEmpleado

  #------------------------------------------------------------
    def consultarNumeroHijos(self):
        return "El numero de hijos del empleado es: ", self.numeroHijosEmpleado
    
  #________Calcular Auxilio Educativo del Empleado________#
    def auxiolioEducativo(self):
        porcentaje = self.salario * 0.05
        auxilio = porcentaje * self.numeroHijosEmpleado
        return "Su axilio educativo es de: ", auxilio
    
    def auxilioEducativoEspeficicado(self, auxilioEspecificado):
        porcentaje = self.salario * auxilioEspecificado
        auxilio = porcentaje * self.numeroHijosEmpleado
        return "Su auxilio educativo es de :", auxilio
    
    #_______________________Comparacion________________________#
    def compararSalarios(self, empleado):
        if self.salario > empleado.salario:
            return self.nombres, 'tiene un salario más alto que ', empleado.nombres
        elif self.salario < empleado.salario:
            return empleado.nombres, 'tiene un salario más alto que ', self.nombres
        else:
            return "Ambos empleados tienen el mismo salario."
        
    #_____________________Diferencia Salarial__________________#
    def diferenciaSalarial(self, empleado):
        return self.salario - empleado.salario
    
######## ----------------------------------------------------------------------------------------------------------------------

    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def cambiarSalario(self, nSalario):
        #aqui va el codigo
        self.salario = nSalario
        return "Su nuevo salario es: ", self.salario
    
    def consultarSalario(self):
        # Aqui va el codigo
        return self.salario
    
    def aumentoSalario(self):
        # aqui va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario
        
    def duplicarSalario(self):
        # aqui va el codigo
        nuevoSalario = self.salario * 2
        self.salario = nuevoSalario

    def calcularSalarioAnual(self):
        # aqui va el codigo
        salarioAnual = self.salario*12
        return salarioAnual

    
    def consultarDiaCumpleanios(self):
        return self.fechaNacimiento.ConsultarDia()
    
    def calcularImpuesto(self):       
        return self.calcularSalarioAnual()*0.195
