#SW 2nd Personal Library


#Weapon Dictionary
weapons={

}
#view function (prints Weapon name and info)
def view(dictionary):
    for key in dictionary:
        print(f"{key}:{dictionary[key]}")
#Add function (asks user for Weapon name, asks user for Weapon info, adds them to a dictionary)
def plus(dictionary):
    name=input(f"What is the name of the item you would like to add to your inventory?\n")
    info=input(f"What is information you would like to give {name}?\n")
    dictionary[name]=info
    print(f"{name}:{dictionary[name]}")
    return dictionary
#Remove function (print dictionary, asks user for number Weapon that they want to remove,removes them to a dictionary)
def minus(dictionary):
    print("Note: If you remove it you will have to manually add it back!")
    name=input(f"Which item would you like to remove from your inventory?\n")
    if name in dictionary:
        del dictionary[name]
        print(f'{name} has been removed')
    else:
        print(f"{name} wasn't found in inventory")
    return dictionary
#Search (ask what they want to search by (effect or name) and print any weapons that fufil the requirements)

