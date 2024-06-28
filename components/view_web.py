from flask import Flask, render_template, jsonify
from app import app

from database.connect_db import get_db_connection


"""#Rutas de la app
@app.route('/')
def home():    
    return render_template('index.html')

@app.route('/site/contacto')
def contacto():
    return render_template('site/contacto.html')

@app.route('/site/inicioSesion')
def inicioSesion():
    return render_template('site/inicioSesion.html')"""

@app.route('/site/productos')
def productos():
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary = True)
    except Exception: 
        connection.connect()
        cursor = connection.cursor(dictionary = True)
    
    cursor.execute("select * from products;")
    datos = cursor.fetchall()
    
    #return jsonify(datos) #MODELO ARQUITECTURA API-REST
    return render_template('site/productos.html', datos=datos) #PATRON MVC

@app.route('/site/ProcesadoresAMC')
def ProcesadoresAMC():
    return render_template('site/ProcesadoresAMC.html')