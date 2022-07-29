#GAME GAME GAME GAME GAME GAME GAME

current_room = None
game_on = True
print("MAKE SURE YOU TYPE IN LOWERCASE LETTERS ONLY AND NO APOSTROPHIES")
command = input("Type 'start' to start the game ")
delay = 10


class Character:
    def __init__(self, name, health, damage, is_alive):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = []

    def get_items(items):
        self.inventory.append(item)
        print(f"Might be useful. You have {self.inventory}") 

class Room:
    def __init__(self, name, direction, items):
        self.name = name
        self.direction = direction
        self.items = items





items = ["pen", "ink", "knife", "headset", "key", "ink knife"]
inventory = []

third_floor = Room("Third Floor", {'West': "Bathroom", "South": "3FStairs", "North": "Electric Room"}, [])
bathroom = Room("Bathroom", {"East": "Third Floor"}, [0])
electric_room = Room("Electric Room", {"South": "Third Floor"}, [])
segundo_piso = Room("Second Floor", {"East": "Cockpit", "South": "2FStairs"}, [])
cockpit = Room("Cockpit", {"West": "Second Floor"}, [3])
first_floor = Room("First Floor",{"West": "Restaurant","East": "Workers Keep"}, [])
restaurant = Room("Restaurant",{"East": "First Floor"}, [1])
workers_keep = Room("Workers Keep", {"West": "First Floor"}, [2])
rooms = {
    "Bathroom": {"East": "Third Floor", "item": "pen"},
    "Electric Room": {"South": "Third Floor", "item": "directions"},
    "Second Floor": {"East": "Cockpit","South":  "2FStairs"},
    "Cockpit": {"West": "Second Floor", "item": "Record"},
    "First Floor": {"Restaurant", "Workers Keep"}
}
def bathroom_instructions(name, direction, items):
    #game directions go here
    print("You should not have eaten that sushi... \n")
    print("Lets get back to first class. The food is getting cold \n")
    

if command == "start":
    bathroom_instructions("Bathroom", "East", [0])
else:
    print("i said to type start...what are you doing")
current_room = bathroom

move = input("You can type go North/South/East/West to head that way.")

def cabin_instructions():
    print("You are now on the third floor")
    print("What's this? WTF??!?!?! Everyone is... \n")
    print("everyone is dead")
    





you = Character("you",1000, 1000, True)

#if command == "take":
#start'




while move != "go east":

    if move == "go west":
        print("There is nothing this way except a toilet...")
    elif move == "go north":
        print("I don't think you can go there unless you plan on climbing into the sink")
    elif move == "go south":
        print("Walk into the wall, I dare you")
    else: 
        print("I don't think you can do that")

    move = input("You can type 'go' North/South/East/West to head that way.")

print(cabin_instructions())
current_room = third_floor

    

#LOOK AROUND/GET A SCOPE OF THE SURROUNDINGS AND THE PLOT
#PLAYER SHOULD HAVE LEFT THE BATHROOM BY NOW

print("It appears everyone on this flight has mysteriously died \n")
print('Welcome to "Aliens On A Plane"')
print("Your goal is to find your way to safety, while avoiding \n and possibly killing the aliens hunting the last person on this plane \n YOU!!!")
print("keep in mind you are 50,000 feet in the air and cruising above the Atlantic Ocean with no clue \n who or what is in your flight path.")

first_move = input("What is your first move? You have alot of space on this aircraft. Choose a cardinal direction.>>>> ")
    
while first_move != "go south":

    if first_move == "go east":
        print("Fancy touching dead bodies? Choose another direction to go >>> ")
    elif first_move == "go west":
        print("You wont find anything in here...")
    elif first_move == "go north":
        print(f"You need {items[5]} to go into this room >>> ")
    else:
        print("You sure you can do that??")
    first_move = input("What is your first move? You have alot of space on this aircraft. Choose a cardinal direction.>>>> ")

if first_move == "go south":
    choice1 = input("You have reached the stairs, do you wish to walk down, or turn back? Type 'go Back' or 'go Down' to make your decision >>> ")

while choice1 != "go down":
    if choice1 == "go back":
        current_room = third_floor
        choice_back = input("U scared or something? Choose a direction to go >>> ")
        while choice_back != "go south":
            if choice_back == "go east":
                print("Fancy touching dead bodies? >>> ")
            elif choice_back == "go west":
                print("You wont find anything in here... >>> ")
            elif choice_back == "go north":
                print(f"You need {items[4]} to go into this room >>> ")
            else:
                print("You sure you can do that?? >>>")

            choice_back = input("Choose another direction to go >>>")

        #outside of choice_back loop - give them choice1 option 

        choice1 = "go down"
    else:
        print("Not too sure you can do that")
        choice1 = input("You have reached the stairs, do you wish to walk down, or turn back? Type 'go Back' or 'go Down' to make your decision >>> ")

