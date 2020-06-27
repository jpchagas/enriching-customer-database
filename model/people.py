import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    gender = db.Column(db.String(50),nullable=False)
    photo = db.Column(db.String(50),nullable=False)

#Base.metadata.create_all(engine)