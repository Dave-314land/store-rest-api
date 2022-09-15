from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    #@jwt_required()
    def get(self, name):
        store = StoreModel.find_by_store_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_store_name(name):
            return {"message": f"A store with the name, '{name}', already exists."}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred while creating the store."}, 500

        return {"message": f"Store with the name, '{name}', created successfully."}, 201
    
    def delete(self, name):
        store = StoreModel.find_by_store_name(name)
        if store:
            store.delete_from_db()
        return {"message": f"{name} has been deleted successfully."}, 200


class Stores(Resource):
    def get(self):
        result = StoreModel.find_all_stores()
        stores = []
        if result:
            for row in result:
                stores.append({'name': row.store_name, 'id': row.id})
        if stores:
            return {"stores": stores}, 200
        return {"message": "No stores found."}, 404
