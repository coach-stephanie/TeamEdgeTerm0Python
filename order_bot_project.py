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
# Chipotle pt.2


user_drink=""
user_meal=""
user_dessert=""
total_mealcost=0
tax_meal=""
tip=0
def print_drinkmessage():
	print("You have selected a drink")
	


name1 = input("Enter name : ")
print(f"Hello {name1} what would you like to order? Please order  a drink")

def get_user_drinkinput():
	global total_mealcost
	global select_drink
	select_drink=int(input("Enter your drink. The options are Fanta(1), Water(2), or a Sprite(3)"))
	
	if select_drink == (1) or (2) or (3):
		print_drinkmessage()
		if select_drink == (1) or (3):
			total_mealcost = total_mealcost + 1.50
			
		elif select_drink == (2):
			total_mealcost = total_mealcost + 1.00
			

get_user_drinkinput()

print(f"Currently, the total meal cost is {total_mealcost}")


def get_user_mealinput():
	global total_mealcost
	global select_meal
	select_meal =int(input("Enter your drink. The options are Beef Burrito(4), Chicken Taco(5), or a Quesedilla(6)"))
	
	if select_meal == (4) or (5) or (6):
		print("You have selected a meal")
		if select_meal == (5) or (6):
			total_mealcost = total_mealcost + 6.00
			
		elif select_meal == (4):
			total_mealcost = total_mealcost + 9.00
			

get_user_mealinput()

print(f"Currently, the total meal cost is {total_mealcost}")

def get_user_dessertinput():
	global total_mealcost
	global select_dessert
	select_dessert=int(input("Enter your dessert. The options are Tres leches(7), Chocolate Popsicle(8)"))
	 
	if select_dessert == (7) or (8):
		print("You have selected a dessert")
		if select_dessert == (7) or (8):
			total_mealcost = total_mealcost + 3.00
			
		


get_user_dessertinput()

print(f"Currently, the total meal cost is {total_mealcost}")
tax_meal= (round(total_mealcost ** 0.0875,2))
total_mealcost = total_mealcost + tax_meal 
print(f"your order total with tax is: {total_mealcost}")
tip = input("Would you like to leave a tip? Yes or No? ")
if tip=="Yes":
	tip = float(input("Enter tip percentage as a decimal: "))
	tip = (round(total_mealcost ** tip,2))
	total_mealcost= total_mealcost + tip
	print("Your total meal cost including tip is:")
	print(round(total_mealcost,2))


else:
	total_mealcost 
	print(round(total_mealcost,2))


print("Thanks! This is your receipt:")

if select_drink == 1:
	print("Fanta = $1.50")
elif select_drink == 2:
	print("Water = $1.00")
elif select_drink == 3:
	print("Sprite = $1.50")

#print(select_meal)
#print(int(select_meal) == int(4))
if select_meal == 4:
	print("Beef Burrito 🌯  = $9.00")
elif select_meal == 5:
	print("Chicken Taco = $6.00")
elif select_meal == 6:
	print("Quesidilla = $6.00")

if select_dessert == 7:
	print("Tres Leches = $3.00")
elif select_meal == 8:
	print("Chocolate Popsicle = $3.00")

print(f"Tax :${tax_meal} ")
print(f"Tip :${tip} ")
print(f"Total :${total_mealcost} ")

print("Come back soon! ")
# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------






# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------












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
