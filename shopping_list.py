# ********************************************************************

#  Team Edge List Mini-project: THE SHOPPING LIST HELPER

# This project prompts users using input() to prompt users
# to add (or remove) items from a shopping list. It starts empty
# and each time the program is run it asks you to either add or 
# remove an item from the list. It also updates the user of its
# contents. The shopping list also checks to see if an item 
# is already present in the list and prevents you from adding it
# again, giving feedback along the way. 

# ***************************************************************

# active = True

# print("Welcome to Shopping List!")

# welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

# print(welcome_message)


#-->Todo: declare a shopping_list list


# def prompt_user():

#     reply = input("What do you want to add or remove?  >>  ")

#     return reply

# def check_answer(ans):
#     pass


# def add_item():
# this function can take in a string and store it in an array
#     pass


# def remove_item():
#     pass

# while active:

#     check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True

# Gonna try making my own >:c
# --------------------------------------------------
commands= 'Type add or remove, then your item to make changes to the list. \nType mylist anytime to check the items on your list. \nType exit() anytime to leave the list.'

print('Smart Shopping List here, what do you wish to do today?')
print(commands)

active = True
mylist = []


while active:
    user_input = input('What do you want to do? >> ').lower()
    user_input = user_input.split()
    user_cmd = user_input.pop(0)
    user_input = " ".join(user_input)

    if user_cmd == 'add':
        if user_input in mylist:
            print('Item is already in the list.')
        elif user_input not in mylist:
            mylist.append(str(user_input))
    elif user_cmd == 'remove':
        if user_input not in mylist:
            print("Item doesn't exist.")
        elif user_input in mylist:
            mylist.remove(str(user_input))
    elif user_cmd == 'mylist':
        print(mylist)
    elif user_cmd == 'exit()':
        active = False
        print('Thank you for using this program.')
    elif user_cmd == 'cmds':
        print(commands)
    else:
        print('Error, Try Again')


    

