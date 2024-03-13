# **TALLER - CONSTRUCCION DE ALGORITMOS** <img src="https://camo.githubusercontent.com/cd122cf1a24b8e8ccb81d65d3995ce9b80cc22d315c9409e09d80aad389006a3/68747470733a2f2f656d6f6a69732e736c61636b6d6f6a69732e636f6d2f656d6f6a69732f696d616765732f313537393231363131312f373535302f70696b616368755f776176652e6769663f31353739323136313131" data-canonical-src="https://emojis.slackmojis.com/emojis/images/1579216111/7550/pikachu_wave.gif?1579216111" style="max-width: 7%; display: inline-block;" data-target="animated-image.originalImage">

Hola, aquí podrás ver mi desarrollo del **taller** para las clases SimuladorBancario y Empleado. He decidido optar por hacer un **README** para poder dar una mejor comprensión de cómo funcionan las **implementaciones** que he hecho a mi codigo.

## **Contenido**

1. [**class** Empleado](#empleado)
2. [**class** SimuladorBancario](#simuladorbancario)

## **Empleado**
En la primera parte nos pedia **modelar** un nuevo **atributo** que nos permitiera saber el **número de hijos del empleado**: 
```python
class Empleado:
    def __init__(selfnumeroHijosEmpleado):
        self.numeroHijosEmpleado = numeroHijosEmpleado

    def consultarNumeroHijos(self):
        return self.numeroHijosEmpleado
```
Por lo que defini la **variable `numeroHijosEmpleado`** para poder acceder a esta informacion, depues cree el **metodo `consultarHijosEmpleado`** el cual simplemente retornara el numero de **hijos** que tiene nuestro empleado.

Ahora para la siguiente parte nos pide que a partir de esto creemos un **nuevo atributo** que nos permita calcular el **Auxilio Educativo** que le corresponderia al empleado, ya sea con un parametro ya definido o uno personalizado:
```python
    def auxiolioEducativo(self):
        porcentaje = self.salario * 0.05
        auxilio = porcentaje * self.numeroHijosEmpleado
        return "Su axilio educativo es de: ", auxilio
    
    def auxilioEducativoEspeficicado(self, auxilioEspecificado):
        porcentaje = self.salario * auxilioEspecificado
        auxilio = porcentaje * self.numeroHijosEmpleado
        return "Su auxilio educativo es de :", auxilio
``` 
Aqui cree **2** metodos **`auxilioEducativo`** y **`auxilioEducativoEspecifacado`**, funcionan de la siguiente manera:

* `auxilioEducativo` **No recibe parametros** ya que este funciona de manera ya **definida**, primeramente se asigna un **valor** a `porcentaje` siendo este el resultado de **multiplicar el salario del empleado por el 5%**. Despues defini la **variable `auxilio`** que multiplicara el valor del auxilio educativo por el numero de hijos dandonos el valor del auxilio educativo. 

*  `auxilioEducativoEspecifacado` Aqui **SI** recibe parametro ya que esta es una **accion personalizada** que se puede cambiar, este funciona de una manera **similar** a `auxilioEducativo` solo que aqui podemos especificar cuanto porcentaje cubrira el auxilio educativo
---
Ahora nos pide que **implementemos** un nuevo metodo:
 ```python 
   def compararSalarios(self, empleado):
        if self.salario > empleado.salario:
            return self.nombres, 'tiene un salario más alto que ', empleado.nombres
        elif self.salario < empleado.salario:
            return empleado.nombres, 'tiene un salario más alto que ', self.nombres
        else:
            return "Ambos empleados tienen el mismo salario."

    def diferenciaSalarial(self, empleado):
        return self.salario - empleado.salario
```
Aqui intente de **muchas manera** pero la unica forma que se me ocurrio fue usar las **condicionales `IF, ELIF y ELSE`** para poner las condiciones de que **si al comparar** alguno tiene un salario mas alto que el otro **nos lo haga saber** denotando sus nombres, si no, nos indique que tienen el mismo salario. Tambien como no estaba muy seguro implemente otro metodo que calcula la diferencia de salarios, osea el resultado de restar el salario de uno con el otro

---


# **SimuladorBancario**

Ahora es el turno de la  clase `SimuladorBancario`.
```python
    def __init__(self, tipoCliente):
        self.tipoCliente = tipoCliente
```

El punto nos pide agregar el atributo **tipo de cliente** (VIP, PLATINO, DIAMANTE, NORMAL, ETC) para eso implemente el atributo **`tipoCliente`** para modelar eso en mi clase `SimuladorBancario `, ahora nos pide un **nuevo metodo** para actualizar este atributo el cual es: 
```python
    def cambiarTipoCliente(self, nuevoTipoCliente):
        self.tipoCliente = nuevoTipoCliente
```
Aqui simplemente **implemente el metodo** `cambiarTipoCliente` el cual recibe como parametro el nuevo tipo de cliente y **lo actualiza**.

Por ultimo nos pide modificar el metodo  **retirar monto** para que cada vez que se haga un retiro de dinero a este **se le agrege pequeño porcentaje por el cobro** de la trassaccion
```python
    def retirarMonto(self, monto):
        precioRetiro = monto * 0.01
        retiro = monto + precioRetiro
        self.saldo -= retiro
        return self.saldo
```
Simplemente tube que **modificar**  los atributos para que se ajusten a estos **criterios**, primeramente recibe el **monto** de retiro como parametro y con este **calcula** el porcentaje que se cobrara por el retiro despues los suma y por ultimo resta .este valor al saldo actual de la cuenta


# ***GRACIAS!.***
## POR Nicolas Bastidas
