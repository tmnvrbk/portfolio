import time
import os


readings_per_city = {"london" : [50, 10, 60, 20], 
                     "sydney" : [10, 20, 30, 40]}
def opening_menu():

    while True: 
        try: 
            clear_screen()
            menu_selections = int(input("Welcome to the Radiation Database. Please select from the following menu:\n1. Data Entry\n2. Data Calculations\n3. Exit\n"))
            if 1 <= menu_selections <= 3:
                return menu_selections
            else: 
                print("Invalid number. Please choose between 1 and 3")
         
        except ValueError: 
            print("That ain't a valid number buddy boy. Please enter a number")
            time.sleep(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_location(location):
    while True:
        choice = None
        choice = input(f"You chose {location.capitalize()}, this city does not yet exist in the database. Do you wish to add it? (Y/N)\n").lower()
        if choice == "y":
            clear_screen()
            print (f"The city {location.capitalize()} has been added")
            readings_per_city[location] = []
            add_reading(location)
            break
        elif choice == "n": 
            print("Please choose a different city")
            time.sleep(1.5)
            break
        else:
            clear_screen()
            print("Please choose yes or no to continue")

def add_reading(location):
    try:
        radiation_reading = int(input(f"What was the radiation reading in {location.capitalize()}?\n"))
        readings_per_city[location].append(radiation_reading)
        clear_screen()
        print(f"Reading {radiation_reading} added for {location.capitalize()}.")
        time.sleep(1)
    except ValueError:
        print("Invalid input. Please enter a valid number.")   

def data_entry():
    continue_question = input("You chose Data Entry. Press enter to continue or type anything else to go back to menu\n")
    while True:
        if not continue_question: 
            clear_screen()
            location = input("Enter a reading or type exit to go back to menu.\nWhere did you gather this sample?\n").lower()
            if location == "exit":
                break
            elif location not in readings_per_city: 
                clear_screen()
                add_location(location)
            else: 
                clear_screen()
                add_reading(location)
        else: 
            break

def data_per_city(): 
    while True: 
        available_cities = "\n".join(readings_per_city.keys())
        clear_screen()
        location = input (f"Which city do you want to see the data for? Press enter to go back to menu.\nAvailable cities:\n{available_cities}\n").lower()
        print (location)
        if location.lower() == "": 
            break
        elif location in available_cities: 
            chosen_city_data = city_data(location)
            clear_screen()
            print(f'''For your chosen city {location.capitalize()} the available data is as follows:
                The highest reading in {location.capitalize()} is {chosen_city_data[0]}.
                The lowest reading in {location.capitalize()} is {chosen_city_data[1]}.
                The total number of readings in {location.capitalize()} is {chosen_city_data[2]}.
                The average of all readings in {location.capitalize()} is {chosen_city_data[3]}.
                ''')
            input ("Press enter to continue") 
        else: 
            print ("Please enter a valid city")



def data_calculations():
    continue_question1 = input("You chose Data Calculations. Press enter to continue or type anything else to go back to menu\n")
    while True: 
        if not continue_question1: 
            clear_screen()
            continue_question2 = ""
            continue_question2 = input ("Do you want to see data:\n1. Per City\n2. Total\n3. Back to menu\n")
            while True: 
                continue_question2 == ""
                if continue_question2 == "1":
                   data_per_city()
                elif continue_question2 == "3": 
                    break
                else: 
                    break
        else: 
            break


def city_data(location):
    city_data_return = []
    city_data_return.append(max(readings_per_city[location]))
    city_data_return.append(min(readings_per_city[location]))
    city_data_return.append(len(readings_per_city[location])) 
    city_data_return.append(sum(readings_per_city[location]) / len(readings_per_city[location]))
    #returns in order: highest, lowest, count, average
    return city_data_return


        

text = "Initializing....."
iteration = 0
text_list = []
while True:
    text_list.append(text[iteration: iteration + 1])
    print("".join(text_list))
    iteration += 1
    time.sleep(0.05)
    os.system('cls' if os.name == 'nt' else 'clear')

    if iteration >= len(text): 
        break
print ("".join(text_list))

while True: 
    choice = opening_menu()
    if choice == 1: 
        clear_screen()
        data_entry()
    elif choice == 2: 
        clear_screen()
        data_calculations()
    elif choice == 3: 
        print("Goodbye") 
        break
    


print (readings_per_city)



            