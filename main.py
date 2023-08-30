shopping_list = ['bread', 'eggs', 'milk', 'chicken', 'meat', 'tomatoes', 'spice']
keep_menu = True
while keep_menu:
    users_option = input("If you want to add an item to the shopping list, "
                         "please type A or a.\nIf you want to remove items "
                         "from the list please type r or R.\nIf you want to "
                         "view items in the list, please type v or V."
                         "\nIf you want to quit the program, type q or Q"
                         "\nType your answer here: ")

    if users_option == "a" or users_option == "A":
        add_to_list = input("Type what you want to add to the list: ")
        shopping_list.append(add_to_list)
        print(add_to_list + " has been added to your shopping list.")
        print(shopping_list)

    elif users_option == "r" or users_option == "R":
        remove_from_list = input("Type the item name that you want to remove: ")
        if remove_from_list in shopping_list:
            index = shopping_list.index(remove_from_list)
            shopping_list.pop(index)
            print(remove_from_list + " has been removed")
            print(shopping_list)
        else:
            print("This item is not in the list.")

    elif users_option == "v" or users_option == "V":
        print(shopping_list)

    elif users_option == "q" or users_option == "Q":
        keep_menu = False
