from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import PIL
from PIL import ImageTk
from PIL import Image
root = Tk()

"""This program is a ordering page for EGGS tuck shop"""
root.title("EGGS Tuckshop ordering system")
debug1 = StringVar

# sets the size of window
root.geometry("1000x800")


# changing the background colour
root.configure(background='#F7DBA7')


# welcome message
welcome_message = Label(text="Welcome to the EGGS tuckshop ordering page",
                        font=('Arial', 20), background="#F7DBA7")
welcome_message.grid(row=0, column=1,  pady=20, columnspan=3)


# titles for the food
hot = Label(root, text='Hot', padx=40, pady=10,
            font=('Arial', 16), background="#F7DBA7")
chilled = Label(root, text='Chilled', padx=40,   pady=10,
                font=('Arial', 16), background="#F7DBA7")
drinks = Label(root, text='Drinks', padx=40,
               pady=10, font=('Arial', 16), background="#F7DBA7")
desserts = Label(root, text='Desserts', padx=40,
                 pady=10, font=('Arial', 16), background="#F7DBA7")

# printing out the titles for the food
hot.grid(row=1, column=0)
chilled.grid(row=1, column=1)
drinks.grid(row=1, column=2)
desserts.grid(row=1, column=3)

# hot foods
hot_chips = Label(root, text='Hot Chips - $4.00',
                  background="#F7DBA7", font=('Arial', 13))
burger = Label(root, text='Burgers - $5.00', padx=40,
               pady=10, background="#F7DBA7", font=('Arial', 13))
pasta = Label(root, text='Pasta - $5.00', padx=40,
              pady=10, background="#F7DBA7", font=('Arial', 13))
soup = Label(root, text='Soup - $4.50', padx=40,
             pady=10, background="#F7DBA7", font=('Arial', 13))

# printing out the hot foods
hot_chips.grid(row=2, column=0)
burger.grid(row=5, column=0)
pasta.grid(row=8, column=0)
soup.grid(row=11, column=0)

# chilled
fruit_salad = Label(root, text='Fruit Salad - $3.00',
                    padx=40, pady=10, background="#F7DBA7", font=('Arial', 13))
sushi = Label(root, text='Sushi - $5.50', padx=40,
              pady=20, background="#F7DBA7", font=('Arial', 13))
sandwiches = Label(root, text='Sandwiches - $5.00',
                   padx=40, pady=10, background="#F7DBA7", font=('Arial', 13))
egg_salad = Label(root, text='Egg Salad - $4.50',
                  padx=40, pady=10, background="#F7DBA7", font=('Arial', 13))

# printing out the chilled foods
fruit_salad.grid(row=2, column=1)
sushi.grid(row=5, column=1)
sandwiches.grid(row=8, column=1)
egg_salad.grid(row=11, column=1)

# drinks
cola = Label(root, text='Cola - $2.00', padx=40,
             pady=10, background="#F7DBA7", font=('Arial', 13))
milkshake = Label(root, text='Milkshake - $2.50',
                  padx=40, pady=10, background="#F7DBA7", font=('Arial', 13))
orange_juice = Label(root, text='Orange juice $2.50',
                     padx=40, pady=10, background="#F7DBA7", font=('Arial', 13))
apple_juice = Label(root, text='Apple Juice - $2.50',
                    padx=40, pady=10, background="#F7DBA7", font=('Arial', 13))

# printing out the drinks
cola.grid(row=2, column=2)
milkshake.grid(row=5, column=2)
orange_juice.grid(row=8, column=2)
apple_juice.grid(row=11, column=2)

# desserts
brownies = Label(root, text='Brownies - $3.00', padx=40,
                 pady=10, background="#F7DBA7", font=('Arial', 13))
cookies = Label(root, text='Cookies - $2.50 ', padx=40,
                pady=10, background="#F7DBA7", font=('Arial', 13))
ice_cream = Label(root, text='Ice Cream - $2.50', padx=40,
                  pady=10, background="#F7DBA7", font=('Arial', 13))
