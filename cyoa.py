#GAME GAME GAME GAME GAME GAME GAME

current_room = None
game_on = True
command = input("Type 'start' to start the game ")



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





items = ["pen", "paper", "ink", "knife", "headset", "key", "directions", "Record"]

third_floor = Room("Third Floor", {'West': "Bathroom", "South": "3FStairs", "North": "Electric Room"}, [])
bathroom = Room("Bathroom", {"East": "Third Floor"}, [0])
electric_room = Room("Electric Room", {"South": "Third Floor"}, [6])
segundo_piso = Room("Second Floor", {"East": "Cockpit", "South": "2FStairs"}, [])
cockpit = Room("Cockpit", {"West": "Second Floor"}, items)
rooms = {
    "Bathroom": {"East": "Third Floor", "item": "pen"},
    "Electric Room": {"South": "Third Floor", "item": "directions"},
    "Second Floor": {"East": "Cockpit","South":  "2FStairs"},
    "Cockpit": {"West": "Second Floor", "item": "Record"},
    "First Floor": {"Restaurant", "Workers Keep", "Cargo Room"}
}
def bathroom_instructions(name, direction, items):
    #game directions go here
    print("You should not have eaten that sushi... \n")
    print("Lets get back to first class. The food is getting cold \n")
    print("You can take this pen here if you want. It could help idk... \n")

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




while move != "go East":

    if move == "go West":
        print("There is nothing this way except a toilet...")
    elif move == "go North":
        print("I don't think you can go there unless you plan on climbing into the sink")
    elif move == "go South":
        print("Walk into the wall, I dare you")
    else: 
        print("I don't think you can do that")

    move = input("You can type go North/South/East/West to head that way.")

print(cabin_instructions())
current_room = third_floor

    

#LOOK AROUND/GET A SCOPE OF THE SURROUNDINGS AND THE PLOT
#PLAYER SHOULD HAVE LEFT THE BATHROOM BY NOW

print("It appears everyone on this flight has mysteriously died \n")
print('Welcome to "Aliens On A Plane"')
print("Your goal is to find your way to safety, while avoiding \n and possibly killing the aliens hunting the last person on this plane \n YOU!!!")
print("keep in mind you are 50,000 feet in the air and cruising above the Atlantic Ocean with no clue \n who or what is in your flight path.")

first_move = input("What is your first move? You have alot of space on this aircraft. Choose a cardinal direction.>>>> ")
    
while first_move != "go South":

    if first_move == "go East":
        print("Fancy touching dead bodies? Choose another direction to go")
    elif first_move == "go West":
        current_room = bathroom
        print("You wont find anything in here...")
    elif first_move == "go North":
        print(f"You need {items[5]} mto go into this room")
    else:
        print("You sure you can do that??")
    first_move = input("What is your first move? You have alot of space on this aircraft. Choose a cardinal direction.>>>> ")