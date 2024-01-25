import time
import os

# Dictionary to store radiation readings for different cities. Examples are already entered. 
readings_per_city = {"london" : [50, 10, 60, 20], 
                     "sydney" : [10, 20, 30, 40]}

# Function to display the main menu and get user input
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

# Function to clear the screen based on the OS type
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to add a new location (city) to the database
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

# Function to add a radiation reading for a specific city
def add_reading(location):
    try:
        radiation_reading = int(input(f"What was the radiation reading in {location.capitalize()}?\n"))
        readings_per_city[location].append(radiation_reading)
        clear_screen()
        print(f"Reading {radiation_reading} added for {location.capitalize()}.")
        time.sleep(1)
    except ValueError:
        print("Invalid input. Please enter a valid number.")   

# Function to handle data entry
def data_entry():
    while True:
        clear_screen()
        location = input("- Data Entry -\nEnter a reading or press enter to go back to menu.\nWhere did you gather this sample?\n").lower()
        if not location:
            break
        elif location not in readings_per_city: 
            clear_screen()
            add_location(location)
        else: 
            clear_screen()
            add_reading(location)

# Function to display data for each city
def data_per_city(): 
    while True: 
        available_cities = "\n".join(readings_per_city.keys())
        clear_screen()
        location = input (f"Which city do you want to see the data for? Press enter to go back to menu.\nAvailable cities:\n{available_cities}\n").lower()
        print (location)
        if location == "": 
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

# Function to handle data calculations
def data_calculations():
    while True: 
        clear_screen()
        continue_question2 = input ("- Data Calculations -\nDo you want to see data:\n1. Per City\n2. Total\n3. Back to menu\n")
        if continue_question2 == "1":
            data_per_city()
        elif continue_question2 == "2": 
            clear_screen()
            print(data_total())
            input("Press enter to return")
        elif continue_question2 == "3": 
            break
        else: 
            break

# Function to calculate total data across all cities
def data_total(): 
    total_sum = 0
    total_entries = 0
    min_entry = [10000, ""]
    max_entry = [0, ""]
    cities = 0
    for city in readings_per_city: 
        cities += 1
        total_sum = total_sum + sum(readings_per_city[city])
        total_entries = total_entries + len(readings_per_city[city])
        if max(readings_per_city[city]) > max_entry[0]: 
            max_entry[0] = max(readings_per_city[city])
            max_entry[1] = city
        if min(readings_per_city[city]) < min_entry[0]: 
            min_entry[0] = min(readings_per_city[city])
            min_entry[1] = city
    return_string = f'''- Total Data -
Cities entered: {cities}
Total entries: {total_entries}
Lowest entry: {min_entry[0]} in {min_entry[1].capitalize()}
Highest entry: {max_entry[0]} in {max_entry[1].capitalize()}
Total average: {total_sum / total_entries}
'''
    return return_string

# Function to retrieve data for a specific city
def city_data(location):
    city_data_return = []
    city_data_return.append(max(readings_per_city[location]))
    city_data_return.append(min(readings_per_city[location]))
    city_data_return.append(len(readings_per_city[location])) 
    city_data_return.append(sum(readings_per_city[location]) / len(readings_per_city[location]))
    #returns in order: highest, lowest, count, average
    return city_data_return

# Initialization message
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

# Main loop to run the program
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
