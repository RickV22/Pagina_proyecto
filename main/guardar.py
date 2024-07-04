from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos (ajusta según tus credenciales)
db_config = {
    'host': 'localhost',
    'user': 'user',
    'password': '123',
    'database': 'monitorias'
}

# Función para conectarse a la base de datos
def conectar_bd():
    return mysql.connector.connect(**db_config)

# Ruta para guardar una nueva postulación
@app.route('/guardar_postulacion', methods=['POST'])
def guardar_postulacion():
    # Recibir datos del formulario
    data = request.get_json()
    nombre = data['nombre']
    tipo_documento = data['tipo_documento']
    correo = data['correo']
    programa = data['programa']
    sede = data['sede']
    cuatrimestre = data['cuatrimestre']
    promedio = data['promedio']
    tipo_monitoria = data['tipo_monitoria']
    modulo = data['modulo'] if 'modulo' in data else None
    area = data['area'] if 'area' in data else None

    # Insertar datos en la base de datos
    try:
        conn = conectar_bd()
        cursor = conn.cursor()

        sql = """
            INSERT INTO postulaciones (nombre, tipo_documento, correo, programa, sede, cuatrimestre, promedio, tipo_monitoria, modulo, area)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nombre, tipo_documento, correo, programa, sede, cuatrimestre, promedio, tipo_monitoria, modulo, area))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Postulación enviada correctamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
