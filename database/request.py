from flask import request, redirect, render_template, url_for
from database.connect_db import get_db_connection
import json

def productos():
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary = True)
    except Exception: 
        connection.connect()
        cursor = connection.cursor(dictionary = True)
    
    cursor.execute("select * from products;")
    datos = cursor.fetchall()
    connection.close()
    return datos #MODELO ARQUITECTURA API-REST
    #return render_template('site/productos.html', datos=datos) #PATRON MVC
 
#Agrega contacto a db    
def addCont():
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary = True)
    except Exception: 
        connection.connect()
        cursor = connection.cursor(dictionary = True)
        
    raw_data = request.get_data()
    json_data = raw_data.decode('utf-8')
    data = json.loads(json_data)
        
    nombre = data.get('nombre')
    email = data.get('email')
    numeroTelefono = data.get('numeroTelefono')
    mensaje = data.get('mensaje')
        
    # Inserta un nuevo contacto
    insert_query = """
            INSERT INTO Contacts (nombre, email, numeroTelefono, mensaje)
            VALUES (%s, %s, %s, %s)
        """
    cursor.execute(insert_query, (nombre, email, numeroTelefono, mensaje))
    connection.commit()
    connection.close()
        
    return 201

# Mostrar el formulario de búsqueda y resultados por EMAIL
def buscar_usuario_db(email):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary = True)
    except Exception: 
        connection.connect()
        cursor = connection.cursor(dictionary = True)
        
    query = "SELECT * FROM contacts WHERE email = %s"
    print(f"Ejecutando consulta SQL: {query} con email = {email}")  # Mensaje de depuración
    cursor.execute(query, (email,))
    resultados = cursor.fetchall()
    cursor.close()
    connection.close()
    return resultados

# Eliminar un usuario por email
def eliminar_usuario(email):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary = True)
    except Exception: 
        connection.connect()
        cursor = connection.cursor(dictionary = True)
    query = "DELETE FROM contacts WHERE email = %s"
    cursor.execute(query, (email,))
    connection.commit()
    cursor.close()
    connection.close()


# Moodificar un usuario
def modificar_usuario(email, nombre, numeroTelefono, mensaje):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary = True)
        query = """
        UPDATE contacts 
        SET nombre = %s, numeroTelefono = %s, mensaje = %s 
        WHERE email = %s
        """
        print(f"Ejecutando consulta SQL: {query} con email = {email}")
        cursor.execute(query, (nombre, numeroTelefono, mensaje, email))    
        connection.commit()
    except Exception: 
        connection.connect()
        cursor = connection.cursor(dictionary = True)
        
    cursor.close()
    connection.close()
