import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cur.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        
        con.close()
        return user
    
    @classmethod
    def find_by_id(cls, _id):
        con = sqlite3.connect('data.db')
        cur = con.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cur.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        
        con.close()
        return user
