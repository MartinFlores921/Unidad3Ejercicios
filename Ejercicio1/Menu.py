class menudeOpciones:
    def __init__(self):
        self.__opcion = 0

    def opciones(self,lista):
        while self.__opcion != 3:
            print("Menu de opciones: ")
            print("1)- Mostrar nombre de facultad y duracion de cada una de sus carreras ")
            print("2)- Mostrar datos de una facultad dado el nombre de una carrera")
            print("3)- Salir")
            self.__opcion = int(input("Ingrese una opcion: "))
            
            if self.__opcion == 1:
                ingcod = str(input("Ingrese el codigo de facultad: "))
                print(ingcod)
                lista.mostrarDuraciones(ingcod)

            elif self.__opcion == 2:
                nomcar = str(input("Ingrese el nombre de una carrera para ver los datos de su facultad: "))
                lista.verDatos(nomcar)   

            else: 
                print("Opcion incorrecta, vuelva a ingresar ")
