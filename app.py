from flask import Flask, jsonify, request

app = Flask(__name__)

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
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name, price):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item(name):
    pass

app.run(port=5000)