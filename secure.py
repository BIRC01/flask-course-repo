from hmac import compare_digest
from models.users_model import UserModel


def authenticate(username, password):
    user = UserModel.find_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_id(user_id)
