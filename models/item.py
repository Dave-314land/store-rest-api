import sqlite3


class ItemModel:
    def __init__(self, item_name, price):
        self.name = item_name
        self.price = price
    
    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_item_name(cls, name):
        con = sqlite3.connect('data.db')
        cur = con.cursor()
        query = "SELECT * FROM items WHERE item_name = ?"
        result = cur.execute(query, (name,))
        row = result.fetchone()
        con.close()
        if row:
            return cls(*row)