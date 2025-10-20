import re
import pickle
from datetime import datetime

product_list = []

def save_to_file(product_list):
    with open("Products.dat", "wb") as file:
        pickle.dump(product_list, file)

def name_validation(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise NameError("Invalid name!")

def brand_validation(brand):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", brand):
        raise NameError("Invalid brand!")

def quantity_validation(quantity):
    if not quantity >0:
        raise NameError("Invalid quantity!")

def price_validation(price):
    if not price > 0:
        raise NameError("Invalid price!")

def expiration_date_validation(expire_date):
    if not expire_date > datetime.today().date():
        raise NameError("Invalid expiration date!")


def get_date():
    name = input("Enter product name: ")
    brand = input("Enter product brand: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    expire_date_input = input("Enter expire date (YYYY-MM-DD): ")
    expire_date = datetime.strptime(expire_date_input, "%Y-%m-%d")

    if name_validation(name) and brand_validation(brand) and quantity_validation(quantity) and price_validation(price):

        product = {
            "name": name,
            "brand": brand,
            "quantity": quantity,
            "price": price,
            "expire_date": expire_date
        }
        return product
    else:
        print("Invalid product data.")
        return None

def show_data(product_list):
    for product in product_list:
        print(f"{product['name']: 10} - {product['brand']: 10} - {product["quantity"]:> 3}, {product['price']:> 8}")
        print("---------------------------------------------------------------------")
        print("Total cost: ", product["price"] * product["quantity"])


