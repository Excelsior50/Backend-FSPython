from database.connect_db import get_db_connection

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