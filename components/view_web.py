from flask import Blueprint, request, jsonify
from database.request import buscar_usuario_db, eliminar_contact, modificar_contact
import json

# Crear un Blueprint
view_web = Blueprint('view_web', __name__)

# Ruta para mostrar el formulario de búsqueda y resultados
@view_web.route('/buscar', methods=['POST'])
def buscar_usuario_por_email():
    try:
        data = request.get_json()
        if not data or 'email' not in data:
            raise ValueError("Datos de solicitud no válidos o 'email' faltante")
        
        email = data['email']
        resultados = buscar_usuario_db(email)
        print(f"Resultados encontrados view_db: {resultados}")  # Mensaje de depuración
        return jsonify(resultados)
    except Exception as e:
        print(f"Error al buscar usuario: {e}")  # Mensaje de depuración
        return jsonify({'error': str(e)}), 500

# Ruta para eliminar un usuario por email
@view_web.route('/eliminar', methods=['POST'])
def eliminar_usuario():
    try:
        data = request.get_json()
        id = data['id']
        eliminar_contact(id)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para modificar un usuario
@view_web.route('/modificar', methods=['POST'])
def modificar_usuario():
    try:
        data = request.get_json()
        id = data['id']
        nombre = data['nombre']
        email = data['email']
        numeroTelefono = data['numeroTelefono']
        mensaje = data['mensaje']
        print(f"ID RECIBIDO PARA MODIFICAR: {id}")  # Mensaje de depuración
        modificar_contact(id, nombre, email, numeroTelefono, mensaje)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


"""#Rutas de la app
@app.route('/')
def home():    
    return render_template('index.html')

@app.route('/site/contacto')
def contacto():
    return render_template('site/contacto.html')

@app.route('/site/inicioSesion')
def inicioSesion():
    return render_template('site/inicioSesion.html')

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
    """