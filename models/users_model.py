from db import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def saved_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_username(cls, username):
        select_query_username = cls.query.filter_by(username=username).first()
        return select_query_username

    @classmethod
    def find_id(cls, _id):
        select_query_id = cls.query.filter_by(id=_id).first()
        return select_query_id
