from flask import Flask
from model.models import Base , People
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dba:pegasos93@localhost:3306/rbsdb'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(People('Bob Jones', 'bob@gmail.com','username','password','gender','photo'))
    db.session.add(People('Joe Quimby', 'eat@joes.com','username','password','gender','photo'))
    db.session.commit()

@app.route('/')
def root():
    person = db.session.query(People).all()
    return u"<br>".join([u"{0}: {1}".format(p.name, p.email) for p in person])

@app.route('/updateapi')
def updateapi():
    #resp = peoplecontroller.update_api()
    #return resp
    pass

@app.route('/userbygenderbycity')
def userbygenderbycity():
    pass
    

app.run(debug=True)