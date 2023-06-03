from claseEmpleado import Empleado
class Contratado(Empleado):
    __fechaInicio: str
    __fechaFinalizacion: str
    __cantHs:int
    __valorPorHora = 10000 #variable de clase
    
    def __init__(self, dni, nombre, direccion, telefono, fechaI, fechaf, cant):
        super().__init__(dni,nombre,direccion, telefono)
        self.__fechaInicio= fechaI
        self.__fechaFinalizacion= fechaf
        self.__cantHs= cant
    
    
    @classmethod
    def getValorPorHora(cls):
        return cls.__valorPorHora
    
    def getfechaInicio(self):
        return self.__fechaInicio
    
    def getfechaFinalizacion(self):
        return self.__fechaFinalizacion
    
    def getcantHs(self):
        return self.__cantHs
    def setHoras(self,hs):
        self.__cantHs +=hs
    def CalculoSueldo(self):
        sueldo=0
        sueldo= self.__cantHs * self.__valorPorHora
        return sueldo
    def mostrar(self):
        print("Empleado Contratado \n")
        print(f"{super().mostrar()}") #utilizo la funcion super para mostrar los datos de la clase padre Empleado
        print("Fecha de Inicio: {}, Fecha de Finalizacion: {}, CantHs: {}, ValorPorHora:{}".format(self.__fechaInicio, self.__fechaFinalizacion, self.__cantHs, self.__valorPorHora))
    
    
    
        
    
    