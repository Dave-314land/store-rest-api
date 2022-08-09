import sqlite3
from flask_restful import Resource, reqparse


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


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="Username cannot be blank!"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="Password cannot be blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        
        if User.find_by_username(data['username']):
            return {"message": f"User with username {data['username']} already exists."}, 409
        else: 
            con = sqlite3.connect('data.db')
            cur = con.cursor()

            query = "INSERT INTO users VALUES (NULL, ?, ?)"
            cur.execute(query, (data['username'], data['password'],))

            con.commit()
            con.close()

            return {"message": "User created successfully."}, 201
