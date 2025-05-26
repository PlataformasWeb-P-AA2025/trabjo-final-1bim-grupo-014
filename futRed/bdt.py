#Usuario
#Publicacion
#Reaccion (como tabla intermedia)
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)
	
Base = declarative_base()

class Reaccion(Base):
    __tablename__ = 'reaccion'
    usuario_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    publicacion.id = Column(Integer, ForeignKey('publicacion.id'), primary_key=True)
    
    #modulo = relationship("Modulo", back_populates="estudiantes")
    #estudiante = relationship("Estudiante", back_populates="modulos")
    tipo_emocion = 

    def __repr__(self):
        return "Matricula: estudiante=%s\n modulo=%s\n"% (
                          self.estudiante,
                          self.modulo)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    #apellido = Column(String(50))
    
    modulos = relationship("Reaccion", back_populates="usuario")

    def __repr__(self):
        return "Usuario: nombre=%s - apellido=%s"% (
                          self.nombre,
                          self.apellido)

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    #nombre = Column(String(50))
    estudiantes = relationship("Matricula", back_populates="modulo")

    def __repr__(self):
        return "Modulo: nombre=%s"% (
                          self.nombre)



Base.metadata.create_all(engine)