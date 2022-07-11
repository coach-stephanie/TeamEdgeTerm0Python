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



print("what is your zodiac sign?(First letter captilized and other lowercase)")
sign = input()


if sign == "Aries":
   print("The rams of Aries are said to be confident and fiery people. However, they may butt heads with others because they are infamously impatient and honest with their opinions..")

elif sign == "Taurus":
   print("Taurus bulls are said to be loyal and persistent. At the same time, these bulls are often stereotyped as being lazy and, appropriately, bullheaded.")

elif sign == "Gemini":
   print("People rocking the twins are said to be highly intelligent and sociable. On the other hand, they are also said to be superficial and indecisive.")

elif sign == "Cancer":
   print("The crabs of Cancer are said to be charitable people and loyal friends. On the other hand, they also tend to be blunt and are known to get … crabby when someone tries to get them out of their shells")

elif sign == "Leo":
   print("Leo lions are said to be proud and brave while sometimes getting a little too arrogant or competitive")

elif sign == "Virgo":
   print("Virgos are said to be diligent and organized. At the same time, Virgos are said to be overly critical perfectionists who tend to worry a lot")

elif sign == "Libra":
   print(" Libra is famously the sign of clever extroverts. These social butterflies are also said to be vain and hate making tough decisions.")

elif sign == "Scorpio":
   print("The scorpions of Scorpio are said to be magnetic thrill-seekers. Scorpios are also often said to be envious and fascinated by the macabre")

elif sign == "Sagittarius":
   print("Sagittarians are said to be highly independent adventurers who are always full of imagination. On the flip side, they are also said to be blunt and impatient.")

elif sign == "Capricorn":
   print("Capricorns are said to be tenacious and pragmatic. At the same time, Capricorns are said to be sticklers for the rules and ferocious when upset.")

elif sign == "Aquarius":
   print("Aquarians are said to be assertive and creative. Aquarians are also said to be impulsive loners.")

elif sign == "Pisces":
   print("A stereotypical Pisces is said to be an adventurous, compassionate person who may get a little too anxious or needy.")

#if (sign != "Aries") and (sign != "Taurus") and (sign != "Gemini") and (sign != "Cancer") and (sign != "Cancer") and (sign != "Leo") and (sign != "Virgo") and (sign != "Libra") and (sign != "Scorpio") and (sign != "Sagittarius") and (sign != "Capricorn") and (sign != "Aquarius") and (sign != "Pisces"):
else:
	print("Error")


print("Ask me anything")
qs = input()

import random
num = (random.randrange(1,21))
print (f"{num}")
if num == 1:
   print("It is certain.")

if num == 2:
   print("It is decidedly so.")

if num == 3:
   print("Without a doubt.")

if num == 4:
   print("Yes - definitely.")

if num == 5:
   print("You may rely on it.")

if num == 6:
   print("As I see it, yes.")

if num == 7:
   print("Most likely.")

if num == 8:
   print("Outlook good.")

if num == 9:
   print("Yes.")

if num == 10:
   print("Signs point to yes.")

if num == 11:
   print("Reply hazy, try again another time.")

if num == 12:
   print("Ask again later.")

if num == 13:
   print("Better not tell you now.")

if num == 14:
   print("Cannot predict now.")

if num == 15:
   print("Concentrate and ask again another time.")

if num == 16:
   print("Don't count on it.")

if num == 17:
   print("My reply is no.")

if num == 18:
   print("My sources say no.")

if num == 19:
   print("Outlook not so good.")

if num == 20:
   print("Very doubtful.")

if num == 21:
   print("I will put a curse on you, and you shall not pass.")


oneg = "You shall have a happy life"
twog ="You shall have a rich life"
threeg ="You shall die"
fourg ="IDK you future"
oneb = "You shall have a happy restuarant"
twob="You shall have a pool house"
threeb ="You shall be buried in california"
fourb ="you slow"
oney = "You will marry a good woman"
twoy ="You shall have a pizza life"
threey ="No sleep to Boston"
foury ="You go to Harvard"
oner = "You shall have a sad but ok life"
twor ="You shall have a poor life"
threer ="You shall die a painful death"
fourr ="IDK you future but you look nuce"

print("Green, Blue, Yellow, or Red?")
color = input()
if color == "Green":
		print("Green it is, teller was switched 5 times")
		answer1 = input("one, two, three, or four?")
		if answer1 == "one":
	   		print(oneg) 
		if answer1 == "two":
	  		print(twog)
		if answer1 == "three":
	  	 print(threeg)
		if answer1 == "four":
	   		print(fourg)



if color == "Blue":
	print("Blue it is, teller was switched 4 times")
	answer2 = input("one, two, three, or four?")
	if answer2 == "one":
		print(f"{oneb}")
	if answer2 == "two":
		print(f"{twob}") 
	if answer2 == "three":
		print(f"{threeb}") 
	if answer2 == "four":
		print(f"{fourb}")


if color == "Yellow":
	print("Yellow it is, teller was switched 6 times")
	answer3 = input("one, two, three, or four?")
	if answer3 == "one":
	   	print(f"{oney}")
	if answer3 == "two":
	   	print(f"{twoy}")
	if answer3 == "three":
	   	print(f"{threey}")
	if answer3 == "four":
		print(f"{foury}")



if color == "Red":
	print("Red it is, teller was switched 3 times")
	answer4 = input("one, two, three, or four?")
	if answer4 == "one":
		print(f"{oner}")
	if answer4 == "two":
		print(f"{twor}")
	if answer4 == "three":
		print(f"{threer}")
	if answer4 == "four":
		print(f"{fourr}")




# -------------------------------------------- 

	# Part 2: Next, we need to randomly select a response from 20 options.

	# Randomly select a number from 0 - 19 
	# Use that to select from the following responses:
		# 0 - 
		# 1 - 
		# 2 - 
		# 3 - 
		# 4 - 
		# 5 - 
		# 6 - 
		# 7 - 
		# 8 - 
		# 9 - 
		# 10 - 
		# 11 - 
		# 12 - 
		# 13 - 
		# 14 - 
		# 15 - 
		# 16 - 
		# 17 - 
		# 18 - 
		# 19 - 

	# Look up random.rand_int to see how you can use it to select a random number.

  # -------------------------------------------- 




















# -------------------------------------------- 

	# Part 3: Customize it!

	# Select your own theme and use case and modify your code!
	
# ---------------------