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


ans = random.randint(1, 19)
print('Welcome to Magic 8 Ball')
question = input("What is your question?(Enter a yes or no question)")

if ans == 1:
	ans = 'It is certain.'
elif ans == 2:
	ans = 'It is decidedly so.'
elif ans == 3:
	ans = 'Without a doubt.'
elif ans == 4:
	ans = 'Yes - definitely.'
elif ans == 5:
	ans = 'You may rely on it.'
elif ans == 6:
	ans = 'As I see it, yes.'
elif ans == 7:
	ans = 'Outlook good.'
elif ans == 8:
	ans = 'Yes.'
elif ans == 9:
	ans = 'Signs point to yes.'
elif ans == 10:
	ans = 'Reply hazy, try again.'
elif ans == 11:
	ans = 'Ask again later.'
elif ans == 12:
	ans = 'Better not tell you now.'
elif ans == 13:
	ans = 'Cannot predict now.'
elif ans == 14:
	ans = 'Concentrate and ask again.'
elif ans == 15:
	ans = "Don't count on it."
elif ans == 16:
	ans = 'My reply is no.'
elif ans == 17:
	ans = 'My sources say no.'
elif ans == 18:
	ans = 'Outlook not so good.'
else:
	ans = 'Very doubtful.'

print(ans)
print('\n')



# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 







 









