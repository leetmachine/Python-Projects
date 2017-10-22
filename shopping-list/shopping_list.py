import os
#make a list to hold onto our items
shopping_list = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#function to show help
def show_help():
    clear()
    #print out instructions on how to use the app
    print("What should we pick up from the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
ENTER 'SHOW' to see the content of your cart.
ENTER 'REMOVE' to delete an item from your list.""")

#function to show list
def show_list():
    clear()
    print('Here is your list: ')

    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))
    
    print("-"*10)

def remove_from_list():
    show_list()
    item = input("What would you like to remove?\n> ")

    try:
        shopping_list.remove(item)
    except ValueError:
        print("{} was not in the list.".format(item))
        input("")
        pass
    show_list()

def add_to_list(new_item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                        "Press Enter to add to the end of the list\n"
                        "> ".format(new_item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, new_item)
    else:
        shopping_list.append(new_item)

    show_list()
#show instructions on initial launch
show_help()

while True:
    #ask for new items
    new_item = input("> ")

    #be able to quit the app
    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

    

#print out the list
print("\nHere's your final list:")
for item in shopping_list:
    print(item)