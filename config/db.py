import sqlalchemy

def create_connection():
    engine =  sqlalchemy.create_engine('mysql+mysqlconnector://dba:pegasos93@localhost:3306/rbsdb', echo = True)
    #Create a session
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session
