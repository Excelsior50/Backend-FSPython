from flask import jsonify
import mysql.connector

#Establecer la Conexion
def get_db_connection():
    connection = mysql.connector.connect(user='root', 
                                         password='', 
                                         host='127.0.0.1', 
                                         database='tiendita_db')
    return connection