cupcakes = Label(root, text='Cupcakes - $3.00', padx=40,
                 pady=10, background="#F7DBA7", font=('Arial', 13))

# printing out the desserts
brownies.grid(row=2, column=3)
cookies.grid(row=5, column=3)
ice_cream.grid(row=8, column=3)
cupcakes.grid(row=11, column=3)

# Chip image
chip_img = Image.open("hotchip.jpg")
chip_img = chip_img.resize((150, 80))
new_chip = ImageTk.PhotoImage(chip_img)

chip_label = Label(root, image=new_chip)
chip_label.grid(row=3, column=0)

# burger image
burger_img = Image.open("burger.jfif")
burger_img = burger_img.resize((150, 80))
new_burger = ImageTk.PhotoImage(burger_img)

burger_label = Label(root, image=new_burger)
burger_label.grid(row=6, column=0)

# pasta image
pasta_img = Image.open("pasta.jpg")
pasta_img = pasta_img.resize((150, 80))
new_pasta = ImageTk.PhotoImage(pasta_img)

pasta_label = Label(root, image=new_pasta)
pasta_label.grid(row=9, column=0)

# soup image
soup_img = Image.open("soup.jpg")
soup_img = soup_img.resize((150, 80))
new_soup = ImageTk.PhotoImage(soup_img)

soup_label = Label(root, image=new_soup)
soup_label.grid(row=12, column=0)

# fruit salad img
fruits_img = Image.open("fruit salad.jpg")
fruits_img = fruits_img.resize((150, 80))
new_fruits = ImageTk.PhotoImage(fruits_img)

fruits_label = Label(root, image=new_fruits)
fruits_label.grid(row=3, column=1)

# sushi img
sushi_img = Image.open("sushi.jpg")
sushi_img = sushi_img.resize((150, 80))
new_sushi = ImageTk.PhotoImage(sushi_img)

sushi_label = Label(root, image=new_sushi)
sushi_label.grid(row=6, column=1)

# sandwiche img
sandwich_img = Image.open("sandwich.jpg")
sandwich_img = sandwich_img.resize((150, 80))
new_sandwich = ImageTk.PhotoImage(sandwich_img)

sandwich_label = Label(root, image=new_sandwich)
sandwich_label.grid(row=9, column=1)

# egg salad img
eggs_img = Image.open("egg salad.jpg")
eggs_img = eggs_img.resize((150, 80))
new_eggs = ImageTk.PhotoImage(eggs_img)

eggs_label = Label(root, image=new_eggs)
eggs_label.grid(row=12, column=1)

# cola img
cola_img = Image.open("coke.jpg")
cola_img = cola_img.resize((150, 80))
new_cola = ImageTk.PhotoImage(cola_img)

cola_label = Label(root, image=new_cola)
cola_label.grid(row=3, column=2)

# milkshake img
milkshake_img = Image.open("milkshake.jpg")
milkshake_img = milkshake_img.resize((150, 80))
new_milkshake = ImageTk.PhotoImage(milkshake_img)

milkshake_label = Label(root, image=new_milkshake)
milkshake_label.grid(row=6, column=2)

# orange juice img
orangej_img = Image.open("orange juice.jpg")
orangej_img = orangej_img.resize((150, 80))
new_orangej = ImageTk.PhotoImage(orangej_img)

orangej_label = Label(root, image=new_orangej)
orangej_label.grid(row=9, column=2)

# apple juice img
applej_img = Image.open("apple juice.jpg")
applej_img = applej_img.resize((150, 80))
new_applej = ImageTk.PhotoImage(applej_img)

applej_label = Label(root, image=new_applej)
applej_label.grid(row=12, column=2)

# brownie img
brownie_img = Image.open("brownie.jpg")
brownie_img = brownie_img.resize((150, 80))
new_brownie = ImageTk.PhotoImage(brownie_img)

brownie_label = Label(root, image=new_brownie)
brownie_label.grid(row=3, column=3)

