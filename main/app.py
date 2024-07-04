from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector
from mysql.connector import Error

def connect():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='gestion_monitorias',
            user='root',
            password='',
            port='3306'
        )
        
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado a MySQL Server versión ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a la base de datos: ", record)
            cursor.execute("SELECT * FROM Usuarios;")
            rows = cursor.fetchall()
            print("Usuarios:")
            for row in rows:
                print(row)

    except Error as e:
        print("Error al conectar a MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

if __name__ == "__main__":
    connect()
