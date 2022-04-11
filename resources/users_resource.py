from flask_restful import (
    Resource,
    reqparse,
)

from models.users_model import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This cannot be left blank"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This cannot be left blank"
    )

    def post(self):

        request_data = UserRegister.parser.parse_args()

        if UserModel.find_id(request_data["username"]):
            return {"message": "The user already exits"}, 400

        user = UserModel(**request_data)
        user.saved_db()

        return {"message": "User created successfully"}, 201
