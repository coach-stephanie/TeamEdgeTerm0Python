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
# print("How a Magic 8 Ball Works:")
# print("The user asks a question and vigoriously shakes the ball. ")
# print("Then the ball will respond with one of twenty responses, chosen at random. ")
# print("That's pretty simple right?")

# question = input("Ask a question \n")

# number = random.randint(0, 19)
# if number==0:
# 	print("It is certain.")
# elif number==1:
# 	print("It is decidedly so.")
# elif number==2:
# 	print("Without a doubt.")
# elif number==3:
# 	print("Yes - definitely")
# elif number==4:
# 	print("You may rely on it.")
# elif number==5:
# 	print("As I see it, yes.")
# elif number==6:
# 	print("Most likely.")
# elif number==7:
# 	print("Outlook good.")
# elif number==8:
# 	print("Yes.")
# elif number==9:
# 	print("Signs point to yes.")
# elif number==10:
# 	print("Reply hazy, try again.")
# elif number==11:
# 	print("Ask again later.")
# elif number==12:
# 	print("")
# elif number==13:
# 	print("Better not tell you now.")
# elif number==14:
# 	print("Concentrate and ask again.")
# elif number==15:
# 	print("Don't count on it.")
# elif number==16:
# 	print("My reply is no.")
# elif number==17:
# 	print("My sources say no.")
# elif number==18:
# 	print("Outlook not so good.")
# elif number==19:
# 	print("Very doubtful.")















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




















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# -------------------------------------------- 




print("How a Horoscopes Works:")
print("The user types what is their zodiac sign. ")
print("Then the horoscope will respond what it's your fortune. ")
print("That's pretty simple right?")

question = input("What is your zodiac sign? \n").lower()

if question == "aries":
	print("\n------------------- The Horoscope says -------------------\n")
	print("Aries natives, especially the ones owning a business, will have the grace of Jupiter right from the start of 2022.")
if question == "taurus":
	print("\n------------------- The Horoscope says -------------------\n")
	print("You will be a part of new adventures and endeavors right from the beginning of the year.")
if question == "gemini":
	print("\n------------------- The Horoscope says -------------------\n")
	print("You will certainly be able to give your best right from the start of the year.")
if question == "cancer":
	print("\n------------------- The Horoscope says -------------------\n")
	print("The focus point for the Cancer natives this year may be Personal life, Career, Finance and Property. All these spheres would be integral and essential, as there are quite happening things that would happen in all these spheres of life.")
if question == "leo":
	print("\n------------------- The Horoscope says -------------------\n")
	print("Leo will enjoy the favourable effects of most of the planets in 2022.")
if question == "virgo":
	print("\n------------------- The Horoscope says -------------------\n")
	print("The year 2022 will bring an abundance of opportunities, which one can use to make progress in life.")
if question == "libra":
	print("\n------------------- The Horoscope says -------------------\n")
	print("Your income can expect a slow pace, but later in the year, the gains will be good.")
if question == "scorpio":
	print("\n------------------- The Horoscope says -------------------\n")
	print("Singles may be in a pursuit to find love and happiness this year. Therefore, you would have to take care of what you plan to do. There may be some hurdles and difficulty in finding love during the initial months of 2022.")
if question == "sagittarius":
	print("\n------------------- The Horoscope says -------------------\n")
	print("This year, your aim with cupid's arrow is incredibly on target, which means love and romance is on the cards, and you are likely to enjoy the beautiful phase in your life.")
if question == "capricorn":
	print("\n------------------- The Horoscope says -------------------\n")
	print("You will gain experience in all aspects of your life which will turn out to be rewarding and worthwhile")
if question == "aquarius":
	print("\n------------------- The Horoscope says -------------------\n")
	print("the upcoming year shall start with a bit of mental stress and trouble.")
if question == "pisces":
	print("\n------------------- The Horoscope says -------------------\n")
	print("Pisces 2022 horoscope predicts that this year is gonna treat you well and help you make career progress.")




