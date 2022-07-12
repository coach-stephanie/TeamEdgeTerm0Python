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
#DRINK EAT DESSERT
# --------------------------------------------
print("\t MENU ")
print("---------------------- \n")

print("Drinks:")
print("-------- \n")
print("1. Coke \t $02.00")
print("2. Pepsi \t $02.00\n")


print("Meals:  ")
print("-------- \n")
print("3. Hamburguer \t $06.00")
print("4. Hot dog \t $03.00")
print("5. Sushi \t $04.00\n")


print("Desserts:  ")
print("-------- \n")
print("6. Cake \t $03.50")
print("7. Flan \t $04.00\n")

print("Hi! Welcome to Steven's Shop :D")

user_drink = ""
user_meal = ""
user_dessert = ""

#START OF DRINK
def drink_ouput():
	#price1_2 = 2
	global user_drink
	drink = int(input("What whould you like to drink? (Enter 1 or 2)"))
	if drink == 1:
		price1_2 = 2.0
		user_drink = "Coke - $02.00"
		return price1_2
	if drink == 2:
		price1_2 = 2.0
		user_drink = "Pepsi - $02.00"
		return price1_2
#drink_ouput()
#END OF DRINK



#MEAL STARTS HERE
def meal_output():
	#price3 = 6.0
	# price4 = 3.0
	# price5 = 4.0
	global user_meal
	meal = int(input("What whould you like to eat? (Enter 3, 4 or 5)"))
	if meal == 3:
		price3 = 6.0
		user_meal = "Hamburger - $06.00"
		return price3
	elif meal == 4:
		price4 = 3.0
		user_meal = "Hot dog - $03.00"
		return price4
	elif meal == 5:
		price5 = 4.0
		user_meal = "Sushi - $04.00"
		return price5

#meal_output()
#MEAL ENDS HERE


#START OF DESSERT
def dessert_output():
	# price6 = 3.5
	# price7 = 4.0
	global user_dessert
	dessert = int(input("What whould you like for dessert? (Enter 6 or 7)"))
	if dessert == 6:
		price6 = 3.5
		user_dessert = "Cake - $03.50"
		return price6
	elif dessert == 7:
		price7 = 4.0
		user_dessert = "Flan - $04.00"
		return price7
#dessert_output()
#END OF DESSERT



cost = drink_ouput() + meal_output() + dessert_output()
taxes_cost = cost*0.08875
total_cost = cost + taxes_cost

print("your order total with tax is: ")
print(total_cost)


#HERE STARTS COSTUMERS TIP
def tip():
	costumers_tip = input("Would you like to leave a tip? (10%, 15%, 20%, 22%):  ")
	if costumers_tip=="10%":
		consumer_tip = total_cost*0.1
		return str(consumer_tip)
	elif costumers_tip=="15%":
		consumer_tip = total_cost*0.5
		return str(consumer_tip)
	elif costumers_tip=="20%":
		consumer_tip = total_cost*0.2
		return str(consumer_tip)
	elif costumers_tip=="22%":
		consumer_tip = total_cost*0.22
		return str(consumer_tip)
	elif costumers_tip=="0" or costumers_tip=="zero" or costumers_tip=="0%":
		return 0.0
#tip()
# COSTUMERS TIP END 

users_tip = str(tip())

# START OF RECEIPT

#Final_cost = total_cost + users_tip
print("Thanks! This is your receipt:")

print(user_drink )
print(user_meal )
print(user_dessert )
print("Subtotal: $", str(cost))
print("Tax: $0.08875")
print("Tip: $" + users_tip)
print("Total: $", str(total_cost))
print("\n Come again soon!")


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
