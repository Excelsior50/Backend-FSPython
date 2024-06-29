from flask import render_template, request, redirect, url_for
from database.connect_db import get_db_connection
from app import app

print('entro')

"""
# Ruta para mostrar el formulario de contacto
@app.route('/')
def form():
    print('entro')
    return render_template('form.html')
"""



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

# Comprueba si el contacto ya existe por DNI
#        cursor.execute("SELECT * FROM contacts WHERE DNI = %s", (dni,))
#        existing_contact = cursor.fetchone()
#
#        if existing_contact:
#            # Actualiza el contacto existente
#            update_query = """
#                UPDATE Contacts
#                SET Name = %s, Email = %s, Phone = %s, ArmadoPC = %s, ActHard = %s, ActSoft = %s, Otros = %s, Profile = %s, Message = %s
#                WHERE DNI = %s
#            """
#            cursor.execute(update_query, (nombre, email, numeroTelefono, armadoPC, actHard, actSoft, otros, perfil, mensaje, dni))
#        else:


# Ruta para mostrar los contactos
@app.route('/contacts')
def contacts():
    cursor.execute("SELECT * FROM Contacts")
    contacts = cursor.fetchall()
    return render_template('contacts.html', contacts=contacts)

# Ruta para eliminar un contacto por ID
@app.route('/delete_contact/<int:contact_id>')
def delete_contact(contact_id):
    cursor.execute("DELETE FROM Contacts WHERE ContactID = %s", (contact_id,))
    connection.commit()
    return redirect(url_for('contacts'))

# Ruta para eliminar un contacto por DNI
@app.route('/delete_contact_by_dni', methods=['POST'])
def delete_contact_by_dni():
    dni = request.form['dni']
    cursor.execute("DELETE FROM Contacts WHERE DNI = %s", (dni,))
    connection.commit()
    return redirect(url_for('contacts'))


"""class Tabla:
    
    # Constructor
    def __init__(self):
        pass
    
    # *** CRUD ***
    # Creador/"Constructor" de instancias de subclase
    def crear(self, valores):
        for campo,valor in zip(self.campo, valores):
            setattr(self, campo, valor)
        

    
    def guardar_db(self):
        pass
    
    # Lectura
    @classmethod 
    def obtener(cls):
        pass
    
    # Modificación
    @classmethod 
    def actualizar(cls):
        pass
    
    # Eliminación
    @classmethod 
    def eliminar(cls):
        pass
    
    # *** Método común en CRUD (encapsulado) ***
    @classmethod
    def __conectar(cls, consulta):
        
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.cursor()
            cursor = cls.conexion.cursor()
        
        cursor.execute(consulta)
        datos = cursor.fetchall()
        #Lista por comprension
        resultado = [cls(registro) for registro in datos]
        cls.conecion.close()
        
        return resultado    

from connect_db import cursor,connection

#--------CRUD------

# Create
insert_query = "INSERT INTO categories (ProductName, Brand) VALUES (%s, %s)"
category_data = ("Electronics", "Products related to electronic devices")
cursor.execute(insert_query, category_data)
connection.commit()  # Guarda los cambios en la base de datos

insert_query = "INSERT INTO products (CategoryName, Description) VALUES (%s, %s)"
product_data = ("Electronics", "Products related to electronic devices")
cursor.execute(insert_query, product_data)
connection.commit()  # Guarda los cambios en la base de datos

insert_query = "INSERT INTO suppliers (SupplierName, ContactName) VALUES (%s, %s)"
supplier_data = ("Electronics", "Products related to electronic devices")
cursor.execute(insert_query, supplier_data)
connection.commit()  # Guarda los cambios en la base de datos


# Read
select_query = "SELECT * FROM products"
cursor.execute(select_query)
products = cursor.fetchall()

for product in products:
    print(product)  # Aquí puedes procesar cada fila como desees


select_query = "SELECT * FROM suppliers"
cursor.execute(select_query)
suppliers = cursor.fetchall()

for supplier in suppliers:
    print(supplier)  # Aquí puedes procesar cada fila como desees


select_query = "SELECT * FROM Categories"
cursor.execute(select_query)
categories = cursor.fetchall()

for category in categories:
    print(category)  # Aquí puedes procesar cada fila como desees
    

# Update
update_query = "UPDATE Products SET UnitPrice = %s WHERE ProductID = %s"
new_price = 199.99
product_id = 1
cursor.execute(update_query, (new_price, product_id))
connection.commit()  # Guarda los cambios en la base de datos


# Delete
delete_query = "DELETE FROM Suppliers WHERE SupplierID = %s"
supplier_id = 1
cursor.execute(delete_query, (supplier_id,))
connection.commit()  # Guarda los cambios en la base de datos

"""