import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="Item price cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = self.find_by_item_name(name)
        if item:
            return item
        return {"message": "Item not found"}, 404

    @classmethod
    def find_by_item_name(cls, name):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        query = "SELECT * FROM items WHERE item_name = ?"
        result = cur.execute(query, (name,))
        row = result.fetchone()
        
        con.close()
        
        if row:
            return {"item": {'name': row[0], 'price': row[1]}}, 200

    def post(self, name):
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}

        if self.find_by_item_name(name):
            return {"message": f"An item with the name, '{name}', already exists."}, 400
        else:
            con = sqlite3.connect('data.db')
            cur = con.cursor()

            query = "INSERT INTO items VALUES (?, ?)"
            cur.execute(query, (item['name'], item['price'],))
            
            con.commit()
            con.close()

            return {"message": f"Item with the name, '{item['name']}', created successfully."}, 201

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