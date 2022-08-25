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
        kwargs = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(kwargs['username'])
        
        if user:
            return {"message": f"User already exists."}, 409
        
        user = UserModel(**kwargs)
        user.save_to_db()
        return {"message": f"User created successfully"}, 201
