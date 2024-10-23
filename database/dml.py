from flask import render_template, request, redirect, url_for
from database.connect_db import get_db_connection
from app import app

print('entro')

# Ruta para manejar la creación o actualización de un contacto
@app.route('/add_contact', methods=['POST'])
def add_contact():
        connection = get_db_connection()
        try:
            cursor = connection.cursor(dictionary = True)
        except Exception: 
            connection.connect()
            cursor = connection.cursor(dictionary = True)

        nombre = request.form['nombre']
        email = request.form['email']
        numeroTelefono = request.form['numeroTelefono']
        dni = request.form['dni']
        armadoPC = 'armadoPC' in request.form
        actHard = 'ActHard' in request.form
        actSoft = 'ActSoft' in request.form
        otros = 'otros' in request.form
        perfil = request.form['turno']
        mensaje = request.form['mensaje']
        
        # Inserta un nuevo contacto
        insert_query = """
                INSERT INTO Contacts (Name, Email, Phone, DNI, ArmadoPC, ActHard, ActSoft, Otros, Profile, Message)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        cursor.execute(insert_query, (nombre, email, numeroTelefono, dni, armadoPC, actHard, actSoft, otros, perfil, mensaje))

        connection.commit()
        return redirect(url_for('form'))
