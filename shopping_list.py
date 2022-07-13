#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/
import random

active = True

print("Welcome to Shopping List!")

welcome_message = ("Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n")





#-->Todo: declare a shopping_list list
list = []




def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")
    if reply == "add":
        add_item()
    elif reply == "remove":
        remove_item()
    else:
        print("not an option, be more clear")
    return reply


def check_answer():
    num = random.randrange(1,2) 
    if num == 1:
        print(welcome_message)
    elif num == 2:
        print("Hi! I'm your shopping assistant. Let me take your order. \n Just choose between add or remove and order")
    pass


def add_item():
#this function can take in a string and store it in an array
    y = input("What do you want to add?")
    if y in list:
        print("You already have that")
    else:
        list.append(y)
        print (list)
        print (f"Amount of items:{len(list)}")
    pass


def remove_item():
    x = input("What do you want to remove?")
    list.remove(x)
    print (list)
    print (f"Amount of items:{len(list)}")
    pass


prompt_user()
while active:
    list.sort()
    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True





check_answer()