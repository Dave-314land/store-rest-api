import sqlite3

class User:
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
