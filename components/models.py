#Clases que corresponden a entidades de la BBDD
from database.dml import Tabla
from database.connect_db import connect as con 

class Product(Tabla):
    tabla = 'Product'
    campos = ('id', 'name')
    connect = con
    #Devuelve tupla
    
    #Convierto tupla a objeto
    def __init__(self, valores):
        super().crear(valores)