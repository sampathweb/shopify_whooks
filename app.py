from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class WH_Order(db.Model):
    __tablename__ = 'wh_orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    json_body = db.Column(db.String(250))

if __name__ == '__main__':
    manager.run()
