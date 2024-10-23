from flask import Flask, jsonify
from database.connect_db import get_db_connection
from flask_cors import CORS
from database.request import *

#Importar Views
from components.view_web import view_web

app = Flask(__name__) #, template_folder=template_dir, static_folder=static_dir)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})  
# Permitir CORS solo para este origen

##### FORMULARIO MODIFICACION Y ELIMINACION DE CONSULTA FORM
# Registrar el Blueprint
app.register_blueprint(view_web)

@app.route('/')
def mostrar():
    datos = productos()
    return jsonify(datos)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    add = addCont() #Modularizo en request y devuelvo 201 
    return add
        
if __name__ == '__main__':

    app.run(debug=True) #host='127.0.0.1', port=3000, debug=True
