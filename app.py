from flask import Flask, render_template,jsonify, request, redirect, url_for
from database.connect_db import get_db_connection
from flask_cors import CORS
import json
"""
# Directorio del archivo actual
base_dir = os.path.dirname(os.path.abspath(__file__))

# Configuración del directorio de plantillas y estáticos
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

# Verificación de la existencia del archivo index.html
index_file_path = os.path.join(template_dir, 'index.html')
if not os.path.exists(index_file_path):
    raise FileNotFoundError(f"El archivo {index_file_path} no existe. Por favor, verifica la ruta y el archivo.")

#Importar Views
from components.view_web import *
"""
app = Flask(__name__) #, template_folder=template_dir, static_folder=static_dir)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

from database.request import productos

@app.route('/')
def mostrar():
    datos = productos()
    return jsonify(datos)

@app.route('/add_contact', methods=['POST'])
def add_contact():
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
        
        return 'Creación exitosa.'

if __name__ == '__main__':

    app.run() #host='127.0.0.1', port=3000, debug=True

