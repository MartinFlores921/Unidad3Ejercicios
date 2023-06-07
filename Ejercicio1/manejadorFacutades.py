import csv
from claseCarrera import Carrera
from claseFacultad import Facultad

class controlFacultades:
    __listaFacultades = []
    def __init__(self):
        self.__listaFacultades = []

    def cargarLista(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        facul = None
        for fila in reader:
            if len(fila)==5:
                codigo = str(fila[0])
                nombre = str(fila[1])
                direccion = str(fila[2])
                localidad = str(fila[3])
                telefono = str(fila[4])
                facultad = Facultad(codigo, nombre, direccion, localidad, telefono)
                self.__listaFacultades.append(facultad)

            elif len(fila)==6:
                cod = str(fila[1])
                nombre = str(fila[2])
                fechain = str(fila[3])
                duracion = str(fila[4])
                titulo = str(fila[5])
                carrera = Carrera(cod, nombre, fechain, duracion, titulo)
                facultad.addCarrera(carrera)

        archivo.close
        return self.__listaFacultades
            

    def mostrarFacultades(self):
        for facultad in self.__listaFacultades:
            print(facultad)


    def mostrarDuraciones(self, cod):
        print(self.__listaFacultades[(int(cod))-1].getNombre())
        self.__listaFacultades[(int(cod))-1].FacultadDuraciones()
        print("Se han mostrado todas las carreras")

    def verificarCodigo(self,cod):
        i = 0
        while i<(len(self.__listaFacultades)) and i != (int(cod)-1):
            i+=1
        if i == len(self.__listaFacultades):
            i = None
        return i
    
    def getDimension(self):
        return len(self.__listaFacultades)
    
    def verDatos(self, nomcar):
        for facultad in self.__listaFacultades:
            facultad.buscarCarrera(nomcar)