# cookie img
cookie_img = Image.open("cookie.jpg")
cookie_img = cookie_img.resize((150, 80))
new_cookie = ImageTk.PhotoImage(cookie_img)

cookie_label = Label(root, image=new_cookie)
cookie_label.grid(row=6, column=3)

# ice cream img
icec_img = Image.open("ice cream.jpg")
icec_img = icec_img.resize((150, 80))
new_icec = ImageTk.PhotoImage(icec_img)

icec_label = Label(root, image=new_icec)
icec_label.grid(row=9, column=3)

# cupcake img
cupcake_img = Image.open("cupcake.jpg")
cupcake_img = cupcake_img.resize((150, 80))
new_cupcake = ImageTk.PhotoImage(cupcake_img)

cupcake_label = Label(root, image=new_cupcake)
cupcake_label.grid(row=12, column=3)


# entry
chip_entry = Entry(root)
chip_entry.grid(row=4, column=0)

burger_entry = Entry(root)
burger_entry.grid(row=7, column=0)

pasta_entry = Entry(root)
pasta_entry.grid(row=10, column=0)

soup_entry = Entry(root)
soup_entry.grid(row=13, column=0)

fruits_entry = Entry(root)
fruits_entry.grid(row=4, column=1)

sushi_entry = Entry(root)
sushi_entry.grid(row=7, column=1)

sandwich_entry = Entry(root)
sandwich_entry.grid(row=10, column=1)

eggs_entry = Entry(root)
eggs_entry.grid(row=13, column=1)

cola_entry = Entry(root)
cola_entry.grid(row=4, column=2)

milkshake_entry = Entry(root)
milkshake_entry.grid(row=7, column=2)

orangej_entry = Entry(root)
orangej_entry.grid(row=10, column=2)

applej_entry = Entry(root)
applej_entry.grid(row=13, column=2)

brownie_entry = Entry(root)
brownie_entry.grid(row=4, column=3)

cookie_entry = Entry(root)
cookie_entry.grid(row=7, column=3)

icec_entry = Entry(root)
icec_entry.grid(row=10, column=3)

cupcake_entry = Entry(root)
cupcake_entry.grid(row=13, column=3)


