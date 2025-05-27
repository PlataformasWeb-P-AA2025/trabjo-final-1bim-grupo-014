import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crear_tablas import Usuario, Publicacion, Reaccion


# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Crear una sesión
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Definimos los archivos con los cuales vamos a trabajar
archivo_usuarios = "../DATA/usuarios_red_x.csv"
archivo_publicaciones = "../DATA/usuarios_publicaciones.csv"
archivo_emociones = "../DATA/usuario_publicacion_emocion.csv"

 

#Cargamos los datos en la tabla Usuario
with open(archivo_usuarios, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombreUsuario = linea.strip()
        usuario = Usuario(nombre = nombreUsuario)
        session.add(usuario)
        

with open(archivo_publicaciones , "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo, delimiter='|')  # Usamos '|' como separador
    for fila in lector:
        usuario = fila['usuario'].strip()
        publicacion = fila['publicacion'].strip()

        # Buscar usuario por nombre
        usuario = session.query(Usuario).filter_by(nombre=usuario).first()
        userid = usuario.id
        
        publicacion = Publicacion(publicacion=publicacion, usuario_id=userid)
        session.add(publicacion)
   
      

with open(archivo_emociones, "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo, delimiter='|')  # Usamos '|' como separador
    for fila in lector:
        usuario = fila['Usuario'].strip()
        publicacion = fila['comentario'].strip()
        emocion = fila['tipo emocion'].strip()
    


        # Buscar usuario por nombre
        usuario = session.query(Usuario).filter_by(nombre=usuario).first()
        userid = usuario.id

        # Buscar publicacion por publicacion
        publicaciones = session.query(Publicacion).filter_by(publicacion=publicacion).first()
        publicacionesid = publicaciones.id
        
        reaccion = Reaccion(usuario_id= userid, publicacion_id=publicacionesid, tipo_emocion = emocion)
        session.add(reaccion)


session.commit()

session.close()

print("Datos guardados exitosamente")