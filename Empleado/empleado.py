class Empleado:
    '''____________________________________________
    # Atributos
    ____________________________________________'''
    nombres = ""
    apellidos = ""
    '''____________________________________________
    # 1 = Masculino y 2 = Femenino
    _____________________________________________'''
    sexo = 0
    salario = 0

    '''_____________________________________________
    # Metodos
    _____________________________________________'''

    def cambiarSalario(self, nSalario):
    # Aqui va el codigo
        self.salario = nSalario
        return "Su nuevo salario es: ", self.salario

    def consultarSalario(self):
    # Aqui va el codigo
        return self.salario

    def aumentoSalarial(self):
    # Aqui va el codigo
        aumento = self.salario * 0.05
        nSalario = aumento + self.salario
        self.salario = nSalario
        return "Su nuevo salario es: ", self.salario