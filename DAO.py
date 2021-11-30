from Persona import Persona
import json
from os import system
import pymysql

class DAO:

    def __init__(self):
        pass

# ---------------------------------------------------------------------

    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost", 
            user = "root",
            password = "",
            db = "bd1_json"
        )
        self.cursor = self.con.cursor()

# ---------------------------------------------------------------------

    def desconectar(self):
        self.con.close()

# ---------------------------------------------------------------------
    