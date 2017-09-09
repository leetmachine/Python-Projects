#make a list to hold onto our items
shopping_list = []

#function to show help
def show_help():
    #print out instructions on how to use the app
    print("What should we pick up from the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
ENTER 'SHOW' to see the content of your cart.""")

#function to show list
def show_list():
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    #add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
#show instructions on initial launch
show_help()

while True:
    #ask for new items
    new_item = input("> ")

    #be able to quit the app
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    
    add_to_list(new_item)

    

#print out the list
print("\nHere's your final list:")
for item in shopping_list:
    print(item)