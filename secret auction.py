import os
import time

# To be printed later
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Empty dictionary to be updated later
bids = {}

# Function to update the bids dictionary with new bids
def dict_updater ( key , value ) :
    bids[key] = value

# Empty variables to start the auction
confirmation = ""
new_name = ""
new_bid = 0

print ( '''
Welcome to the super secret auction. Today you will be bidding on an ultra rare collectors item potentially worth thousands:
A copy of the original Shrek movie on DVD
When it's your turn to bid, please enter your name and the amount you wish to bid. Once bidding is done the winner will be announced immediately.''' )

# Simple while loop that will ask for new bids as long as "no" isn't entered
while confirmation != "no" : 
    new_name = input ( "What's your name?\n")
    new_bid = int ( input ( "What's your bid for the item?\n" ) )
    dict_updater ( new_bid , new_name )
    confirmation = input ( f'''Thank you for your bid {new_name}. 
Does anyone else wish to make a bid? Yes or no:\n''' ).lower()
    os.system('cls' if os.name == 'nt' else 'clear')

# Slamming of the gavel to close the auction
print ( f"{logo}")

time.sleep ( 1 )
os.system('cls' if os.name == 'nt' else 'clear')

# Prints out the highest value bid and who made it, thus the winner of the auction
print ( f'''
The auction is now closed
The winner of the auction is: { bids [ max ( bids.keys() ) ] }
Congratulations!
At £{ max ( bids.keys() ) } your bid was the highest!''') 
input ( "Press enter to clear" )
os.system('cls' if os.name == 'nt' else 'clear')


