class Fecha:
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    def _init_(self, dia=0, mes=0, anio=0):
        self.dia=dia
        self.mes=mes
        self.anio=anio
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def ConsultarDia(self):
        return self.dia
    
    def ConsultarMes(self):
        return self.mes
    
    def ConsultarAnio(self):
        return self.anio