import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Item name cannot be left blank!"
    )
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Item price cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        query = "SELECT * FROM items WHERE item_name = ?"
        result = cur.execute(query, (name,))
        row = result.fetchone()
        
        con.close()
        
        if row:
            return {"item": {'name': row[0], 'price': row[1]}}, 200
        return {"message": "Item not found"}, 404
         
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {'message': f'An item with {name} already exists.'}, 400
        data = Item.parser.parse_args()
        item = {
            'name': name,
            'price': data['price']
        }
        items.append(item)
        return item, 201

    def put(self, name):
        data = Item.parser.parse_args()
        for item in items:
            if item['name'] != name:
                item = {
                    'name': name,
                    'price': data['price']
                }
                items.append(item)
            else:
                item.update(data)
            return item
    
    def delete(self, name):
        global items
        items = list(filter(lambda x:x['name'] != name, items))
        return {'message': 'item deleted'}

class Items(Resource):
    def get(self):
        return {'items': items}, 200