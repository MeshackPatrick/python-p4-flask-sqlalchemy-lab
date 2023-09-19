from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    animals = db.relationship('Animal', backref='zookeeper', lazy=True)


class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String(50), nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False)
    animals = db.relationship('Animal', backref='enclosure', lazy=True)


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'), nullable=False)
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'), nullable=False)
    animal_enclosure = db.relationship('Enclosure', backref='animal_enclosure')
