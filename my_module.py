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


def expiration_date_validator(dates):
    try:
        exp_date = datetime.strptime(dates, "%Y-%m-%d").date()
    except:
        raise ValueError("Expiration date format error!")

    if exp_date < date.today():
        raise ValueError("Expiration date cannot be in the past")

    return exp_date




