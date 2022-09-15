from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from decouple import config

from security import authenticate, identity
from db import db
from resources.user import UserRegister
from resources.item import Items, Item
from resources.store import Store, Stores

API_JWT_SECRET_KEY = config('JWT_SECRET_KEY')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = API_JWT_SECRET_KEY

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Items, '/items') # http://127.0.0.1:5000/items
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/apple
api.add_resource(UserRegister, '/register') # http://127.0.0.1:5000/register
api.add_resource(Stores, '/stores') # http://127.0.0.1:5000/stores
api.add_resource(Store, '/store/<string:name>') # http://127.0.0.1:5000/store/apple


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, port=5000)
