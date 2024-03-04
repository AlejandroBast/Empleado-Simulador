from empleado import Empleado

empleado1 = Empleado("juan", "Perez", 1000000, 1, 5)
empleado2 = Empleado("pedro", "martinez", 6000000, 1, 3)
empleado3 = Empleado("Maria", "benitez", 6000000, 2, 0)

#________________________Prueba de Metodo - Calculacion de Auxilio________________________#
print(empleado1.consultarNumeroHijos())
print(empleado1.auxiolioEducativo())
print(empleado1.auxilioEducativoEspeficicado(0.15))

#________________________Prueba de Metodo - Comparacion________________________#
print(empleado2.compararSalarios(empleado1))


