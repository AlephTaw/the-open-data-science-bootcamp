## Using posgre

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psychopg2://testuser:testuserpassword@localhost:5432/alchemy_tutorial', echo=False)

# posgres default port 5432
# sudo -i -u postgres
# psql
# CREATE USER testuser WITH PASSWORD 'testuserpassword'

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
  __tablename__ = 'student'

  id = Column(Integer, primary_key=True)
  name = Column(String(50))
  age = Column(Integer)
  grade = Column(String(50))

Base.metadata.create_all(engine)

