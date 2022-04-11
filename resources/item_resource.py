from flask_restful import (
    Resource,
    reqparse,
)
from flask_jwt import jwt_required
from models.item_model import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This cannot be left blank"
    )
    parser.add_argument(
        'store_id',
        type=int,
        required=True,
        help="Every item needs a store id"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_name(name)
        if item:
            return item.json_repr()
        return {'message': 'Item Not Found'}, 404

    def post(self, name):
        if ItemModel.find_name(name):
            return {"message": "The {} already exists".format(name)}, 400

        request_data = Item.parser.parse_args()
        item = ItemModel(name, **request_data)

        try:
            item.saved_db()
        except:
            return {"message": "An error occurred during the creation"}, 500

        return item.json_repr(), 201

    def delete(self, name):

        item = ItemModel.find_name(name)
        if item:
            item.deleted_db()
        return {"message": "Item has been deleted"}

    def put(self, name):
        request_data = Item.parser.parse_args()

        item = ItemModel.find_name(name)

        if item is None:
            item = ItemModel(name, **request_data)
        else:
            item.price = request_data['price']

        item.saved_db()
        return item.json_repr()


class ItemList(Resource):
    def get(self):
        item_select_all_query = ItemModel.query.all()
        items = list(map(lambda item: item.json_repr(), item_select_all_query))
        # Another way:
        # items = [item.json_repr() for item in item_select_all_query]
        return {"items": items}
