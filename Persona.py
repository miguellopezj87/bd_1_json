class Persona:
    __id = 0
    __rut = ""
    __nombre = ""
    __apellido = ""
    __edad = 0

    def __init__(self):
        pass

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getRut(self):
        return self.__rut

    def setRut(self, rut):
        self.__rut = rut
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad
