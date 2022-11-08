import random 
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

#message = "\nWelcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
#print(message)
# -------------------------------------------- 

#print("\n------------------- Challenge 1 -------------------\n")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether the user is legally allowed to drive in your city. 



 #age = int(input(""):
   #print("")









# -------------------------------------------- 

#print("\n------------------- Challenge 2 -------------------\n") 

# Who placed first?
   # Create three variables and assign them random scores. 
   # Write conditional statements that check which is the highest score and prints it.

var1 = random.randint(10,20)
var2 = random.randint(10,20)
var3 = random.randint(10,20)

if var1 > var2 and var1 > var3:
   print("One wins!")
elif var2 > var1 and var2 > var3:
   print("Two wins")
else:
   print("three wins!")





# -------------------------------------------- 

#print("\n------------------- Challenge 3 -------------------\n")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:





weather = "rainy"
degrees = random.randint(0,90)
if weather == "rainy" and degrees <= 30:
  print("bring an umbrella and a coat")

elif weather == "sunny" and degrees >= 80:
  print("wear a hat and maybe some sunglasses")

elif weather == "stormy" and degrees <= 60:
  print("Dont go out!")

elif weather == "moderate" and degrees > 50:
   print("Wear a sweater it's chilly")
elif weather == "moderate" and degrees <50:
   print("Wear some shorts")
else: 
   print("Look out the window and you decide")











# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.


weather = "overcast"
degrees = random.randint(0,91)
if weather == "overcast" and degrees >60:
   print("wear a t-shirt and some sweatpants")

elif weather == "overcast" and degrees <60 and degrees >30:
   print("Maybe a light sweater will do")
elif weather == "overcast" and degrees <30:
   print("Get yourself a jacket ASAP")

#CREDIT TO STEVEN FOR GIVING ME THE IDEA TO ADD EXTRA DEGREES ON LINE 120






# -------------------------------------------- 

#print("\n------------------- Challenge 4 -------------------\n")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 

day = input("Enter day")

#day = input("Enter a day of the week")
if day == 1:
   print("monday")

elif day == 2:
   print("Tuesday") 

elif day == 3:
   print("Wednesday") 

elif day == 4:
   print("Thursday") 

elif day == 5:
   print("Friay") 


elif day == 6:
   print("Saturday")


       
elif day == 7:
   print("Sunday") 

# -------------------------------------------- 

#print("\n------------------- Challenge 5 -------------------\n")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.

#year = int(input("Enter year \n"))
year = int(input("Enter year"))
if year%4==0:
   if year%100==0:
     if year%400==0:
        print("This is a leap year")
     else:
        print("This is not a leap year")
   else: 
     print("This is a leap year")
else:
   print("This is not a leap year")


