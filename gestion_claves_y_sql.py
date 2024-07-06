from cryptography.fernet import Fernet
import sqlite3
import os

# Función para generar una clave y guardarla en un archivo
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Función para cargar la clave desde un archivo
def cargar_clave():
    return open("clave.key", "rb").read()

# Función para encriptar un mensaje
def encriptar_mensaje(mensaje):
    clave = cargar_clave()
    fernet = Fernet(clave)
    mensaje_encriptado = fernet.encrypt(mensaje.encode())
    return mensaje_encriptado

# Función para desencriptar un mensaje
def desencriptar_mensaje(mensaje_encriptado):
    clave = cargar_clave()
    fernet = Fernet(clave)
    mensaje_desencriptado = fernet.decrypt(mensaje_encriptado).decode()
    return mensaje_desencriptado

# Función para crear una base de datos y una tabla
def crear_base_datos():
    conexion = sqlite3.connect('datos.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                     (id INTEGER PRIMARY KEY, nombre TEXT, mensaje_encriptado TEXT)''')
    conexion.commit()
    conexion.close()

# Función para insertar un usuario en la base de datos
def insertar_usuario(nombre, mensaje):
    conexion = sqlite3.connect('datos.db')
    cursor = conexion.cursor()
    mensaje_encriptado = encriptar_mensaje(mensaje)
    cursor.execute("INSERT INTO usuarios (nombre, mensaje_encriptado) VALUES (?, ?)",
                   (nombre, mensaje_encriptado))
    conexion.commit()
    conexion.close()

# Función para obtener y desencriptar mensajes de la base de datos
def obtener_mensajes():
    conexion = sqlite3.connect('datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, mensaje_encriptado FROM usuarios")
    filas = cursor.fetchall()
    for fila in filas:
        nombre, mensaje_encriptado = fila
        mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado)
        print(f"Nombre: {nombre}, Mensaje: {mensaje_desencriptado}")
    conexion.close()

# Generar y guardar una clave si no existe
if not os.path.exists("clave.key"):
    generar_clave()

# Crear la base de datos y la tabla si no existe
crear_base_datos()

# Insertar un usuario y su mensaje encriptado
insertar_usuario("Carlos", "Este es un mensaje secreto")

# Obtener y mostrar los mensajes desencriptados
obtener_mensajes()
