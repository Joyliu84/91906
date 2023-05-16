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
hot_chips = Label(root, text = 'Hot Chips', padx = 40, pady = 20)
burger = Label(root, text = 'Burgers', padx = 40, pady = 20)
pasta = Label(root, text = 'Pasta', padx = 40, pady = 20)
soup = Label(root, text = 'Soup', padx = 40, pady = 20)

hot_chips.grid(row = 2, column = 0)
burger.grid(row = 3, column =0)
pasta.grid(row = 4, column =0)
soup.grid(row = 5, column =0)

# chilled
fruit_salad = Label(root, text = 'Fruit Salad', padx = 40, pady = 20)
sushi = Label(root, text = 'Sushi', padx = 40, pady = 20)
sandwiches = Label(root, text = 'Sandwiches', padx = 40, pady = 20)
egg_salad = Label(root, text = 'Egg Salad', padx = 40, pady = 20)

fruit_salad.grid(row = 2, column = 1)
sushi.grid(row = 3, column =1)
sandwiches.grid(row = 4, column =1)
egg_salad.grid(row = 5, column =1)

# drinks
cola = Label(root, text = 'Cola', padx = 40, pady = 20)
milkshake = Label(root, text = 'Milkshake', padx = 40, pady = 20)
orange_juice = Label(root, text = 'Orange juice', padx = 40, pady = 20)
apple_juice = Label(root, text = 'Apple Juice', padx = 40, pady = 20)

cola.grid(row = 2, column = 2)
milkshake.grid(row = 3, column =2)
orange_juice.grid(row = 4, column =2)
apple_juice.grid(row = 5, column =2)

# desserts
brownies = Label(root, text = 'Brownies', padx = 40, pady = 20)
cookies = Label(root, text = 'Cookies', padx = 40, pady = 20)
ice_cream = Label(root, text = 'Ice Cream', padx = 40, pady = 20)
cupcakes = Label(root, text = 'Cupcakes', padx = 40, pady = 20)

brownies.grid(row = 2, column = 3)
cookies.grid(row = 3, column =3)
ice_cream.grid(row = 4, column =3)
cupcakes.grid(row = 5, column =3)



root.mainloop()