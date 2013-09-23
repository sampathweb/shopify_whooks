from flask import Flask, render_template
from flask import abort, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from web_hooks import OrderHook, SmartCollection

api.add_resource(OrderHook, '/wh_orders/', endpoint='wh_orders_ep')
api.add_resource(SmartCollection, '/wh_smart_cols/', endpoint='wh_smart_cols_ep')
