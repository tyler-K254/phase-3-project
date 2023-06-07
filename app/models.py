import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
# from .base import Base
# from .restaurant import Restaurant
# from .customer import Customer


Base = declarative_base()
#engine = create_engine('sqlite:///hotels.db')
engine = create_engine('sqlite:///hotels.db', echo=True)


