from . import db
from sqlalchemy.sql import func


class leadearBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    score = db.Column(db.Integer)