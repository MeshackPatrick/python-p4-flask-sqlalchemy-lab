#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return '<h1>Zoo app</h1>'


@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get_or_404(id)
    response_body = f'<h1>Animal Information</h1>'
    response_body += f'<ul>'
    response_body += f'<li>ID: {animal.id}</li>'
    response_body += f'<li>Name: {animal.name}</li>'
    response_body += f'<li>Species: {animal.species}</li>'
    response_body += f'<li>Zookeeper: {animal.zookeeper.name}</li>'
    response_body += f'<li>Enclosure: {animal.enclosure.environment}</li>'
    response_body += f'</ul>'
    return make_response(response_body, 200)


@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get_or_404(id)
    response_body = f'<h1>Zookeeper Information</h1>'
    response_body += f'<ul>'
    response_body += f'<li>ID: {zookeeper.id}</li>'
    response_body += f'<li>Name: {zookeeper.name}</li>'
    response_body += f'<li>Birthday: {zookeeper.birthday}</li>'
    for animal in zookeeper.animals:
        response_body += f'<ul>'
        response_body += f'<li>Name: {animal.name}</li>'
        response_body += f'</ul>'
    response_body += f'</li>'
    response_body += f'</ul>'
    return make_response(response_body, 200)


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get_or_404(id)
    response_body = f'''
        <h1>Enclosure Information</h1>
        <ul>
             <li>Environment: {enclosure.environment}</li>
             <li>Open to Visitors: {enclosure.open_to_visitors}</li> 
        </ul>
    '''
    for animal in enclosure.animals:
        response_body += f'''
            <li>Name: {animal.name}</li>
        '''

    response_body += '''
            </ul>
    </ul>
    '''

    return make_response(response_body, 200)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
