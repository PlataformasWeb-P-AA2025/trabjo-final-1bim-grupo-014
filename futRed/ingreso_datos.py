from sqlalchemy.orm import sessionmaker
from crear_tablas import Reaccion, Usuario, Publicacion

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Definimos los archivos con los cuales vamos a trabajar
archivo_usuarios = "../DATA/usuarios_red_x.csv"
archivo_publicaciones = "../DATA/usuarios_publicaciones.csv"
archivo_emociones = "../DATA/usuario_publicacion_emocion.csv"

#Cargamos los datos en la tabla Usuario
with open(archivo_usuarios, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombreUsuario = linea.strip().split(";")
        usuario = Usuario(nombre=nombreUsuario)
        session.add(usuario)

session.commit()

session.close()

print("Datos guardados exitosamente")