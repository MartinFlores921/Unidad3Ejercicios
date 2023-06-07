class Empleado:
    __dni: set
    __nombre: str
    __direccion: str
    __telefono: str
    
    def __init__(self, dni, nom, dir, tel):
        self.__dni= dni
        self.__nombre= nom
        self.__direccion= dir
        self.__telefono= tel
    
    
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    
        