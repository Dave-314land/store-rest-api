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
        item = ItemModel.find_by_item_name(name)
        if item:
            return {"message": f"An item with the name, '{name}', already exists."}, 400

        data = self.parser.parse_args()
        item = ItemModel(name, data['price'])
        
        item.save_to_db()
        return {"message": f"Item with the name, '{name}', created successfully."}, 201

    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel.find_by_item_name(name)

        if item:
            item.price = data['price']
            item.save_to_db()
            return {"message": f"The price for {name} was updated successfully."}, 200
        else:
            item = ItemModel(name, data['price'])
            item.save_to_db()
            return {"message": f"Item with the name, '{name}', created successfully."}, 201
    
    def delete(self, name):
        item = ItemModel.find_by_item_name(name)
        if item:
            item.delete_from_db()
        return {"message": f"{name} has been deleted successfully."}, 200


class Items(Resource):
    def get(self):
        result = ItemModel.find_all_items()
        items = []
        if result:
            for row in result:
                items.append({'name': row.item_name, 'price': row.price})
        if items:
            return {"items": items}, 200
        return {"message": "No items found."}, 404
