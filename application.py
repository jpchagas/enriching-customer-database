from flask import Flask , redirect
from model.models import Base , People, Address
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import atexit
from apscheduler.scheduler import Scheduler

application = Flask(__name__)

cron = Scheduler(daemon=True)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://j4h6pfu6j2hsgjsx:jnrhopjytnncg7ij@pqxt96p7ysz6rn1f.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/tqq7jin5tgyki2cl'
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://dba:pegasos93@localhost:3306/rbsdb'
db = SQLAlchemy(application)
cron.start()

@cron.interval_schedule(minutes=1)
def batch():
    #requests.get('http://127.0.0.1:5000/update')
    requests.get('https://ecdserver.herokuapp.com/update')
    print('Requested')

@application.before_first_request
def setup():
    #Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    #new_people = People('Bob Jones', 'bob@gmail.com','username','password','gender','photo')
    #db.session.add(new_people)
    #db.session.commit()
    #db.session.add(Address(new_people.id, 'teste',1234,'teste','teste'))
    #db.session.commit()

@application.route('/update')
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


@application.route('/')
def root():
    person = db.session.query(People).all()
    return u"<br>".join([u"{0}: {1}".format(p.name, p.email) for p in person])

@application.route('/updateapi')
def updateapi():
    #resp = peoplecontroller.update_api()
    #return resp
    pass

@application.route('/userbygenderbycity')
def userbygenderbycity():
    p ={}
    a = 1
    info = db.session.query(Address.city,People.gender,db.func.count(People.id)).join(Address, People.id == Address.pessoa_id).group_by(Address.city,People.gender).all()
    for i in info:
        p[a] = {'city':i[0],
                'gender':i[1],
                'amout': i[2]}
        a = a + 1
    return json.dumps(p,indent=2)
    
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == "__main__":
    application.debug = True
    application.run()