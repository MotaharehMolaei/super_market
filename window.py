from tkinter import *
from tkinter import messagebox, DoubleVar
from my_module import *

window = Tk()
window.title("Supermarket")
window.geometry("600x400")

# ID
Label(window, text="ID").place(x=20, y=20)
id = IntVar()
Entry(window, textvariable=id).place(x=100, y=20)

# Name
Label(window, text="name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=60)

# Brand
Label(window, text="brand").place(x=20, y=100)
brand = StringVar()
Entry(window, textvariable=brand).place(x=100, y=100)

# quantity
Label(window, text="quantity").place(x=20, y=140)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=100, y=140)

# price
Label(window, text="price").place(x=20, y=180)
price = DoubleVar()
Entry(window, textvariable=price).place(x=100, y=180)

# expire_date
Label(window, text="expire date").place(x=20, y=220)
expire_date = StringVar()
Label(window, text="expire date").place(x=100, y=220)

Button(window,text="Save",command=save).place(x=80, y = 200, width=100)

window.mainloop()