from sqlalchemy import Column, Integer, String
from app import db

class WH_Order(db.Model):
    __tablename__ = 'wh_orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    json_body = Column(String(250))
