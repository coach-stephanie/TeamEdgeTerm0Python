import random

# -------------------------------------------- 

	# You've just learned about variables, conditionals.
	# Just from knowing those two topics, you can do so much!
	
	# Let's try to make a simple program that responds to the user.
	# We're going to recreate the Magic 8 Ball!!!
			
			# Never heard of it? That's ok!

					# You got this!

  # -------------------------------------------- 

	# How a Magic 8 Ball Works:

	# The user asks a question and vigoriously shakes the ball. 
	# Then the ball will respond with one of twenty responses, chosen at random. 

	# That's pretty simple right?

 # -------------------------------------------- 

	# Part 1: 
	# Print instructions on the screen and 
	# prompt the user to ask a question

	

  # --------------------------------------------


print("How a Magic 8 Ball Works:")
print("The user asks a question and vigoriously shakes the ball.")
print("Then the ball will respond with one of twenty responses, chosen at random.")

question = input("Ask a question")










# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - It is certain.
		# 1 - It is decidedly so.
		# 2 - Without a doubt.
		# 3 - Yes - definitely.
		# 4 - You may rely on it.
		# 5 - As I see it, yes.
		# 6 - Most likely.
		# 7 - Outlook good.
		# 8 - Yes.
		# 9 - Signs point to yes.
		# 10 - Reply hazy, try again.
		# 11 - Ask again later.
		# 12 - Better not tell you now.
		# 13 - Cannot predict now.
		# 14 - Concentrate and ask again.
		# 15 - Don't count on it.
		# 16 - My reply is no.
		# 17 - My sources say no.
		# 18 - Outlook not so good.
		# 19 - Very doubtful.

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 

one = random.randint(1,20)
if answer == 1:
	print("It is certain")
elif answer = 2:
	print("It is decidedly so")
elif answer = 3:
	print("Without a doubt.")
elif answer = 4:
	print("Yes - definitely.")
elif answer = 5:
	print("You may rely on it.")
elif answer = 6:
	print("As I see it, yes.")
elif answer = 7:
	print(" Most likely.")
elif answer = 8:
	print("Outlook good")
elif answer = 9:
	print("Yes.")
elif answer = 10:
	print(" Signs point to yes.")
elif answer = 11:
	print("Reply hazy, try again.")
elif answer = 12:
	print("Ask again later.")
elif answer = 13:
	print("Better not tell you now.")
elif answer = 14:
	print("Cannot predict now.")
elif answer = 15:
	print("Concentrate and ask again.")
elif answer = 16:
	print("Don't count on it.")
elif answer = 17:
	print("My reply is no.")
elif answer = 18:
	print(" My sources say no.")
elif answer = 19:
	print("Outlook not so good.")
else:
	print("Very doubtful.")












# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 


one = random.randint(1,20)
if answer == 1:
	print("Pinkie swear its true")
elif answer = 2:
	print("100% certain")
elif answer = 3:
	print("Yass")
elif answer = 4:
	print("Yes slay")
elif answer = 5:
	print("I'm not smart, but trust me, its a yes")
elif answer = 6:
	print("Absolutely bestie")
elif answer = 7:
	print("Most definently")
elif answer = 8:
	print("I can say yes")
elif answer = 9:
	print("Yes")
elif answer = 10:
	print("I think lol")
elif answer = 11:
	print("I'm too tired to answer that")
elif answer = 12:
	print("Go away")
elif answer = 13:
	print("Ask later I'm eating")
elif answer = 14:
	print("TMI")
elif answer = 15:
	print("Be more specific bozo")
elif answer = 16:
	print("I don't think so buddy")
elif answer = 17:
	print("No sorry buster")
elif answer = 18:
	print("Did you think it would be a yes??")
elif answer = 19:
	print("Gonna have to say no bestie")
else:
	print("Absolutely not lmao")














