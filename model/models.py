from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class People(Base):
    __tablename__='people'

    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False)
    username = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)
    gender = Column(String(50),nullable=False)
    photo = Column(String(50),nullable=False)

    def __init__(self,name=None,email=None,username=None,password=None,gender=None,photo=None):
        self.name=name
        self.email=email
        self.username=username
        self.password=password
        self.gender=gender
        self.photo=photo

    def __repr__(self):
        return '<User %r>' % (self.name)

class Address(Base):
    __tallename__='address'