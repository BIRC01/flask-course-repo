from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json_repr(self):
        store_items = [
            item.json_repr() for item in self.items.all()
        ]
        json_model_repr = {"name": self.name, "items": store_items}
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
