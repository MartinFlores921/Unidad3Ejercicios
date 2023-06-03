import numpy as np
from claseEmpleado import Empleado
from claseExterno import Externo
from clasePlanta import Planta
from claseContratado import Contratado
import csv
class Coleccion:
    __dimension:int
    __cantidad: int
    __incremento=5
    
    
    def __init__(self,dimension):
        self.__empleados= np.empty(dimension, dtype=Empleado)
        self.__dimension= dimension
        self.__cantidad= 0
    
    def agregarEmpleado(self,empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad]= empleado
        self.__cantidad +=1
    
    def agregarContratado(self):
        archivo= open("contratados.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            unContratado= Contratado(fila[0], fila[1], fila[2] , fila[3], (fila[4]), (fila[5]), int(fila[6]))
            self.agregarEmpleado(unContratado)
        archivo.close()
        
    def agregarExterno(self):
        archivo= open("externos.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            unExterno= Externo(fila[0],fila[1],fila[2],fila[3],fila[4], fila[5], fila[6], int(fila[7]), int(fila[8]), int(fila[9]))
            self.agregarEmpleado(unExterno)
        archivo.close()
    
    def agregarPlanta(self):
        archivo= open("planta.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            unaPlanta= Planta(fila[0],fila[1], fila[2],fila[3],int(fila[4]), fila[5])
            self.agregarEmpleado(unaPlanta)
        
    def setDimension(self,dimension):
        self.__dimension = dimension
        
    def initColeccion (self, dimension): #Cargo el Arreglo Empleado con los 3 tipos de Empleados dada la dimension
        self.setDimension(dimension) #Modifico el atributo dimension a partir de la dimension ingresada por teclado
        self.agregarContratado()
        self.agregarExterno()
        self.agregarPlanta()
    
    
    def mostrarEmpleados(self):
        i=0
        for emp in self.__empleados:
            if isinstance(emp,Empleado):
                #print("Los Empleados Cargados son: \n")
                print(emp.mostrar())
                
    
    def buscar(self, dni):
        i=0
        hs= int(input("Ingrese la Cantidad de Horas para Acumular: \n"))
        while i < len(self.__empleados):
            if isinstance(self.__empleados[i], Contratado): 
                if self.__empleados[i].getDni() == dni:
                   self.__empleados[i].setHoras(hs)
                   print("Horas Actualizadas")
                   print("Los Datos de los Empleados contratados son: \n")
                   print(self.__empleados[i].mostrar())
                i+=1
            i+=1
    
    def buscarTarea(self,tarea):
        i=0
        acum=0
        while i < len(self.__empleados):
            if isinstance(self.__empleados[i], Externo):
                if self.__empleados[i].getTarea() == tarea:
                    acum+= self.__empleados[i].getmontoViatico() + self.__empleados[i].getcostoObra() + self.__empleados[i].getmontoSeguro()
                    print("El Total a pagar para la Tarea {} es: {}".format(tarea, acum))
                i+=1
            i+=1
    
    def ayuda(self):
        print("Los Empleados que necesitan la Ayuda Economica son: \n")
        i=0
        while i < (len(self.__empleados)):
            if self.__empleados[i] != None:
                 if self.__empleados[i].CalculoSueldo() < 150000:
                    print("Nombre:{}, Direccion: {}, Dni: {}".format(self.__empleados[i].getNombre(),self.__empleados[i].getDireccion(), self.__empleados[i].getDni()))
                 i+=1
            i+=1
    
    def sueldo(self):
        i=0
        while i < len(self.__empleados):
            if self.__empleados[i] != None:
                sueldo= self.__empleados[i].CalculoSueldo()
            print("Nombre:{}, Telefono:{}, Sueldo:{}".format(self.__empleados[i].getNombre(), self.__empleados[i].getTelefono(), sueldo))
            i+=1
        
        
                    
                

            
    