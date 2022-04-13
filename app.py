import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from dotenv import (
    load_dotenv,
    find_dotenv,
)

from resources.item_resource import (
    Item,
    ItemList,
)
from secure import (
    authenticate,
    identity,
)
from resources.store_resource import (
    Store,
    StoreList,
)
from resources.users_resource import UserRegister
from db import db

load_dotenv(find_dotenv())

track_modifications = os.getenv('TRACK_MODIFICATIONS')
secret_key = os.getenv('SECRET_KEY')
database_uri = os.getenv('DATABASE_URI')
data_db = os.getenv('DATA_DB')
data_db_postgresql = os.getenv('DATABASE_URL')

app = Flask(__name__)
app.config[database_uri] = os.environ.get(data_db_postgresql, data_db)
app.config[track_modifications] = False
app.secret_key = secret_key

jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items/")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
