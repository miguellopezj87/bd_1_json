from beautifultable import BeautifulTable
from Persona import Persona
from DAO import DAO
from os import system
import json
import os

class Funciones():

    d = DAO()

# ---------------------------------------------------------------------

    def __init__(self):
        pass

# ---------------------------------------------------------------------

    def menu(self):
        while True:
            try:
                system("cls")
                print("\n--- MENU ---")
                print("1.Agregar Persona")
                print("2.Listar Personas (Campos)")
                print("3.Listar Personas (Diccionario)")
                print("4.Buscar Persona")
                print("5.Eliminar Persona")
                print("6.Actualizar Datos")
                print("7.Salir")
                op = int(input("Digite Una Opcion : "))
                if op!=1 and op!=2 and op!=3 and op!=4 and op!=5 and op!=6 and op!=7:
                    print("\n--- Error De Opcion De Menu!! ---")
                    system("pause")
                else:
                    if op==1:
                        self.__registrar()
                    elif op==2:
                        self.__listarPersonasCampos()
                    elif op==3:
                        self.__listarPersonasDiccionario()
                    elif op==4:
                        self.__buscarPersona()
                    elif op==5:
                        self.__eliminarPersona()
                    elif op==6:
                        self.__actualizarDatos()
                    elif op==7:
                        self.__salir()
                        os._exit(1)
            except:
                print("\n--- Error De Opcion Try!! ---")
                system("pause")

# ---------------------------------------------------------------------

    def __registrar(self):
        pass

# ---------------------------------------------------------------------

    def __listarPersonasCampos(self):
        pass

# ---------------------------------------------------------------------

    def __listarPersonasDiccionario(self):
        pass

# ---------------------------------------------------------------------

    def __buscarPersona(self):
        pass

# ---------------------------------------------------------------------

    def __eliminarPersona(self):
        pass

# ---------------------------------------------------------------------

    def __actualizarDatos(self):
        pass

# ---------------------------------------------------------------------

    def __salir(self):
        system("cls")
        print("\n-------------------")
        print("--- Ok. Adios!! ---")
        print("-------------------")
        system("pause")
