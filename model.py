from sqlalchemy import MetaData, Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("sqlite:///almacenDB.db")


class Productos(Base):
    __tablename__ = "productos"
    producto_id = Column(
        Integer(), unique=True, primary_key=True, nullable=False, autoincrement=True
    )
    nombre = Column(String(50), nullable=False)
    marca = Column(String(30), nullable=True)
    precio = Column(Float(precision=2), nullable=False)
    cantidad = Column(Integer(), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# session.add(Productos(nombre="Laptop", marca="Lenovo",precio=2299.99, cantidad=3))
# session.commit()
def getProducts():
    return session.query(
        Productos.nombre,
        Productos.marca,
        Productos.precio,
        Productos.cantidad,
        Productos.producto_id,
    ).all()


def insertProduct(nombre: str, marca: str, precio: float, cantidad: int):
    session.add(Productos(nombre=nombre, marca=marca, precio=precio, cantidad=cantidad))
    session.commit()


def delProduct(id: int):
    session.delete(session.query(Productos).filter(Productos.producto_id == id).one())
    session.commit()


def actuProduct(id: int, precio, cantidad):
    a = session.query(Productos).filter(Productos.producto_id == id).first()
    a.precio = precio
    a.cantidad= cantidad
    session.commit()
