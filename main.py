# import sqlite3
# from db_conection import banco
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import inspect, create_engine
from sqlalchemy import Column, Integer, String, Double, ForeignKey


# banco = sqlite3.connect('banco.db')

Base = declarative_base()
engine = create_engine("sqlite:///banco.db")
insp = inspect(engine)


class Cliente(Base):
    __tablename__ = "cliente"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    endereco = Column(String)

    conta = relationship(
        "Conta", back_populates="cliente", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"Cliente (id={self.id}, name={self.name}, cpf={self.cpf})"


class Conta(Base):
    __tablename__ = "conta"
    # atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(Double)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta (id={self.id}, agencia={self.agencia}, num={self.num})"


Base.metadata.create_all(engine)
print(Cliente.__tablename__)
print(Conta.__tablename__)
print(insp.has_table("cliente"))
# criado uma sessão para a comunicção com DB
Session = sessionmaker(bind=engine)
session = Session()
# user = User(name='John Snow', password='johnspassword')
beto = Cliente(
    id='002',
    name='beto2',
    cpf='056.029.689-46',
    endereco='Rua Zzzzz, zzz',
)


session.add(beto)

print(beto.name)
query = session.query(Cliente).filter_by(name='beto2')
for u in query:
    print(u)
print(query.count())

session.close()
