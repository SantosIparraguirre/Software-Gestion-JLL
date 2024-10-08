from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import datetime

# Crear la base de datos
Base = declarative_base()

# Crear el motor de la base de datos SQLite
engine = create_engine('sqlite:///database.db')

# Crear una sesión
Session = sessionmaker(bind=engine)

# Variable de sesión para interactuar con la base de datos
session = Session()

# Crear la clase de la tabla de productos
class Productos(Base):
    __tablename__ = 'PRODUCTOS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_categoria = Column(Integer, ForeignKey('CATEGORIAS.id'))
    codigo = Column(String)
    linea = Column(String)
    nombre = Column(String)
    precio = Column(Float)
    categoria = relationship('Categorias', back_populates='productos')

# Crear la clase de la tabla de categorías
class Categorias(Base):
    __tablename__ = 'CATEGORIAS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    productos = relationship('Productos', back_populates='categoria')

# Crear la clase de la tabla de clientes
class Clientes(Base):
    __tablename__ = 'CLIENTES'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    cuit = Column(String)
    telefono = Column(String)
    direccion = Column(String)
    presupuestos = relationship('Presupuestos', back_populates='cliente')
    remitos = relationship('Remitos', back_populates='cliente')
    acopios = relationship('Acopios', back_populates='cliente')

# Presupuestos
class Presupuestos(Base):
    __tablename__ = 'PRESUPUESTOS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey ('CLIENTES.id'), nullable=False)
    fecha = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    total = Column(Float)
    cliente = relationship('Clientes', back_populates='presupuestos')
    detalles = relationship('DetallesPresupuestos', back_populates='presupuesto')

# Detalles de presupuestos
class DetallesPresupuestos(Base):
    __tablename__ = 'DETALLES_PRESUPUESTOS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_presupuesto = Column(Integer, ForeignKey ('PRESUPUESTOS.id'), nullable=False)
    producto = Column(String)
    cantidad = Column(Float)
    precio_unitario = Column(Float)
    descuento = Column(Float)
    total = Column(Float)
    presupuesto = relationship('Presupuestos', back_populates='detalles')

# Remitos
class Remitos(Base):
    __tablename__ = 'REMITOS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey ('CLIENTES.id'), nullable=False)
    fecha = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    fecha_pago = Column(DateTime)
    total = Column(Float)
    pago = Column(String)
    observacion = Column(String)
    cliente = relationship('Clientes', back_populates='remitos')
    detalles = relationship('DetallesRemitos', back_populates='remito')

# Detalles de remitos
class DetallesRemitos(Base):
    __tablename__ = 'DETALLES_REMITOS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_remito = Column(Integer, ForeignKey ('REMITOS.id'), nullable=False)
    producto = Column(String)
    cantidad = Column(Float)
    precio_unitario = Column(Float)
    descuento = Column(Float)
    total = Column(Float)
    remito = relationship('Remitos', back_populates='detalles')

# Acopios
class Acopios(Base):
    __tablename__ = 'ACOPIOS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey('CLIENTES.id'), nullable=False)
    fecha = Column(DateTime)
    fecha_modificacion = Column(DateTime)
    producto = Column(String)
    cantidad = Column(Float)
    cliente = relationship('Clientes', back_populates='acopios')


# Crear las tablas
Base.metadata.create_all(engine)