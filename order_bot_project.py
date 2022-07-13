# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------
BurgerP = "Burger - 10.00"
CheeseBurgerP = "CheeseBurger - 12.50 " 
FriesP = "Fries - 2.50"  
JuiceP = "Juice - 2.00" 
SodaP = "Soda - 2.25"  
CookieP = "Cookie - 1.00" 
MuffinP = "Muffin - 2.50"
CakeP = "cake - 3.00"

BurgerPN = 10.00
CheeseBurgerPN = 12.50  
FriesPN = 2.50  
JuicePN = 2.00 
SodaPN = 2.25 
CookiePN = 1.00
MuffinPN = 2.50
CakePN = 3.00

# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------

menu = "Menu \n\n\n Plates \n Burger - 10.00 \n Cheese Burger - 12.50 \n Fries - 2.50 \n\n\n Drinks \n Juice - 2.00 \n Soda - 2.25 \n\n\n Desert \n Cookie - 1.00 \n Muffin - 2.50 \n Cake - 3.00"
print(menu.lower())






# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------




def order1():
	global recipt 
	global price1 
	order = input("Hello, what would you like from our plates?").lower()
	if order == "burger": 
		recipt = BurgerP
		price1 = BurgerPN
		order2()
	elif order == "cheese burger":
		recipt = CheeseBurgerP
		price1 = CheeseBurgerPN
		order2()
	elif order == "fries":
		recipt = FriesP
		price1 = FriesPN
		order2()
		
	else:
		print("Escuse me, can you repeat")
		order1()
	

def order2():
	global recipt2 
	global price2	
	ordert = input("Hello, what would you like from our drinks?").lower()
	if ordert == "juice":
		recipt2 = JuiceP
		price2 = JuicePN
		order3t()
	elif ordert == "soda":
		recipt2 = SodaP
		price2 = SodaPN
		order3t()
	else:
		print("Heh?")
		order2()



def order3t():
	order3 = input("Hello, what would you like from our deserts?").lower()
	if order3 == "cookie":
		reciptf = (f"{recipt} \n {recipt2} \n {CookieP}")
		pricet = price1 + price2 + CookiePN
		print (reciptf)
		print (f"Without tax {pricet}")
		pricewt = round(pricet * 1.08875, 2)
		print (f"With Tax {pricewt}")
		tip = float(input("How many dollars for tip?"))
		Finalp = tip + pricewt
		print("Here is you recipt")
		print (reciptf)
		print (f"Without tax {pricet}")
		print (f"With Tax {pricewt}")
		print (f"Final price: {Finalp}")
	elif order3 == "muffin" :
		reciptf = (f"{recipt} \n {recipt2} \n {MuffinP}")
		pricet = price1 + price2 + MuffinPN
		print (reciptf)
		print (f"Without tax {pricet}")
		pricewt = round(pricet * 1.08875, 2)
		print (f"With Tax {pricewt}")
		tip = float(input("How many dollars for tip?"))
		print("Here is you recipt")
		Finalp = tip + pricewt
		print (reciptf)
		print (f"Without tax {pricet}")
		print (f"With Tax {pricewt}")
		print (f"Final price: {Finalp}")
	elif order3 == "cake":
		reciptf = (f"{recipt} \n {recipt2} \n {CakeP}")
		pricet = price1 + price2 + CakePN
		print (reciptf)
		print (f" With no tax {pricet}")
		pricewt = round(pricet * 1.08875, 2)
		print (f"With Tax {pricewt}")
		tip = float(input("How many dollars for tip?"))
		print("Here is you recipt")
		print (reciptf)
		print (f" With no tax {pricet}")
		print (f"With Tax {pricewt}")
		Finalp = tip + pricewt
		print (f"Final price: {Finalp}")
	else:
		print("Say what?")
		order3t()
	


order1()
		
		
		












# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 












# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 




# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