def checkout():
    """This function error traps and calculates the checkout."""
    # getting the value for each input
    chip_value = chip_entry.get()
    burger_value = burger_entry.get()
    pasta_value = pasta_entry.get()
    soup_value = soup_entry.get()
    fruits_value = fruits_entry.get()
    sushi_value = sushi_entry.get()
    sandwich_value = sandwich_entry.get()
    eggs_value = eggs_entry.get()
    cola_value = cola_entry.get()
    milkshake_value = milkshake_entry.get()
    orangej_value = orangej_entry.get()
    applej_value = applej_entry.get()
    brownie_value = brownie_entry.get()
    cookie_value = cookie_entry.get()
    icec_value = icec_entry.get()
    cupcake_value = cupcake_entry.get()

    # checking if there is quantity inputed if not the value will be set to 0
    if len(chip_value) == 0:
        chip_value = 0
    if len(burger_value) == 0:
        burger_value = 0
    if len(soup_value) == 0:
        soup_value = 0
    if len(pasta_value) == 0:
        pasta_value = 0
    if len(fruits_value) == 0:
        fruits_value = 0
    if len(sushi_value) == 0:
        sushi_value = 0
    if len(sandwich_value) == 0:
        sandwich_value = 0
    if len(eggs_value) == 0:
        eggs_value = 0
    if len(cola_value) == 0:
        cola_value = 0
    if len(milkshake_value) == 0:
        milkshake_value = 0
    if len(orangej_value) == 0:
        orangej_value = 0
    if len(applej_value) == 0:
        applej_value = 0
    if len(brownie_value) == 0:
        brownie_value = 0
    if len(icec_value) == 0:
        icec_value = 0
    if len(cookie_value) == 0:
        cookie_value = 0
    if len(cupcake_value) == 0:
        cupcake_value = 0

    # error trapping for letters
    try:
        chip_value = int(chip_value)
        burger_value = int(burger_value)
        pasta_value = int(pasta_value)
        soup_value = int(soup_value)
        fruits_value = int(fruits_value)
        sushi_value = int(sushi_value)
        sandwich_value = int(sandwich_value)
        eggs_value = int(eggs_value)
        cola_value = int(cola_value)
        milkshake_value = int(milkshake_value)
        orangej_value = int(orangej_value)
        applej_value = int(applej_value)
        brownie_value = int(brownie_value)
        cookie_value = int(cookie_value)
        icec_value = int(icec_value)
        cupcake_value = int(cupcake_value)

        # if no error has been found
        occour_trouble = False
    # error trapping for numbers not between 1-100
        if chip_value >= 100 or chip_value < 0:

            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif burger_value >= 100 or burger_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif pasta_value >= 100 or pasta_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif soup_value >= 100 or soup_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif fruits_value >= 100 or fruits_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif sushi_value >= 100 or sushi_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif sandwich_value >= 100 or sandwich_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif eggs_value >= 100 or eggs_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif cola_value >= 100 or cola_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif milkshake_value >= 100 or milkshake_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif orangej_value >= 100 or orangej_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif applej_value >= 100 or applej_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif brownie_value >= 100 or brownie_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif cookie_value >= 100 or cookie_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif icec_value >= 100 or icec_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif cupcake_value >= 100 or cupcake_value < 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")
        elif chip_value == 0 and burger_value == 0 and pasta_value == 0 \
            and soup_value == 0 and fruits_value == 0 and sushi_value == 0 \
                and sandwich_value == 0 and eggs_value == 0 and \
        cola_value == 0 and milkshake_value == 0 and \
        orangej_value == 0 and applej_value == 0 \
        and brownie_value == 0 and cookie_value == 0 \
        and icec_value == 0 and cupcake_value == 0:
            occour_trouble = True
            messagebox.showerror(
                "error", "Please enter a number between 1 - 100")

    except:
        occour_trouble = True
        messagebox.showerror(
            "error", "Please only enter a positive whole number")

    if not occour_trouble:  # checking whether a error has occured for the inputed quantity
        # if not the checkout window will open
        checkout_window = Toplevel(root)
        # setting the colour for the checkout window
        checkout_window.configure(background='#F7DBA7')
        checkout_window.title("Checkout")
        checkout_welcome = Label(checkout_window, text="Check Out",
                                 font=('Arial', 20), background="#F7DBA7")
        # displaying the title of the checkout page
        checkout_welcome.grid(row=0, column=1, columnspan=2, padx=50, pady=22,)

        # calculating the price of food
        chip_price = chip_value * 4
        burger_price = burger_value * 5
        pasta_price = pasta_value * 5
        soup_price = soup_value * 4.5
        fruits_price = fruits_value * 3
        sushi_price = sushi_value * 5.5
        sandwich_price = sandwich_value * 5
        eggs_price = eggs_value * 4.5
        cola_price = cola_value * 2
        milkshake_price = milkshake_value * 2.5
        orangej_price = orangej_value * 2.5
        applej_price = applej_value * 2.5
        brownie_price = brownie_value * 3
        cookie_price = cookie_value * 2.5
        icec_price = icec_value * 2.5
        cupcake_price = cupcake_value * 3
        total = chip_price + burger_price + pasta_price + \
            soup_price + fruits_price + sushi_price + \
            sandwich_price + eggs_price + cola_price + \
            milkshake_price + orangej_price + applej_price \
            + brownie_price + cookie_price + \
            icec_price + cupcake_price
        tax = total * 0.15

        # display items prices on the GUI
        chip_p = Label(checkout_window, 
                       text="Chips - \t $%.2f" % chip_price, padx=40, 
                       font=('Arial', 13), background="#F7DBA7")
        chip_p.grid(row=2, column=2, rowspan=2)

        burger_p = Label(checkout_window, 
                         text="Burgers -  $%.2f" % burger_price, 
                         padx=40, font=('Arial', 13), background="#F7DBA7")
        burger_p.grid(row=4, column=2, rowspan=2)

        pasta_p = Label(checkout_window, 
                        text="Pasta - \t $%.2f" % pasta_price, 
                        padx=40, font=('Arial', 13), background="#F7DBA7")
        pasta_p.grid(row=6, column=2, rowspan=2)

        soup_p = Label(checkout_window, 
                       text="Soup - \t $%.2f" % soup_price, 
                       padx=40, font=('Arial', 13), background="#F7DBA7")
        soup_p.grid(row=8, column=2, rowspan=2)

        fruits_p = Label(checkout_window, 
                         text="Fruit salad - $%.2f" % fruits_price, padx=40, 
                         font=('Arial', 13), background="#F7DBA7")
        fruits_p.grid(row=10, column=2, rowspan=2)

        sushi_p = Label(checkout_window, 
                        text="Sushi - \t $%.2f" % sushi_price, 
                        padx=40, font=('Arial', 13), background="#F7DBA7")
        sushi_p.grid(row=12, column=2, rowspan=2)

        sandwich_p = Label(checkout_window, 
                           text="Sandwich - $%.2f" % sandwich_price, 
                           padx=40, font=('Arial', 13), background="#F7DBA7")
        sandwich_p.grid(row=14, column=2, rowspan=2)

        eggs_p = Label(checkout_window, 
                       text="Egg salad - $%.2f" % eggs_price, 
                       padx=40, font=('Arial', 13), background="#F7DBA7")
        eggs_p.grid(row=16, column=2, rowspan=2)

        cola_p = Label(checkout_window, 
                       text="Cola - \t $%.2f" % cola_price, 
                       padx=40, font=('Arial', 13), background="#F7DBA7")
        cola_p.grid(row=18, column=2, rowspan=2)

        milkshake_p = Label(checkout_window, 
                            text="Milkshake - $%.2f" % milkshake_price,
                            padx=40, font=('Arial', 13), background="#F7DBA7")
        milkshake_p.grid(row=20, column=2, rowspan=2)

        orangej_p = Label(checkout_window, 
                          text="Orange Juice - $%.2f" % orangej_price, 
                          padx=40, font=('Arial', 13), background="#F7DBA7")
        orangej_p.grid(row=22, column=2, rowspan=2)

        applej_p = Label(checkout_window, 
                         text="Apple Juice - $%.2f" % applej_price, 
                         padx=40, font=('Arial', 13), background="#F7DBA7")
        applej_p.grid(row=24, column=2, rowspan=2)

        brownie_p = Label(checkout_window, 
                          text="Brownie -  $%.2f" % brownie_price, padx=40, 
                          font=('Arial', 13), background="#F7DBA7")
        brownie_p.grid(row=26, column=2, rowspan=2)

        cookie_p = Label(checkout_window, 
                         text="Cookie - \t $%.2f" % cookie_price, 
                         padx=40, font=('Arial', 13), background="#F7DBA7")
        cookie_p.grid(row=28, column=2, rowspan=2)

        icec_p = Label(checkout_window, 
                       text="Ice cream - $%.2f" % icec_price, 
                       padx=40, font=('Arial', 13), background="#F7DBA7")
        icec_p.grid(row=30, column=2, rowspan=2)

        cupcake_p = Label(checkout_window, 
                          text="Cupcake - $%.2f" % cupcake_price, 
                          padx=40, font=('Arial', 13), background="#F7DBA7")
        cupcake_p.grid(row=32, column=2, rowspan=2)

        tax = Label(checkout_window, 
                    text="Tax - $%.2f" % tax, padx=40, 
                    pady=10, font=('Arial', 14), background="#F7DBA7")
        tax.grid(row=36, column=2, rowspan=2)

        total = Label(checkout_window, 
                      text="Total - $%.2f" % total, padx=40, 
                      pady=10, font=('Arial', 14), background="#F7DBA7")
        total.grid(row=38, column=2, rowspan=2)

        dining_options = Label(checkout_window, 
                               text="Dining Options", padx=40, 
                               font=('Arial', 13), background="#F7DBA7")
        dining_options.grid(row=40, column=2, rowspan=2)

        # dine in take out option
        clicked = StringVar()
        clicked.set("Dine in")

        drop = OptionMenu(checkout_window, clicked, "Dine in",
                          "Take out")  # creating the drop down menu
        drop.config(background="#F7DBA7")
        drop["menu"].config(background="#F1AB86")
        # displaying the drop down menu
        drop.grid(row=42, column=2, rowspan=2, columnspan=3)

        # enter name
        name = Label(checkout_window, text="Name for order (optional)",
                     padx=40, font=('Arial', 13), background="#F7DBA7")
        name.grid(row=44, column=2, rowspan=2)

        name_entry = Entry(checkout_window)
        name_entry.grid(row=46, column=2, rowspan=2)

        # placed order window
        def order():
            # creating the ordered window
            ordered_window = Toplevel(checkout_window)
            ordered_window.configure(
                background='#F7DBA7')  # setting the colour
            ordered_window.title("Order Placed")  # title of the window
            ordered_num = Label(ordered_window, text="Your order number is 1",
                                font=('Arial', 15), background="#F7DBA7")
            ordered_num.grid(row=3, column=2, padx=50, pady=20,
                             columnspan=3)  # displaying order number
            ordered_msg = Label(ordered_window, text="Your order has been placed",
                                font=('Arial', 20), background="#F7DBA7")
            ordered_msg.grid(row=2, column=2, padx=50, pady=20,
                             columnspan=3)  # displaying ordered message
            time = Label(ordered_window, 
                         text="Order will be ready in around 10 minutes", 
                         font=('Arial', 15), background="#F7DBA7")
            time.grid(row=4, column=2, padx=50, pady=20,
                      columnspan=3)  # displaying the wait time

        # place order button
        place_order = Button(checkout_window, text="Place order",
                             font=('Arial', 12), pady=10, 
                             command=order, background="#F1AB86")
        # place order button which will open the ordered page when pressed
        place_order.grid(row=48, column=2, rowspan=2)


