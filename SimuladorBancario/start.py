from SimuladorBancario import SimuladorBancario

####---Testeo de Funcionalidad-----------------------------------------------------
cliente1 = SimuladorBancario("123456", "Juan", 1, "Normal")
cliente1.consignarCuentaCorriente(500000)
print(cliente1.consultarSaldoCorriente())
cliente1.retirarCuentaCorriente(50000)
print(cliente1.consultarSaldoCorriente())
