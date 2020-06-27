from flask import Flask , redirect
from model.models import Base , People, Address
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dba:pegasos93@localhost:3306/rbsdb'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    #new_people = People('Bob Jones', 'bob@gmail.com','username','password','gender','photo')
    #db.session.add(new_people)
    #db.session.commit()
    #db.session.add(Address(new_people.id, 'teste',1234,'teste','teste'))
    #db.session.commit()

@app.route('/update')
def update():
    resp = requests.get('https://randomuser.me/api/').json()['results'][0]
    new_people = People(resp['name']['first'] + ' ' + resp['name']['last'],
                            resp['email'],
                            resp['login']['username'],
                            resp['login']['password'],
                            resp['gender'],
                            resp['picture']['large'])
    db.session.add(new_people)
    db.session.commit()

    new_address = Address(new_people.id,
                                resp['location']['street']['name'],
                                resp['location']['street']['number'],
                                resp['location']['city'],
                                resp['location']['state'])
    db.session.add(new_address)
    db.session.commit()
    return redirect('/')


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