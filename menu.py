from tkinter import * 
import PIL
from PIL import ImageTk
from PIL import Image
root = Tk()

root.geometry()
root.title("Eggs Tuckshop ordering system")


# welcome message
welcome_message = Label(text = "Welcome to the EGGS tuckshop ordering page" , font= ('Arial', 20), )
welcome_message.grid(row=0, column=0, padx = 50, pady = 20, columnspan=3)


# titles for the food
hot = Label(root, text = 'Hot', padx = 40, pady = 20, font= ('Arial', 16))
chilled = Label(root, text = 'Chilled', padx = 40, pady = 20, font= ('Arial', 16))
drinks = Label(root, text = 'Drinks', padx = 40, pady = 20, font= ('Arial', 16))
desserts = Label(root, text = 'Desserts', padx = 40, pady = 20, font= ('Arial', 16))

hot.grid(row = 1, column = 0)
chilled.grid(row = 1, column =1)
drinks.grid(row = 1, column =2)
desserts.grid(row = 1, column =3)


 # hot foods
hot_chips = Label(root, text = 'Hot Chips - $4.00')
burger = Label(root, text = 'Burgers - $5.00', padx = 40, pady = 20)
pasta = Label(root, text = 'Pasta - $5.00', padx = 40, pady = 20)
soup = Label(root, text = 'Soup - $4.50', padx = 40, pady = 20)

hot_chips.grid(row = 2, column = 0)
burger.grid(row = 5, column =0)
pasta.grid(row = 8, column =0)
soup.grid(row = 11, column =0)

# chilled
fruit_salad = Label(root, text = 'Fruit Salad - $3.00', padx = 40, pady = 20)
sushi = Label(root, text = 'Sushi - $5.50', padx = 40, pady = 20)
sandwiches = Label(root, text = 'Sandwiches - $5.00', padx = 40, pady = 20)
egg_salad = Label(root, text = 'Egg Salad - $4.50', padx = 40, pady = 20)

fruit_salad.grid(row = 2, column = 1)
sushi.grid(row = 5, column =1)
sandwiches.grid(row = 8, column =1)
egg_salad.grid(row = 11, column =1)

# drinks
cola = Label(root, text = 'Cola - $2.00', padx = 40, pady = 20)
milkshake = Label(root, text = 'Milkshake - $2.50', padx = 40, pady = 20)
orange_juice = Label(root, text = 'Orange juice $2.50', padx = 40, pady = 20)
apple_juice = Label(root, text = 'Apple Juice - $2.50', padx = 40, pady = 20)

cola.grid(row = 2, column = 2)
milkshake.grid(row = 5, column =2)
orange_juice.grid(row = 8, column =2)
apple_juice.grid(row = 11, column =2)

# desserts
brownies = Label(root, text = 'Brownies - $3.00', padx = 40, pady = 20)
cookies = Label(root, text = 'Cookies - $2.50 ', padx = 40, pady = 20)
ice_cream = Label(root, text = 'Ice Cream - $2.50', padx = 40, pady = 20)
cupcakes = Label(root, text = 'Cupcakes - $3.00', padx = 40, pady = 20)

brownies.grid(row = 2, column = 3)
cookies.grid(row = 5, column =3)
ice_cream.grid(row = 8, column =3)
cupcakes.grid(row = 11, column =3)

# Chip image
chip_img = Image.open("hotchip.jpg")
chip_img = chip_img.resize((150, 80))
new_chip = ImageTk.PhotoImage(chip_img)

chip_label = Label(root, image=new_chip)
chip_label.grid(row = 3, column = 0)

# burger image
burger_img = Image.open("burger.jfif")
burger_img = burger_img.resize((150,80))
new_burger = ImageTk.PhotoImage(burger_img)

burger_label = Label(root, image=new_burger)
burger_label.grid(row = 6, column=0)

# pasta image
pasta_img = Image.open("pasta.jpg")
pasta_img = pasta_img.resize((150,80))
new_pasta = ImageTk.PhotoImage(pasta_img)

pasta_label = Label(root, image=new_pasta)
pasta_label.grid(row = 9, column=0)

# soup image
soup_img = Image.open("soup.jpg")
soup_img = soup_img.resize((150,80))
new_soup = ImageTk.PhotoImage(soup_img)

soup_label = Label(root, image=new_soup)
soup_label.grid(row = 12, column=0)

# fruit salad img
fruits_img = Image.open("fruit salad.jpg")
fruits_img = fruits_img.resize((150,80))
new_fruits = ImageTk.PhotoImage(fruits_img)

fruits_label = Label(root, image=new_fruits)
fruits_label.grid(row = 3, column=1)

# sushi img
sushi_img = Image.open("sushi.jpg")
sushi_img = sushi_img.resize((150,80))
new_sushi = ImageTk.PhotoImage(sushi_img)

sushi_label = Label(root, image=new_sushi)
sushi_label.grid(row = 6, column=1)

# sandwiche img
sandwich_img = Image.open("sandwich.jpg")
sandwich_img = sandwich_img.resize((150,80))
new_sandwich = ImageTk.PhotoImage(sandwich_img)

sandwich_label = Label(root, image=new_sandwich)
sandwich_label.grid(row = 9, column=1)

# egg salad img
eggs_img = Image.open("egg salad.jpg")
eggs_img = eggs_img.resize((150,80))
new_eggs = ImageTk.PhotoImage(eggs_img)

