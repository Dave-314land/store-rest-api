import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


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
        item = ItemModel.find_by_item_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        data = self.parser.parse_args()
        item = ItemModel(name, data['price'])
        if ItemModel.find_by_item_name(name):
            return {"message": f"An item with the name, '{name}', already exists."}, 400
        else:
            con = sqlite3.connect('data.db')
            cur = con.cursor()
            query = "INSERT INTO items VALUES (?, ?)"
            cur.execute(query, (item.name, item.price,)) 
            con.commit()
            con.close()
            return {"message": f"Item with the name, '{item.name}', created successfully."}, 201

    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel(name, data['price'])
        updated_item = ItemModel(name, data['price'])
        if ItemModel.find_by_item_name(name):
            con = sqlite3.connect('data.db')
            cur = con.cursor()
            query = "UPDATE items SET price=? WHERE item_name=?"
            cur.execute(query, (updated_item.price, updated_item.name,))
            con.commit()
            con.close()
            return {"message": f"The price for {updated_item.name} was updated successfully."}, 200
        else:
            con = sqlite3.connect('data.db')
            cur = con.cursor()
            query = "INSERT INTO items VALUES (?, ?)"
            cur.execute(query, (item.name, item.price,))
            con.commit()
            con.close()
            return {"message": f"Item with the name, '{item.name}', created successfully."}, 201
    
    def delete(self, name):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        query = "DELETE FROM items WHERE item_name=?"
        cur.execute(query, (name,))
        con.commit()
        con.close()
        return {"message": f"{name} has been deleted successfully."}, 200


class Items(Resource):
    def get(self):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        query = "SELECT * FROM items"
        result = cur.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        con.close()
        if items:
            return {"items": items}, 200
        return {"message": "No items found."}, 404
