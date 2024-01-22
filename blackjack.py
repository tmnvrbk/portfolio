import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

#Creating a list of all potential cards

card_values = [ "Ace" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "Jack" , "Queen" , "King" ]
cards_list = []
decks = 2   # change to input later to make it user-defined

for _ in range(decks):
    for card in card_values:
        cards_list.append(f"{card} of Hearts")
        cards_list.append(f"{card} of Clubs")
        cards_list.append(f"{card} of Spades")
        cards_list.append(f"{card} of Diamonds")

#creating a dictionary of all cards with numbers as keys to be referenced later by RNG
    
card_number = 0
adjustable_deck = {}

for card in cards_list : 
    card_number += 1
    adjustable_deck [ str ( card_number ) ] = card

# request input for the amount of players

amount_of_players = input ( "How many players are there? (1-5)\n" )
while not amount_of_players.isdigit() or int ( amount_of_players ) > 5 : 
    amount_of_players = input ( "Please enter a valid number between 1-5:\n" )

amount_of_players = int ( amount_of_players )
os.system('cls' if os.name == 'nt' else 'clear')

#creating dictionaries for the dealer and for the amount of players chosen to track gamestates later on
#All players initially get £5000 to spend

player_dictionaries = {
    "Dealer" : { "bust" : False , 
                "total" : 0 ,
                "ace" : False , 
                "stand" : False ,
                "cards" : [] , 
                "bet" : 0 ,
                "broke" : False
                }
}
for player in range ( 1 , amount_of_players + 1 ) : 
    player_dictionaries [ f"Player {player}" ] = { "bust" : False , 
                                                "total" : 0 ,
                                                "ace" : False , 
                                                "stand" : False ,
                                                "cards" : [] , 
                                                "bet" : 0 , 
                                                "win" : False , 
                                                "funds" : 5000 ,
                                                "broke" : False
                                                }
   





#function to get the card value from an assigned card later on
#Ace value as 1 or 11 gets handled later 
    
random_number = None
def get_value ( cardname ):
    cardname_split_list = cardname.split()
    if cardname_split_list[0].isdigit() : 
        card_value_number = int ( cardname_split_list [0] )
    elif cardname_split_list [0] in ["King" , "Queen", "Jack" ] :
        card_value_number = 10
    else :
        card_value_number = 11
    return int ( card_value_number )

#function that can be called to deal an extra card to any player or dealer

def deal_a_card ( player ) :
        """
        Floob
        """

        random_number = random.choice ( list ( adjustable_deck.keys() ) )
        random_number = str (random_number)
        player_dictionaries [ player ] [ "total" ] = player_dictionaries [ player ] [ "total" ] + get_value ( adjustable_deck [ random_number ] )
        player_dictionaries [ player ] [ "cards" ].append ( adjustable_deck [ random_number ] )
        if get_value ( adjustable_deck [ random_number ] ) == 11 :
            player_dictionaries [ player ] [ "ace" ] = True
        adjustable_deck.pop(f"{ random_number }")






#nested while/if/elif loops to make the dealer automatically draw cards until either == 21, > 17 or busted
#players then get the chance to hit or stand. Players automatically win if dealer busts. 
play_again = "yes"

