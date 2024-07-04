from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)
app.secret_key = 'secret'

def obtener_conexion():
    return mysql.connector.connect(
        host='localhost',
        database='gestion_monitorias',
        user='root',
        password='',
        port='3306'
    )


@app.route('/')
def inicio():
    if 'loggedin' in session:
        return 'Bienvenido, ' + session['usuario'] + '!'
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'usuario' in request.form and 'contrasena' in request.form:
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        conexion = obtener_conexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute('SELECT * FROM Usuarios WHERE usuario = %s AND contrasena = %s', (usuario, contrasena))
        cuenta = cursor.fetchone()

        if cuenta:
            session['loggedin'] = True
            session['id'] = cuenta['id']
            session['usuario'] = cuenta['usuario']
            return redirect(url_for('inicio'))
        else:
            return 'Nombre de usuario/contraseña incorrectos'
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('usuario', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
