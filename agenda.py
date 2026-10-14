"""Clase agenda"""
from contacto import Contacto


class Agenda:
    def __init__(self):
        self.Contacto = {}

    def agregar_contacto(self, un_contacto: Contacto):
        if un_contacto.nombre not in self.Contacto:
            self.Contacto[un_contacto.nombre] = un_contacto
            return  True
        else:
            return False

    def buscar_contacto(self, nombre):
        if nombre in self.Contacto:
            contacto_encontrado = self.Contacto[nombre]
            return contacto_encontrado
        else:
            return "El contacto no esta en la agenda"
            

