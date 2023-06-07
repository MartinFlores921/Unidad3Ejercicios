from ManejaHelado import ManejaHelados as MH
from ManejaSabores import ManejaSabores as MS
from Menu import menuOpciones

listasabores = MS ()
listasabores.cargarSabores()
listahelados = MH()
menu = menuOpciones()
menu.opciones(listasabores,listahelados)