import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

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
        
        if UserModel.find_by_username(data['username']):
            return {"message": f"User with username {data['username']} already exists."}, 409
        else: 
            con = sqlite3.connect('data.db')
            cur = con.cursor()

            query = "INSERT INTO users VALUES (NULL, ?, ?)"
            cur.execute(query, (data['username'], data['password'],))

            con.commit()
            con.close()

            return {"message": "User created successfully."}, 201
