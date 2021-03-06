import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Adresses(Base):
    __tablename__ = 'adresses'
    
    id = db.Column(db.Integer,primary_key = True)
    Column('pessoa_id',Integer,ForeignKey("people.id"),nullable=False)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    gender = db.Column(db.String(50),nullable=False)
    photo = db.Column(db.String(50),nullable=False)