class Empleado:
    __dni: str
    __nombre: str
    __direccion: str
    __telefono: str
    
    def __init__(self, dni, nom, direc, tele):
        self.__dni= dni
        self.__nombre= nom
        self.__direccion = direc
        self.__telefono= tele
        
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def CalculoSueldo(self):
        pass
    
    def mostrar(self):
        return f"Nombre del Empleado: {self.__nombre}, Dni: {self.__dni}, Direccion: {self.__direccion}, Telefono: {self.__telefono}"
    
    