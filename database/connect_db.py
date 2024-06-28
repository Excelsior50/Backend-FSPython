from flask import jsonify
import mysql.connector

#Establecer la Conexion
def get_db_connection():
    connection = mysql.connector.connect(user='root', 
                                         password='', 
                                         host='127.0.0.1', 
                                         database='tiendita_db')
    return connection


"""
#Utilizar los datos
connection = get_db_connection()
cursor = connection.cursor(dictionary=True)
consulta = "SELECT * FROM contacts;"

cursor.execute(consulta)
datos = cursor.fetchall()
print(datos)
#Siempre cierro la conexion para evitar trafico a la db
connection.close()

"""

