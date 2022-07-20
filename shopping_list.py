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
#
active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list
#we check input an check if that input contains add or remove if it contains add or removw then we c reat  statement to move on to corespnd func. if add/remove is in stmnt then go to it. 
shopping_list = []

def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")
    return reply

    

def check_answer(ans):

    ans_list = ans.split(" ")
    add_or_remove = ans_list[0]
    groceries = ans_list[1]
    if add_or_remove == "add":
        add_item(groceries)
    elif add_or_remove == "remove":
        remove_item(groceries)

def add_item(item):
#this function can take in a string and store it in an array
    global shopping_list 
    shopping_list.append(item)




def remove_item(item):
    global shopping_list
    shopping_list.remove(item)
    
 

while active:
    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True
    print(f"Your shopping list now has: {shopping_list}")