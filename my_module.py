import re
from datetime import datetime

def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise NameError("Invalid name!")

def brand_validator(brand):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", brand):
        raise NameError("Invalid brand!")

def quantity_validator(quantity):
    if not (type(quantity) == int and quantity > 0):
        raise NameError("Invalid quantity!")

def price_validator(price):
    if not price > 0:
        raise NameError("Invalid price!")

def expiration_date_validator(expire_date):
    if not expire_date > datetime.today().date():
        raise NameError("Invalid expiration date!")




