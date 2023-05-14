from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models2.database import Base


class Doctor(Base):
    __tablename__ = 'head_physician'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    id_doctor = relationship('Hospital')

    def __repr__(self):
        return f"Главный врач (ID: {self.id}, Имя: {self.group_name})"
