from claseEmpleado import Empleado

class Planta(Empleado):
    __sueldoBasico: int
    __antiguedad: str
    
    def __init__(self,dni, nombre, direccion, telefono, sueldoB, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico= sueldoB
        self.__antiguedad = antiguedad
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    def getAntiguedad(self):
        return self.__antiguedad
    
    def CalculoSueldo(self):
        sueldo= self.__sueldoBasico + ((self.__sueldoBasico*0.01) * int(self.__antiguedad))
        return sueldo
    def mostrar(self):
        print("Empleado Planta \n")
        print(f"{super().mostrar()}")
        print("SueldoBasico:{}, Antiguedad: {}".format(self.__sueldoBasico, self.__antiguedad))