#if choice1 == "go Down":
    #choice1 = input("You have reached the stairs, do you wish to walk down, or turn back? Type 'go Back' or 'go Down' to make your decision >>> ")

#enemy encounter
if choice1 == "go down":
    current_room = segundo_piso
    print("As you reach downstairs and find more fresh, bleeding, rotting, leaking, smelling corpses at your disposal.")

floor_two = input("Choose a direction to go in using 'go' and a cardinal direction >>> ")


if floor_two == "go east":
    print("Opening cockpit do-")
    print("AYURGVAUYRBGUAYFUDHAGUKYBSKJTBNSIUTHBUHGBSUHDBSHBISHIBUERBG")
    
    
attack1 = input("You have found an alien. How would you like to attack? Use 'hit left' or 'hit right' to choose >>> ")
while attack1 != "hit right":
    if attack1 == "hit left":
        print("You smacked the shit out of that alien. But...it's an alien so it didn't do much.")
        print("You have been killed.")
        quit()
    else:
        print("That's not a valid command")
    attack1 = input("You have found an alien. How would you like to attack? Use 'hit left' or 'hit right' to choose >>> ")


if attack1 == "hit right":
    print("Good thing the aliens last victim ripped a hole in that spot. Well you killed it...")

land = input("You are now in the cockpit, and in control of this jumbo jet. But whats this? \n No tower communication? Looks like you might have to fly this plane inexperienced.\n Choose 'turn left' or 'turn right' to make a decision. >> ")
while land != "turn right":
    if land == "turn left":
        print("You and another plane had the same idea, and you two havbe collided. Now you have added to the death toll...")
        print("GAME OVER")
        quit()
    else:
        print("Type a valid command")
        land = input("You are now in the cockpit, and in control of this jumbo jet. But whats this? \n No tower communication? Looks like you might have to fly this plane inexperienced.\n Choose 'turn left' or 'turn right' to make a decision. >> ")

if land == "turn right":
    print("You have evaded a flight that was in your way. You are now on course to safety")

last = input("You are decreasing at a steady pace. Choose 'more speed' , 'less speed' , or 'dont move' to make some final adjustments. >>> ")

while last != "dont move":
    if last == "less speed":
        print("Stalling...Stalling...YOU ARE GOING DOWN HERBGVHIWEBRVBDFGHJBFKUHBSUFGBUYOWHBFUYWHERIUYGHWIUERGHUWYERHGUYWERHBVUWHBERUIVHWIUERHIUYQHRGIUYWHDFOIBGQIDFBHVWOUEIRHOIUEHRBOIEHRNOIVQHBERUOYVHBQEIORUHWIERHVOIUQEHROIVUQHEROIUVHQEOIURVHOIUWERBNVIULWEFHBVUWHERKVUSBEKUVBSKUFVBSUKFBVSUBV\n The plane has exploded and you have died")
        quit()
    elif last == "more speed":
        print("You are contradicting the commands of the autopilot. The computer system has gotten furious and self destructed. \n You are dead now.")
        print("GAME OVER")
        quit()
    else:
        print("Type a valid command")
    last = input("You are decreasing at a steady pace. Choose 'more speed' , 'less speed' , or 'dont move' to make some final adjustments. >>> ")

if last == "dont move":
    print("The autopilot is flying really well and has landed the mighty Airbus A380 \n You have made it to safety")

print("As you exit the plane, you look to the sky and see fireworks...you have ma- \n Yo- hvae mdae it to the ariortp adn yuo aer sfae- \n Waht si ginog on?")

print("The world turns black, and you wake up inside a dim room, with machinery powering off.")
print(" 'Welcome back Mrs. Gedes' 'Thank you for testing our virtual reality genesis V121'. 'Please leave, while we send your payment to 2324 Sandbag Ave' 'You have passed the test and finished the game'. ")
wtf = input("As you leave the building and walk home, you wonder to yourself 'what the fuck just happened' >>> ")

if wtf == "what the fuck just happened":
    print("YOU WIN WOOHOOOO THANK YOU FOR PLAYING WOOHOOOOOO")
else:
    print("YOU STILL WIN EVEN THOUGH YOU DIDNT TYPE 'what the fuck just happened' WOOHOOOOOO")