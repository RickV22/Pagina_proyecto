import mysql.connector as sql
from flask import session
import bcrypt
import secrets
import string

import json

def obtener_postulaciones():
    try:
        # Configuración de la conexión a la base de datos (ajusta según tus credenciales)
        connection = mysql.connector.connect(
            host='localhost',
            database='gestion_monitorias',
            user='root',
            password='',
            port='3306'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            # Consulta SQL para obtener las postulaciones
            sql_query = "SELECT * FROM postulaciones"
            cursor.execute(sql_query)
            postulaciones = cursor.fetchall()

            # Convertir a formato JSON
            postulaciones_json = json.dumps(postulaciones, default=str)
            print(postulaciones_json)  # Imprimir el resultado JSON
            
    except Error as e:
        print("Error al conectar con MySQL:", e)
    finally:
        # Cerrar la conexión si está abierta
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    obtener_postulaciones()
