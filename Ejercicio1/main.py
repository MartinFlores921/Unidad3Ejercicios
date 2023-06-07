from manejadorFacutades import manejadorF
from Menu import menudeOpciones


listaFacultades = manejadorF()
listaFacultades.cargarLista()
#listaFacultades.mostrarFacultades()
menu = menudeOpciones() 
menu.opciones(listaFacultades)