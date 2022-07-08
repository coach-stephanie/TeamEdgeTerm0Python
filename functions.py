import random
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

def print_message():
	print('Hello')

print_message('hello')

# **** Challenge 1: Problem 2 ****
# Write a function called print_five_messages() that calls print_message() five times.

def print_five_messages():
	print_message()
	print_message()
	print_message()
	print_message()
	print_message()
	print('\n')

print_five_messages()
# **** Challenge 1: Problem 3 ****
# Write a function called get_user_input() that asks the user if they'd like to print your message
# once or five times. Then call one of the two functions above based on what the user decides.

def get_user_input():
	gui = int(input('Do you want to print 1 or 5 times?'))

	if gui == 1:
		print_message()
	elif gui == 5:
		print_five_messages()
	else:
		print('Invalid')

get_user_input()
# **** Challenge 1: Problem 4 ****
# Write a function called print_greeting() that prints a greeting message to the user.

def print_greeting():
	print('Greetings\n')

print_greeting()
# **** Challenge 1: Problem 5 ****
# Write a function called print_closing() that prints a goodbye message to the user.

def print_closing():
	print('Goodbye\n')

print_closing()
# **** Challenge 1: Problem 6 ****
# Write a function called run() that greets the user, asks them for input, and sends a goodbye message.
# Remember! Use the functions that you've already made. Don't hardcode anything!

def run():
	get_user_input()
	print_closing()

run()
print('\n--------------------\n')
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

num1 = int(input('Enter Any Number: '))
num2 = int(input('Enter Any Number: '))

def sum_double():
	if num1 == num2:
		sum = (num1 + num2) * 2
		print(sum)
	else:
		sum = num1 + num2
		print(sum)
	print('\n')

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

num1 = int(input('Enter Any Number: '))
num2 = int(input('Enter Any Number: '))

def makes_10():
	sum = num1 + num2
	if sum == 10 or num1 == 10 or num2 == 10:
		print('True')
	else:
		print('False')
	print('\n')

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

def alarm_clock():
	vac = input("Please enter 'on' or 'off' for vacation mode: ")
	dotw = (input('Please enter the day of the week (First three letters, Cap first letter): '))
# dotw = day of the week

	if vac == 'off':
		if dotw == 'Sun':
			print('Today is Sunday, alarm will ring at 10:00am.')
		elif dotw == 'Mon':
			print('Today is Monday, alarm will ring at 7:00am.')
		elif dotw == 'Tue':
			print('Today is Tuesday, alarm will ring at 7:00am.')
		elif dotw == 'Wed':
			print('Today is Wednesday, alarm will ring at 7:00am.')
		elif dotw == 'Thu':
			print('Today is Thursday, alarm will ring at 7:00am.')
		elif dotw == 'Fri':
			print('Today is Friday, alarm will ring at 7:00am.')
		elif dotw == 'Sat':
			print('Today is Saturday, alarm will ring at 10:00am.')
		else:
			print('Invalid Value')
	elif vac == 'on':
		if dotw == 'Sun':
			print('Today is a vacation Sunday, alarm will not ring.')
		elif dotw == 'Mon':
			print('Today is a vacation Monday, alarm will ring at 10:00am.')
		elif dotw == 'Tue':
			print('Today is a vacation Tuesday, alarm will ring at 10:00am.')
		elif dotw == 'Wed':
			print('Today is a vacation Wednesday, alarm will ring at 10:00am.')
		elif dotw == 'Thu':
			print('Today is a vacation Thursday, alarm will ring at 10:00am.')
		elif dotw == 'Fri':
			print('Today is a vacation Friday, alarm will ring at 10:00am.')
		elif dotw == 'Sat':
			print('Today is a vacation Saturday, alarm will not ring.')
		else:
			print('Invalid Value')
	else:
		print('Invalid Value')
	print('\n')

alarm_clock()
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

def speeding_ticket():
	speed = random.randint(30, 100)

	if speed <= 60:
		print("Police Officer: Sorry, I was mistaken. You won't be getting a speeding ticket.")
	elif speed >= 61 and speed <= 80:
		diff = speed - 60
		print(f"Police Officer: You were {diff}mph above the speed limit, heres a small speeding fine.")
	elif speed >= 81:
		diff = speed - 60
		print(f"Police Officer: You were {diff}mph above the speed limit, you are now detained for reckless driving.")
	else:
		print('Error')
	print('\n')

speeding_ticket()
# Make sure to test your code! Write a few function calls to make sure your code works!
