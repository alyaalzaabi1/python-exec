shopping_list = []

while True:
    action = input("Add, Remove, Show, or Quit: ").lower()
    
    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found.")
    elif action == "show":
        print("Shopping List:", shopping_list)
    elif action == "quit":
        break
    else:
        print("Invalid command.")
