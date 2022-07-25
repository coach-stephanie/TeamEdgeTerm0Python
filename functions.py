# -------------------------------------------- 

	# You've just learned about functions.
	# Functions are reusable pieces of code that make your code more modular.
	
	# If you are writing the same bit of code over and over, you are doing more work that you have to.
	# Use functions to simplify your code and decrease the amount of work you're doing. 

	# Any time you start thinking 'this is tedious', you can probably write a function for that task.

# -------------------------------------------- 


# -------------------------------------------- 
  # Challenge 1: Let's try to write some basic functions.
# -------------------------------------------- 

print("\n------------------- Challenge 1 -------------------\n")

# **** Challenge 1: Problem 1 ****
# Write a function called print_message() that prints any message you want.

print("What you want to write?:")
x = input()

def print_message():
	print(x)
print_message()

# **** Challenge 1: Problem 2 ****
# Write a function called print_five_messages() that calls print_message() five times.
def print_five_messages():
	print(x)
	print(x)
	print(x)
	print(x)
	print(x)

print_five_messages()

# **** Challenge 1: Problem 3 ****
# Write a function called get_user_input() that asks the user if they'd like to print your message
# once or five times. Then call one of the two functions above based on what the user decides.
def get_user_input():
	print("Do you want to print one or five times:")
	num = input()
	if num == "one":
		print_message()
	if num == "five":
		print_five_messages()
	if (num != "five") and (num != "one"):
		print("error")	
get_user_input()
# **** Challenge 1: Problem 4 ****
# Write a function called print_greeting() that prints a greeting message to the user.
def print_greeting():
	print("Greetings user")
print_greeting()
# **** Challenge 1: Problem 5 ****
# Write a function called print_closing() that prints a goodbye message to the user.
def print_closing():
	print("Ok. Goodbye user")
print_closing()

# **** Challenge 1: Problem 6 ****
# Write a function called run() that greets the user, asks them for input, and sends a goodbye message.
# Remember! Use the functions that you've already made. Don't hardcode anything!
def run():
	print_greeting()
	get_user_input()
	print_closing()

run()

# -------------------------------------------- 

# Challenge 2: Functions are also able to take input and return output. 
				# The value(s) you pass to it are called parameters.

# -------------------------------------------- 

print("\n------------------- Challenge 2 -------------------\n")

# **** Challenge 2: Problem 1 ****

# Write a function called sum_double that takes two number paramters and returns their sum.
# However, if the two values are the same, the funciton will return double their sum.

	# Examples:
		# sum_double(1, 2) → 3
		# sum_double(3, 2) → 5
		# sum_double(2, 2) → 8

# -------------------------------------------- 


def sum_double():
	print("What is the first number")
	num1 = int(input())

	print("What is the second number")
	num2 = int(input())

	sum = num1 + num2 
	sum2 = num1 + num2 + num1 + num2
	if num1 != num2:
		print(f"{num1} + {num2} = {sum}")
	if num1 == num2:
		print(f"{num1} + {num2} = {sum2}")


sum_double()


# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 2 ****

# Write a function called makes_10 that takes two numbers, a and b, and returns true if one of them is 10 or if their sum is 10.

	# Examples:
		# makes_10(9, 10) → True
		# makes_10(9, 9) → False
		# makes_10(1, 9) → True

# -------------------------------------------- 
def makes_10():
	print("What is the first number")
	numb1 = int(input())

	print("What is the second number")
	numb2 = int(input())
	
	sum12 = numb1 + numb2

	if (numb1 == 10) or (numb2 == 10) or (sum12 == 10):
		print("true")
	elif (numb1!= 10) or (numb2 != 10) or (sum12 != 10): 
		print("false")
	
makes_10()




# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 3 ****

# Write a function that will return the time our alarm is set to go off.

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string in the form "7:00" indicating
# when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
# the weekend it should be "10:00". However, if we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".
	# Examples:
		# alarm_clock(1, False) → "7:00"
		# alarm_clock(6, True) → "off"
		# alarm_clock(0, False) → "10:00"

# -------------------------------------------- 

def alarm():
	print("what day is it(put number)?")
	day = int(input())
	print("Are you on vacation? Yes or no?")
	vac = input()
	if vac == "yes":
		if (day == 1) or (day == 2) or (day == 3) or (day == 4) or (day == 5):
			print("Alarm sound at 10:00")
		if (day == 6) or (day == 7):
			print("Doesn't sounds")
	if vac == "no":
		if (day == 1) or (day == 2) or (day == 3) or (day == 4) or (day == 5):
			print("Alarm sound at 7:00")
		if (day == 6) or (day == 7):
			print("Alarm sounds at 10:00")

alarm()



# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 4 ****

# Write a function that will tell you if you received a speeding ticket.
# You are driving a little too fast, and a police officer stops you. 

# To compute the result, encoded as a number value: 
	# 0=no ticket
	# 1=small ticket
	# 2=big ticket
# If speed is 60 or less, the result is 0. 
# If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2.

# -------------------------------------------- 
def speedcheck():
	print("You are driving a little too fast, and a police officer stops you. What was your speed?")
	speed = int(input())
	if speed <= 60:
		print("0, no ticket")
	if (speed >= 61) and (speed <= 80):
		print("1, small ticket")
	if speed >= 81:
		print("2, big ticket")

speedcheck()






# Make sure to test your code! Write a few function calls to make sure your code works!
