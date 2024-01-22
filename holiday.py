# User gets to make a few inputs, then gets to confirm theses, if is not confirmed the loop continues until confirmed
# Similarly if at the end of the while loop the user does not confirm the inputs and the subsequent print the loop will restart


# several functions defined for later use
# calculates cost of hotel by inputting the amount of nights the user wishes to stay
def hotel_cost (nights):
    total_hotel_cost = nights * 50
    return total_hotel_cost

#calculates the cost of the plane ticket depending on where the user wishes to go
def plane_cost (city): 
    if city == cities [0]:
        cost = 100
    elif city == cities [1]: 
        cost = 500
    elif city == cities [2]: 
        cost = 300
    return cost

#calculates the cost of car rental based on amount of days user wishes to rent
def car_rental (day): 
    cost = 100 * day 
    return cost

#Calculates the complete cost of the holiday by inputting variables that will call upon the previous 3 functions for a total amount
def holiday_cost (hotel_nights, plane, rental_days): 
    total_cost = car_rental(rental_days) + plane_cost(plane) + hotel_cost(hotel_nights)
    return total_cost



confirmation = "n"
final_confirmation = ""

while final_confirmation != "confirm": 

    while confirmation[0].lower() == "n": 
        
        cities = ["Rome", "Naples", "Valencia"]
        city_flight = ""

        # ask for user input of a city, repeats until a valid city from the list of available cities is chosen

        while city_flight not in cities:
            city_flight = input(f'''\nChoose from the following options: \n{", ".join(cities)}\n''')
            if city_flight not in cities:
                print("That's not an option ")

        # Requests nights the user wishes to stay, loops until a number is entered

        num_nights = ""
        num_nights = input("\nHow many nights do you want to stay?\n")
        while not num_nights.isnumeric() or int (num_nights) < 0: 
            num_nights = input("\nPlease enter a valid number\n")
        num_nights = int (num_nights)

        # requests how many days the user wants a rental car, loops until a number is entered

        rental_days = input("\nFor how many days do you need a rental car? Enter 0 if you do not need a rental car.\n")
        while not rental_days.isnumeric(): 
            rental_days = input("\nPlease enter a valid number. \nFor how many days do you need a rental car?\n")

        # creates a string for later print use depending on if the user wants a car or not
        
        rental_days_string = ""
        if rental_days != "0": 
            rental_days_string = f"You need a rental car for {rental_days} days"
        elif rental_days == "0": 
            rental_days_string = f"You do not need a rental car" 
        rental_days = int (rental_days)
        
        print(f'''\nYou want to stay in {city_flight} for {num_nights} nights.\n{rental_days_string}''')
        
        confirmation = input("Is this correct? Yes to continue or no to start over.\n")
    if confirmation[0].lower() == "y": 
        print("Thank you")
    

    print(f'''\nThe cost of the hotel will be {hotel_cost(num_nights)}.
    The airplane ticket will cost {plane_cost(city_flight)}''')
    if car_rental(rental_days) > 0:
        print(f"Your car rental will cost {car_rental(rental_days)}")


    # creates 2 alternative strings to print later on depending on whether or not the user chose to have a rental car earlier in the program

    if rental_days > 0: 
        rental_days_string = f" and you will have a rental car for {rental_days} days"
    else: 
        rental_days_string = ""

   
    final_confirmation = input("Type confirm to book your holiday, or anything else to start over: \n").lower()
    if final_confirmation != "confirm": 
        confirmation = "n"


# print of all the user inputs after being processed by the functions


print(f"\nYour holiday is booked, you are going to {city_flight} for {num_nights} nights{rental_days_string}. The total cost of your holiday will be £{holiday_cost(num_nights , city_flight , rental_days) }."
       f"\nThank you for booking with Dodo Airlines and we hope you'll enjoy your getaway!")


