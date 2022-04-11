from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json_repr(self):
        json_model_repr = {"name": self.name, "price": self.price}
        return json_model_repr

    @classmethod
    def find_name(cls, name):
        select_query_name = cls.query.filter_by(name=name).first()
        return select_query_name

    def saved_db(self):
        db.session.add(self)
        db.session.commit()

    def deleted_db(self):
        db.session.delete(self)
        db.session.commit()