eggs_label = Label(root, image=new_eggs)
eggs_label.grid(row = 12, column=1)

# cola img
cola_img = Image.open("coke.jpg")
cola_img = cola_img.resize((150,80))
new_cola = ImageTk.PhotoImage(cola_img)

cola_label = Label(root, image=new_cola)
cola_label.grid(row = 3, column=2)

# milkshake img
milkshake_img = Image.open("milkshake.jpg")
milkshake_img = milkshake_img.resize((150,80))
new_milkshake = ImageTk.PhotoImage(milkshake_img)

milkshake_label = Label(root, image=new_milkshake)
milkshake_label.grid(row = 6, column=2)

# orange juice img
orangej_img = Image.open("orange juice.jpg")
orangej_img = orangej_img.resize((150,80))
new_orangej = ImageTk.PhotoImage(orangej_img)

orangej_label = Label(root, image=new_orangej)
orangej_label.grid(row = 9, column=2)

# apple juice img
applej_img = Image.open("apple juice.jpg")
applej_img = applej_img.resize((150,80))
new_applej = ImageTk.PhotoImage(applej_img)

applej_label = Label(root, image=new_applej)
applej_label.grid(row = 12, column=2)

# brownie img
brownie_img = Image.open("brownie.jpg")
brownie_img = brownie_img.resize((150,80))
new_brownie = ImageTk.PhotoImage(brownie_img)

brownie_label = Label(root, image=new_brownie)
brownie_label.grid(row = 3, column=3)

# cookie img
cookie_img = Image.open("cookie.jpg")
cookie_img = cookie_img.resize((150,80))
new_cookie = ImageTk.PhotoImage(cookie_img)

cookie_label = Label(root, image=new_cookie)
cookie_label.grid(row = 6, column=3)

# ice cream img
icec_img = Image.open("ice cream.jpg")
icec_img = icec_img.resize((150,80))
new_icec = ImageTk.PhotoImage(icec_img)

icec_label = Label(root, image=new_icec)
icec_label.grid(row = 9, column=3)

# cupcake img
cupcake_img = Image.open("cupcake.jpg")
cupcake_img = cupcake_img.resize((150,80))
new_cupcake = ImageTk.PhotoImage(cupcake_img)

cupcake_label = Label(root, image=new_cupcake)
cupcake_label.grid(row = 12, column=3)

# entry
chipEntry = Entry(root)
chipEntry.grid(row = 4, column=0)

burgerEntry = Entry(root)
burgerEntry.grid(row = 7, column=0)

pastaEntry = Entry(root)
pastaEntry.grid(row = 10, column=0)

soupEntry = Entry(root)
soupEntry.grid(row = 13, column=0)

fruitsEntry = Entry(root)
fruitsEntry.grid(row = 4, column=1)

sushiEntry = Entry(root)
sushiEntry.grid(row = 7, column=1)

sandwichEntry = Entry(root)
sandwichEntry.grid(row = 10, column=1)

eggsEntry = Entry(root)
eggsEntry.grid(row = 13, column=1)

colaEntry = Entry(root)
colaEntry.grid(row = 4, column=2)

milkshakeEntry = Entry(root)
milkshakeEntry.grid(row = 7, column=2)

orangejEntry = Entry(root)
orangejEntry.grid(row = 10, column=2)

applejEntry = Entry(root)
applejEntry.grid(row = 13, column=2)

brownieEntry = Entry(root)
brownieEntry.grid(row = 4, column=3)

cookieEntry = Entry(root)
cookieEntry.grid(row = 7, column=3)

icecEntry = Entry(root)
icecEntry.grid(row = 10, column=3)

cupcakeEntry = Entry(root)
cupcakeEntry.grid(row = 13, column=3)
# entry end


# open checkout 
def open_checkout():
    checkout_window = Toplevel(root)

    checkout_window.title("Checkout")
    checkout_welcome = Label(checkout_window, text="Check Out", font= ('Arial', 20))
    checkout_welcome.grid( row=0, column= 1, columnspan=2, padx = 50, pady = 20,)

# open help
def open_help():
    help_window = Toplevel(root)

    help_window.title("Help")
    help_welcome = Label(help_window, text="Help", font= ('Arial', 20))
    help_welcome.grid(row=1, column= 3,padx = 50, pady = 20)
    help_text = Label(help_window, text="Welcome to the EGGS tuck shop ordering system\n"
                                        "If you wish you order, you can do so by entering\n"
                                        "the quantity you want under your desired food item\n "
                                        "After you have finished ordering, press on the checkout\n"
                                        "button and a summary of your order, you will be required\n"
                                        "to enter the name for the order along with the option\n"
                                        "to deliver or pick up your order", font= ('Arial', 14))
    help_text.grid(row = 2, column=2, columnspan=3, padx = 50, pady = 50)


# reset


# buttons
check_out = Button(root, text = 'Check Out', height = 5, width = 10, command = open_checkout)
check_out.grid(row = 9, column=4, rowspan= 2, padx= 10)

help = Button(root, text = 'Help', height = 5, width = 10,command = open_help)
help.grid(row = 11, column=4, rowspan= 2, padx= 10)

reset = Button(root, text = 'Reset', height = 5, width = 10, )
reset.grid(row = 13, column=4, rowspan= 2, pady= 10)

root.mainloop()