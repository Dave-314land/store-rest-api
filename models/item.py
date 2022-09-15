from db import db


class ItemModel(db.Model):
    __tablename__ = "items"
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, item_name, price, store_id):
        self.item_name = item_name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name': self.item_name, 'price': self.price}

    @classmethod
    def find_by_item_name(cls, name):
        return cls.query.filter_by(item_name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all_items(cls):
        return cls.query.all()
