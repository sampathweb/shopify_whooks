from flask import request
from flask.ext.restful import reqparse, abort, Api, Resource
from flask.ext.restful import fields, marshal, marshal_with, Api
from .models import WH_Order
from app import db

parser = reqparse.RequestParser()
parser.add_argument('orders', type=str)

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class OrderHook(Resource):

    def post(self):
        args = parser.parse_args()
        order = WH_Order()
        order.json_body = request.form['orders']
        db.session.add(order)
        db.session.commit()
        return None

class SmartCollection(Resource):

    def post(self):
        with open('wh_smart_collections.json', 'a') as outfile:
            outfile.write(request.form)
        return None