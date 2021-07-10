#!/usr/bin/python3

class Persona:
    def __init__(self, entidad_federativa, municipio):
        self.entidad_federativa = entidad_federativa
        self.municipio = municipio


class PersonaFisica(Persona):
    def __init__(self, entidad_federativa, municipio, nombre):
        super().__init__(entidad_federativa, municipio)
        self.nombre = nombre

    def __str__(self):
        return "Nombre: " + self.nombre + "\tEntidad federativa: " + self.entidad_federativa + "\tMunicipio: " + self.municipio