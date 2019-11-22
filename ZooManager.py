import random

class Exhibit:
    def __init__(self, exhibit_type, name):
        self.exhibit_type = exhibit_type
        self.name = name
        self.animal_type = "none"
        self.animal_number = 0
    
    def can_place_animal(self, animal): #Check if a given animal can be placed in this exhibit
        if (self.animal_type == "none"): #If exhibit has no animals yet, check if it is the right type of exhibit
            if (animal == "elephant"):
                if (self.exhibit_type == "savannah"):
                    return True
                else:
                    print("Umm... an elephant can't be placed here. They need a Savannah exhibit.")
            if (animal == "lion"):
                if (self.exhibit_type == "savannah"):
                    return True
                else:
                    print("Umm... a lion can't be placed here. They need a Savannah exhibit.")
            if (animal == "polar bear"):
                if (self.exhibit_type == "arctic"):
                    return True
                else:
                    print("Umm... a polar bear can't be placed here. They need an Arctic exhibit.")
            if (animal == "penguin"):
                if (self.exhibit_type == "arctic"):
                    return True
                else:
                    print("Umm... a penguin can't be placed here. They need an Arctic exhibit.")
            if (animal == "whale"):
                if (self.exhibit_type == "ocean"):
                    return True
                else:
                    print("Umm... a whale can't be placed here. They need an Ocean exhibit.")
            if (animal == "dolphin"):
                if (self.exhibit_type == "ocean"):
                    return True
                else:
                    print("Umm... a dolphin can't be placed here. They need an Ocean exhibit.")
        else: #If exhibit has animals, check if they are the same type
            if (animal == self.animal_type):
                if (self.animal_number < 4): #Can only hold up to 4 animals
                    return True
                else:
                    print("Umm.. this " + animal + "can't be placed here. There are too many animals in this exhibit!")
            else:
                print("Umm... this " + animal + " can't be placed here. This is the " + self.animal_type + " exhibit!")
        return False
    
    def place_animal(self, animal): #Place an animal in the exhibit
        if (self.animal_type == "none"):
            self.animal_type = animal
        self.animal_number += 1

    def print_status(self): #Display name and animals
        if self.animal_number == 0:
            print(self.name + " - 0 animals")
        else:
            print(self.name + " - " + str(self.animal_number) + " " + self.animal_type + "(s)")

def random_animal(): #Generate random animal out of 6 options
    num = random.randint(1, 6)
    if (num == 1):
        return "elephant"
    elif (num == 2):
        return "lion"
    elif (num == 3):
        return "polar bear"
    elif (num == 4):
        return "penguin"
    elif (num == 5):
        return "whale"
    else:
        return "dolphin"

def make_selection(): #Convert user input to selection number
    while (True): #Continue running until valid input causes return
        for exhibit in list_of_exhibits:
            exhibit.print_status() #Display the status of every exhibit
        user_input = input()
        if (user_input == "a"):
            return 0
        elif(user_input == "b"):
            return 1
        elif(user_input == "c"):
            return 2
        elif(user_input == "d"):
            return 3
        elif(user_input == "e"):
            return 4
        elif(user_input == "f"):
            return 5
        elif(user_input == "exit"):
            exit()
        else:
            print("Invalid input. Select an exhibit:")
    
list_of_exhibits = [] #Create list of exhibits
list_of_exhibits.append(Exhibit("savannah", "Savannah 1 (a)"))
list_of_exhibits.append(Exhibit("savannah", "Savannah 2 (b)"))
list_of_exhibits.append(Exhibit("arctic", "Arctic 1 (c)"))
list_of_exhibits.append(Exhibit("arctic", "Arctic 2 (d)"))
list_of_exhibits.append(Exhibit("ocean", "Ocean 1 (e)"))
list_of_exhibits.append(Exhibit("ocean", "Ocean 2 (f)"))

#Run program
print("Welcome to the Zoo Management System")
while (True):
    new_animal = random_animal() #Give user a random animal
    keep_trying = True
    while (keep_trying): #Keep looping until animal is placed correctly
        print("A new " + new_animal + " is ready to be placed. Select an exhibit:")
        selection = make_selection() #Get selection from user converted into number
        exhibit = list_of_exhibits[selection]
        if (exhibit.can_place_animal(new_animal)): #Check if animal can be placed in exhibit
            exhibit.place_animal(new_animal)
            print("Fantastic! The new " + new_animal + " seems pleased with his new home!")
            keep_trying = False #Animal is placed, break out of loop