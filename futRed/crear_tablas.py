
from configuracion import cadena_base_datos

# traemos la cadena de bd del archivo configuracion.py
engine = create_engine(cadena_base_datos)
	
Base = declarative_base()


# La tabla reaccion tiene una conexion con usuario y publicacion
# los unimos con el nombre de usuario y comentario
# y se le agrega el campo tipo_emocion
class Reaccion(Base):
    __tablename__ = 'reaccion'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    publicacion.id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)
    tipo_emocion = Column(String(50), nullable=False)
    usuario = relationship("Usuario", back_populates="comentario")
    comentario = relationship("Publicacion", back_populates="usuario")
    

    def __repr__(self):
        return "Reaccion: usuario=%s\n publicacion=%s\n emocion=%s\n"% (
                          self.usuario,
                          self.comentario,
                          self.tipo_emocion)


# La tabla usuario tiene el nombre de usuario y se le agrega la conexion
# con la tabla reaccion
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    comentario = relationship("Reaccion", back_populates="usuario")

    def __repr__(self):
        return "Usuario: %s "% (
                          self.nombre)


# La tabla publicacion tiene el campo publicacion y se le agrega la conexion
# con la tabla reaccion
class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    publicacion = Column(String(500))
    usuario = relationship("Reaccion", back_populates="publicacion")

    def __repr__(self):
        return "Publicacion: %s"% (
                          self.publicacion)



Base.metadata.create_all(engine)


