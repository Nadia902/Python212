from sqlalchemy import Column, Integer, String

from models2.database import Base


class Hospital(Base):
    __tablename__ = 'hospital'

    id = Column(Integer, primary_key=True)
    country = Column(String(250), nullable=False)
    town = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    number = Column(String(250), nullable=False)
    number_hospital = Column(Integer)

    def __init__(self, country, town, name, number, number_hospital):
        self.country = country
        self.town = town
        self.name = name
        self.number = number
        self.number_hospital = number_hospital

    def __repr__(self):
        return f"Больница (Страна: {self.country}, Город: {self.town}, Название: {self.name}, " \
               f"Номер телефона: {self.number}, Номер больницы: {self.number_hospital})"
