from sqlalchemy import Column, Integer, String
from . import db

class WH_Order(db.Model):
    __tablename__ = 'wh_orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    json_body = db.Column(db.String(250))
