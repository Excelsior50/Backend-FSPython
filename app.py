from flask import Flask, render_template,jsonify
import os
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

from database.request import productos

@app.route('/')
def mostrar():
    datos = productos()
    return jsonify(datos)

if __name__ == '__main__':

    app.run() #host='127.0.0.1', port=3000, debug=True