# checkout button
check_out = Button(root, text='Check Out', height=5, width=10,
                   command=lambda: [checkout()], background="#F1AB86", 
                   font=('Arial', 13))
check_out.grid(row=5, column=4, rowspan=2, padx=10)


# open help
def open_help():
    help_window = Toplevel(root)  # creating help window
    help_window.configure(background='#F7DBA7')  # setting window colour
    help_window.title("Help")
    help_welcome = Label(help_window, text="Help", font=(
        'Arial', 20), background="#F7DBA7")
    # displaying the window title
    help_welcome.grid(row=1, column=3, padx=50, pady=20)
    help_text = Label(help_window, 
                      text="Welcome to the EGGS tuck shop ordering system\n"
                        "If you wish to order, you can do so by entering\n"
                        "the quantity you want under your desired food item\n "
                        "(In the following white bar)\n"
                        "(Please only enter a positive wholenumber under 100).\n"
                        "After you have finished ordering, press on the checkout\n"
                        "button and a summary of your order, you will be required\n"
                        "to enter the name for the order along with the option\n"
                        "to deliver or pick up your order", font=('Arial', 14),
                      background="#F7DBA7")
    help_text.grid(row=2, column=2, columnspan=3, padx=50, pady=50)


# help button
help = Button(root, text='Help', height=5, width=10, command=open_help,
              background="#F1AB86", font=('Arial', 13))
help.grid(row=3, column=4, rowspan=2, padx=10)

# exit button
exit = Button(root, text='Exit', height=5, width=10, background="#E76B74",
              command=root.destroy, font=('Arial', 13))
exit.grid(row=7, column=4, rowspan=3, pady=10)

root.mainloop()
