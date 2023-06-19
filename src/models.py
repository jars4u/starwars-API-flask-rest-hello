from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(40), nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.height

    def serialize(self):
        return {
            "id": self.id,
            "height": self.height,
            "name": self.name
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    population = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.population

    def serialize(self):
        return {
            "id": self.id,
            "population": self.population,
            "name": self.name
            # do not serialize the password, its a security breach
        }


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people = db.relationship('People', backref='favorites', uselist=True)
    planet = db.relationship('Planet', backref='favorites', uselist=True)


    def __repr__(self):
        return '<User %r>' % self.people_id

    def serialize(self):
        return {
            "id": self.id,
            "people_id": self.people_id,
            "planet_id": self.planet_id,
            "user_id": self.user_id
            # do not serialize the password, its a security breach
        }
