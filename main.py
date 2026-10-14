from agenda import Agenda
from contacto import Contacto

mi_agenda = Agenda()

contacto_1 = Contacto("Diego", "12345678")

exito = mi_agenda.agregar_contacto(contacto_1)
print("¿Se pudo agregar?", exito)

exito_duplicado = mi_agenda.agregar_contacto(contacto_1)
print("¿Dejó agregar duplicado?", exito_duplicado)