from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['AQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#db.init_app(app) //could do this instead of db = SQLAlchemy(app) if using the 'init app pattern'

class Customer(db.Model):
  id = db.Column(sb.Integer, primary_key=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  address = db.Column(db.String(50), nullable=False)
  city = db.Column(db.String(50), nullable=False)
  postcode = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)

  # (one-to-many relationship) order.customer and customer.order are now directly accessible
  orders = db.relationship('Order', backref='customer')

# (many-to-many relationship) create association table
order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)    
)

class Order(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  order_date = db.column(db.DateTime, nullable=False, default=datetime.utcnow)
  shipped_date = db.column(db.Datetime)
  delivered_date = db.column(db.Datetime)
  coupon_code = db.column(db.String(50))
  customer_id = db.column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

  products = db.relationship('Product', secondary=order_product)

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False, unique= True)
  price = db.Column(db.Integer, nullable=False)

# # in python interpreter
# from app import db

# db.create_all()

# # sqlite shell from command line
# sqlite3 db.sqlite3
# .tables
# .schema
select * from product;
select * from "order";
select * from order_product;
# .exit