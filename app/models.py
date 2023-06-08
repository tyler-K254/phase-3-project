import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

engine = create_engine('sqlite:///hotels.db', echo=True)


    


class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    # reviews = relationship("Review", back_populates="hotel")

    def __repr__(self):
        return f'Hotel: {self.name}'
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    # reviews = relationship("Review", back_populates="customer")

    def __repr__(self):
        return f'Customer: {self.name}'