while play_again.lower() == "yes" : 

    #request bets from players, max their total funds, min 0

    for player in player_dictionaries:
        if player != "Dealer" and not player_dictionaries [ player ] [ "broke" ]  :
            funds = player_dictionaries [ player ][ "funds" ]

            while True:
                bet = input(f"{player}, your funds are {funds}. How much do you want to bet?\n")

                if bet.isdigit() and 0 < int ( bet ) <= funds :
                    player_dictionaries [ player ] [ "bet" ] = int(bet)
                    print("Your bet has been placed")
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print("Please enter a valid amount, lower than your total funds.")

    #deal two cards to each player to initiate the game

    for _ in range ( 2 ) :
        if player_dictionaries [ player ] [ "broke" ] != True :
            for player in player_dictionaries : 
                deal_a_card ( player )


    hit_or_stand = ""
    for player in player_dictionaries : 
        #Will make the dealer draw to at least 18 or bust
        if player == "Dealer" : 
            while not player_dictionaries [ player ] [ "stand" ] and not player_dictionaries [ player ] [ "bust" ] :
                    if player_dictionaries [ player ] [ "total" ] == 21 : 
                        player_dictionaries [ player ] [ "stand" ] = True
                        print ( "Dealer has Blackjack\n")
                    elif player_dictionaries [ player ] [ "total" ] < 18 : 
                        deal_a_card ( player )
                    elif player_dictionaries [ player ] [ "total" ] > 21 : 
                        player_dictionaries [ player ] [ "bust" ] = True
                        print ( "Dealer has busted\n" )
                        for player in player_dictionaries : 
                            if player != "Dealer" : 
                                player_dictionaries [ player ] [ "win" ] = True
                    else :
                        player_dictionaries [ player ] [ "stand" ] = True
        if player != "Dealer" :
            while not player_dictionaries [ player ] [ "stand" ] and not player_dictionaries [ player ] [ "bust" ] and not player_dictionaries [ "Dealer" ] [ "bust" ] and not player_dictionaries [ player ] [ "broke" ] :
                    hit_or_stand = input (f'''{ player } your total is { player_dictionaries [ player ] [ 'total' ] } 
The dealer's total is { player_dictionaries [ "Dealer" ] [ "total" ] }
Your cards are {', '.join(player_dictionaries [ player ] [ 'cards' ])} 
Do you want to hit or stand?
''')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if hit_or_stand.lower() == "hit" :
                        deal_a_card ( player )
                        if player_dictionaries [ player ] [ "total" ] > 21 : 
                            if player_dictionaries [ player ] [ "ace" ] : 
                                player_dictionaries [ player ] [ "total" ] = player_dictionaries [ player ] [ "total" ] - 10
                                player_dictionaries [ player ] [ "ace" ] = False
                            else :
                                player_dictionaries [ player ] [ "bust" ] = True
                                print ( "You busted" )
                        elif player_dictionaries [ player ] [ "total" ] == 21 : 
                            player_dictionaries [ player ] [ "stand" ] = True
                            player_dictionaries [ player ] [ "win" ] = True
                            print ( "Blackjack!" )
                    elif hit_or_stand.lower() == "stand" : 
                        player_dictionaries [ player ] [ 'stand' ] = True
                    hit_or_stand = ""

    for player in player_dictionaries : 
        if player_dictionaries [ player ] [ "broke" ] != True :
            print (f"{ player }'s total is { player_dictionaries [ player ] [ 'total' ] }\n" )

#Determine if the player won or lost

    for player in player_dictionaries : 
        if player != "Dealer" and player_dictionaries [ player ] [ "bust" ] != True and player_dictionaries [ player ] [ "broke" ] != True : 
            if player_dictionaries [ player ] [ "total" ] >= player_dictionaries [ "Dealer" ] [ "total" ] :
                player_dictionaries [ player ] [ "win" ] = True


    for player in player_dictionaries :
        if player != "Dealer" and player_dictionaries [ player ] [ "broke" ] != True  : 
            if player_dictionaries [ player ] [ "win" ] == True :
                player_dictionaries [ player ] [ "funds" ] += player_dictionaries [ player ] [ "bet" ]
                print (f'''Congratulations { player } You won.
Your bet of £{ player_dictionaries [ player ] [ "bet" ]} was doubled.
Your total funds are now £{ player_dictionaries [ player ] [ "funds" ] }
''')
            else : 
                player_dictionaries [ player ] [ "funds" ] -= player_dictionaries [ player ] [ "bet" ]
                print ( f'''I'm sorry { player } you lost your bet of £{ player_dictionaries [ player ] [ "bet" ] }.
    Your total is now £{ player_dictionaries [ player ] [ "funds" ] }
''' ) 
                if player_dictionaries [ player ] [ "funds" ] <= 0 :
                    player_dictionaries [ player ] [ "broke" ] = True 
                    print ( player_dictionaries [ player ] [ "broke" ] )
    while True:
        play_again = input("Do you wish to play again? (yes/no):\n")
        if play_again.lower() == "yes": 
            for player in player_dictionaries : 
                player_dictionaries [ player ] [ "stand" ] = False
                player_dictionaries [ player ] [ "bust" ] = False
                player_dictionaries [ player ] [ "ace" ] = False
                player_dictionaries [ player ] [ "total" ] = 0
                player_dictionaries [ player ] [ "cards" ] = []
                player_dictionaries [ player ] [ "bet" ] = 0
                player_dictionaries [ player ] [ "win" ] = False
        if play_again.lower() in ["yes", "no"]:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'\n")
else : 
    print ( "Thank you for playing today. Your payouts are:" )
    for player in player_dictionaries : 
        if player != "Dealer" : 
            print ( f"{player} cashes out {player_dictionaries [ player ] [ 'funds' ] }")



