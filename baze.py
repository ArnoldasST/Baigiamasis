from sqlalchemy import Column, String, Integer, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///inventorius.db')
Base = declarative_base()


class Elektronika(Base):
    __tablename__ = 'Elektronika'
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)
    kiekis = Column("Kiekis", Integer)
    kaina = Column("Vieneto kaina", Float)

    def __init__(self, pavadinimas, kiekis, kaina):
        self.pavadinimas = pavadinimas
        self.kiekis = kiekis
        self.kaina = kaina

    def __repr__(self):
        return f"{self.pavadinimas}, kiekis - {self.kiekis}, vieneto kaina - {self.kaina}"


Base.metadata.create_all(engine)
