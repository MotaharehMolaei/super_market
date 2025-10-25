from tkinter import *
from tkinter import messagebox
from my_module import *
from datetime import datetime


product_list = []

def save():
    try:
        name_validator(name.get())
        brand_validator(brand.get())
        quantity_validator(quantity.get())
        price_validator(price.get())
        exp_date = datetime.strptime(expire_date.get(), "%Y-%m-%d").date()
        expiration_date_validator(exp_date)
        product = {
            "id": id.get(),
            "name": name.get(),
            "brand": brand.get(),
            "quantity": quantity.get(),
            "price": price.get(),
            "expiration_date": exp_date
        }
        product_list.append(product)
        messagebox.showinfo("Saved", "Product saved successfully!")
        id.set(0)
        name.set("")
        brand.set("")
        quantity.set("0")
        price.set("0.0")
        expire_date.set("")
    except Exception as e:
        messagebox.showerror("Save Error", f"Error: {e}")


def total_price():
    """Calculate the total price of all products."""
    if not product_list:
        messagebox.showwarning("No Products", "No products available.")
        return

    total = 0
    for product in product_list:
        total += product["quantity"] * product["price"]

    messagebox.showinfo("Total Price", f"Total value of all products: {total}")

window = Tk()
window.title("Supermarket App")
window.geometry("600x400")

# id
Label (window, text="Id").place(x=30, y=30)
id = IntVar()
Entry(window, textvariable=id).place(x=150, y=30)

# name
Label (window, text="Name").place(x=30, y=70)
name = StringVar()
Entry(window, textvariable=name).place(x=150, y=70)

# brand
Label (window, text="Brand").place(x=30, y=110)
brand = StringVar()
Entry(window, textvariable=brand).place(x=150, y=110)

# quantity
Label (window, text="Quantity").place(x=30, y=150)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=150, y=150)

# price
Label (window, text="Price").place(x=30, y=190)
price = DoubleVar()
Entry(window, textvariable=price).place(x=150, y=190)

# date
Label(window, text="Expiration Date\n YYYY-MM-DD").place(x=30, y=230)
expire_date = StringVar()
Entry(window, textvariable=expire_date).place(x=150, y=230)

Button (window, text="Save", command=save).place(x=80, y=280, width=100)
Button(window, text="Total", command=total_price).place(x=200, y=280, width=100)

window.mainloop()