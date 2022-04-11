from flask_restful import Resource
from models.store_model import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_name(name)
        if store:
            store_json = store.json_repr()
            return store_json
        return {"message": "Store Not Found"}, 404

    def post(self, name):
        store = StoreModel.find_name(name)
        if store:
            return {
                "message": "A store with name {} already exists".format(name)
                }, 400

        store_model = StoreModel(name)
        try:
            store_model.saved_db()
        except:
            return {
                "message": "An error occurred while creating the store"
                }, 500
        return store_model.json_repr(), 201

    def delete(self, name):
        store = StoreModel.find_name(name)
        if store:
            store.deleted_db()
        return {"message": "The stored has been deleted"}


class StoreList(Resource):
    def get(self):
        store_select_all_query = StoreModel.query.all()
        stores = list(
            map(lambda store: store.json_repr(), store_select_all_query)
        )
        return {"stores": stores}
