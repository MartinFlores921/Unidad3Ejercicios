from claseEmpleado import Empleado

class Externo(Empleado):
    __tarea: str
    __fechaI: str
    __fechaF: str
    __montoViatico: int
    __costoObra: int
    __montoSeguro: int
    
    def __init__(self, dni, nombre, direccion, telefono, tar, fi, ff, mv, co, ms):
        super().__init__(dni,nombre, direccion, telefono)
        self.__tarea= tar
        self.__fechaI= fi
        self.__fechaF = ff
        self.__montoViatico= mv
        self.__costoObra= co
        self.__montoSeguro= ms
    
    def getTarea(self):
        return self.__tarea
    def getFechaI(self):
        return self.__fechaI
    def getFechaF(self):
        return self.__fechaF
    def getmontoViatico(self):
        return self.__montoViatico
    def getcostoObra(self):
        return self.__costoObra
    def getmontoSeguro(self):
        return self.__montoSeguro
    def CalculoSueldo(self):
        sueldo = self.__costoObra - self.__montoViatico - self.__montoSeguro
        return sueldo
    def mostrar(self):
        print("Empleado Externo \n")
        print( f"{super().mostrar()}")
        print("Tarea: {}, FechaI: {}, FechaF: {}, MontoViatico:{}, CostoObra:{}, MontoSeguro:{}".format(self.__tarea, self.__fechaI, self.__fechaF, self.__montoViatico, self.__costoObra, self.__montoSeguro))