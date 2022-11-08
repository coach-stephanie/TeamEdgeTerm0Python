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

Burger = 3.00 
Fries = 2.75
Cheesburger = 3.75

Water = 1.50
Juice = 1.75
Soda = 2.00

IceCream = 2.50
Scone = 3.75
Cake = 4.00

userdrink = 0.00 
userfood  = 0.00
userdessert = 0.00

userorderDr = ""
userorderF = ""
userorderDe = ""
#Tax = price_total % 8.875
# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------

def display_menu():
	print("Welcome to the secret store. We got food. May or may not be edible. Eat at your own discretion \n")
	print("Take a look at what we have here \n")
	print("----------------Meals-------------")
	print("1. Burgers: $3.00 \n")
	print("2. Fries: $2.50 \n")
	print("3. Cheesburger: $3.50 \n")
	print("--------------Drinks----------- \n")
	print("4. Water: $1.50 \n")
	print("5. Juice: $1.50 \n")
	print("6. Soda: $2.00 \n")
	print("----------------Dessert------------ \n")
	print("7. IceCream: $1.50 \n")
	print("8. Scones: $3.00 \n")
	print("9. Cake: $4.00 \n")

display_menu()
# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------
def drink():
	global userdrink
	global userorderDr
	drink = int(input("Drink bud? What do you want? Choose 4-6 or any other number if you arent thirsty \n"))
	if drink == 4:
		print("Water? Ok. \n") 
		userdrink = 1.50
		userorderDr = "Water"
	elif drink == 5:
		print("Juice? No problem \n")
		userdrink = 1.75
		userorderDr = "Juice"	
	elif drink == 6:
		print("Soda? Alright \n")
		userdrink = 2.00
		userorderDr = "Soda"
	else:
		print("No Bev??? Crazy")
drink()


def food():
	global userfood
	global userorderF
	food = int(input("And what do you need to eat? Use 1-3 to choose and use other numbers for nothing\n"))
	if food == 1:
		print("Burger! Nice... \n")
		userfood = 3.00
		userorderF = "Burger (No Cheese)"
	elif food == 2:
		print("Fries. Gotcha \n")
		userfood = 2.75
		userorderF = "Fries"
	elif food == 3:
		print("Cheesburger. No problem. \n")
		userfood = 3.75
		userorderF = "Burger (Cheese)"
	else:
		print("Then why are you...nevermind")
food()

def dessert():
	global userdessert
	global userorderDe
	dessert = int(input("Do you want some dessert? Choose 7-9 or press any other number for nothing \n"))
	if dessert == 7:
		print("IceCream. We only have vanilla smh... \n")
		userdessert = 2.50
		userorderDe = "Ice Cream"
	elif dessert == 8:
		print("Scones. Alright \n")
		userdessert = 3.75
		userorderDe = "Scones"
	elif dessert == 9:
		print("Cake. We only have chocolate. \n")
		userdessert = 4.00
		userorderDe = "Chocolate Cake"
	else:
		print("No dessert? Okay \n")
dessert()


# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 
final = input("will that be all? Y/N \n")
if final == "Y":
	print("Cool, here is the total \n ")
	


if final == "N":
	print("Too bad, here is your total: \n")
	


print("-------Total-----\n")
print(f"{userorderDr}: ${userdrink}")
print(f"{userorderF}: ${userfood}")
print(f"{userorderDe}: ${userdessert} \n")

print("--------Receipt------")









# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order

subtotal = userdrink + userfood + userdessert
# -------------------------------------------- 
tax2 = 0.08875
Tax = 8.8
total = (subtotal*tax2) + (subtotal)

def receipt():
	print(f"{userorderDr}: ${userdrink}")
	print(f"{userorderF}: ${userfood}")
	print(f"{userorderDe}: ${userdessert} \n")
	print(f"Subtotal: ${subtotal}")
	print(f"Tax: {Tax}%")
	
	




	print(f"Total: {round(total, 2)}")
receipt()

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
