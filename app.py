from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from decouple import config

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Items, Item
from db import db

API_JWT_SECRET_KEY = config('JWT_SECRET_KEY')
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = API_JWT_SECRET_KEY
api = Api(app)
jwt = JWT(app, authenticate, identity) #/auth
db.init_app(app)

api.add_resource(Items, '/items') # http://127.0.0.1:5000/items
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/apple
api.add_resource(UserRegister, '/register') # http://127.0.0.1:5000/register

"""
stores = [
    {
        'name': 'Superpowers store',
        'items': [
            {
                'name': 'Flight',
                'price': 7000.00
            },
            {
                'name': 'Super Strength',
                'price': 8000.00
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    # Create a new store with an empty list of items
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})
"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)
