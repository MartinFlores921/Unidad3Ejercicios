
from claseColeccion import Coleccion
if __name__ == "__main__":
    dimension= int(input("Ingrese la Cantidad de Empleados para Almacenar \n"))
    manejador= Coleccion(dimension)
    manejador.initColeccion(dimension)
    print("\n")
    manejador.mostrarEmpleados()
    print("INCISO 1")
    dni= input("Ingrese el Dni de un Empleado: \n")
    manejador.buscar(dni)
   # manejador.mostrarContratados()
    print("INCISO 2")
    tarea= input("Ingrese una Tarea \n")
    manejador.buscarTarea(tarea)
    print("INCISO 3")
    manejador.ayuda()
    print("INCISO 4")
    manejador.sueldo()
    """Lote de Prueba
   dimension= 8, ya que son esos los empleados que se encuentra entre los 3 archivos csv(planta, exteros, contratados)
   dni= 12345678
   hs= 50
   Antes de la Actualizacion el Dni 12345678 tenia 160 hs trabajadas, luego me deberia mostrar 210hs
   
   """