"""
A small starter app to get Flask, Flask-RESTful and Flask-SQLAlchemy all talking.
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Gunnar14@localhost:5432/authentise'
db = SQLAlchemy(app)
api = Api(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(200))
    username = db.Column(db.String(200))
    password = db.Column(db.String(128))


db.create_all()


class UserResource(Resource):

    def get(self):
        return {'Hello': 'world'}

api.add_resource(UserResource, '/user')


if __name__ == '__main__':
    app.run(debug=True)
