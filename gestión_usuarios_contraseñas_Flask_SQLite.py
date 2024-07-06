from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Función para generar una clave y guardarla en un archivo
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Función para cargar la clave desde un archivo
def cargar_clave():
    return open("clave.key", "rb").read()

# Crear la base de datos y la tabla si no existe
def crear_base_datos():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                     (id INTEGER PRIMARY KEY, nombre TEXT, contraseña_hash TEXT)''')
    conexion.commit()
    conexion.close()

# Función para insertar un usuario en la base de datos
def insertar_usuario(nombre, contraseña):
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    contraseña_hash = generate_password_hash(contraseña)
    cursor.execute("INSERT INTO usuarios (nombre, contraseña_hash) VALUES (?, ?)",
                   (nombre, contraseña_hash))
    conexion.commit()
    conexion.close()

# Función para validar un usuario
def validar_usuario(nombre, contraseña):
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT contraseña_hash FROM usuarios WHERE nombre=?", (nombre,))
    fila = cursor.fetchone()
    conexion.close()
    if fila is None:
        return False
    contraseña_hash = fila[0]
    return check_password_hash(contraseña_hash, contraseña)

@app.route('/registrar', methods=['POST'])
def registrar():
    data = request.get_json()
    nombre = data.get('nombre')
    contraseña = data.get('contraseña')
    insertar_usuario(nombre, contraseña)
    return jsonify({"mensaje": "Usuario registrado exitosamente"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nombre = data.get('nombre')
    contraseña = data.get('contraseña')
    if validar_usuario(nombre, contraseña):
        return jsonify({"mensaje": "Inicio de sesión exitoso"})
    else:
        return jsonify({"mensaje": "Nombre de usuario o contraseña incorrectos"}), 401

if __name__ == '__main__':
    if not os.path.exists("clave.key"):
        generar_clave()
    crear_base_datos()

    # Agregar usuarios iniciales
    usuarios_iniciales = [
        ("Sebastian Aviles", "cisco"),
        ("Salomon Vergara", "cisco"),
        ("Carlos Hernández", "cisco")
    ]

    for nombre, contraseña in usuarios_iniciales:
        insertar_usuario(nombre, contraseña)

    app.run(host='0.0.0.0', port=5800)
