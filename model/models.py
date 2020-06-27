from sqlalchemy import Column, Integer, String, ForeignKey
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
        return '<People %r>' % (self.name)

class Address(Base):
    __tablename__='address'

    id = Column(Integer,primary_key = True)
    pessoa_id =Column(Integer,ForeignKey("people.id"),nullable=False)
    street = Column(String(50),nullable=False)
    number = Column(String(50),nullable=False)
    city = Column(String(50),nullable=False)
    state = Column(String(50),nullable=False)

    def __init__(self, pessoa_id=None,street=None,number=None,city=None,state=None):
        self.pessoa_id = pessoa_id
        self.street = street
        self.number = number
        self.city = city
        self.state = state

    def __repr__(self):
        return '<Address %r>' % (self.street)