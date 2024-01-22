import random
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

count = 15
score = 0
words = ('''broad
cynical
approval
argument
cumbersome
gigantic
real
unkempt
nail
cattle
foregoing
animated
chin
charge
mass
zip
spring
silly
correct
penitent
secretive
sin
periodic
divide
start
bite-sized
eight
terrific
recognise
hateful
harm
throne
flower
trashy
hurt
fearful
eyes
maddening
stiff
concern
naive
finger
tie
lazy
adhesive
decisive
rural
cow
hat
object
welcome
girls
guitar
symptomatic
quill
ball
hunt
library
gaze
suck
depressed
ajar
heal
unhealthy
shoe
ski
count
system
stone
acoustic
skate
roof
clean
kittens
launch
fit
unite
aromatic
flavor
fire
kitty
thank
rush
tan
reminiscent
third
plausible
abounding
graceful
adaptable
fancy
stream
ill
cactus
cows
hellish
romantic
carriage
dust
digestion
''')
words_list = words.splitlines()

def current_highscore():
    high_score_path = "/Users/timonverbeek/Documents/Python/50.txt"

    with open(high_score_path, 'r') as file:
        high_score_content = file.read()
        return high_score_content

def update_highscore(highscore): 

    high_score_path = "/Users/timonverbeek/Documents/Python/50.txt"

    with open(high_score_path, 'r') as file:
        high_score_content = file.read()

    # Update the second character
    high_score_content = str(score)

    with open(high_score_path, 'w') as file:
        file.write(high_score_content)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_word(): 
    random_word = random.choice(words_list)
    words_list.remove(random_word)
    return random_word

def play_game():
    global score
    global count
    while True: 
        if len(words_list) != 0:
            start_time = int(time.time())
            current_word = pick_word()
            typed_word = input(f"Type the word within the time limit: {count} seconds.\nYour word is {current_word}\n")

            if typed_word == current_word: 
                end_time = int(time.time())
                if end_time - start_time < count:
                    score += 1
                    if score % 5 == 0: 
                        count -= 1
                    clear_screen()
                    print(f"Well done!\nYour current score is {score}")
                    time.sleep(1)
                    clear_screen()
                else: 
                    clear_screen()
                    print(f"Time's up. Your final score is {score}")
                    break
            else: 
                clear_screen()
                print(f"Too bad, better luck next time!\nYour final score is {score}")
                time.sleep(2)
                clear_screen()
                break
        else: 
            break
    if score > int(current_highscore()):
        update_highscore(score)
        print (f"Your score ({score}) is the new highscore, congratulations!")


input(f'''Welcome to the typing game.
The current highscore is {current_highscore()}.
Press enter to continue''')
clear_screen()
play_game()

while True:
    replay = input("Do you want to play again? (yes/no)\n")
    if replay != "": 
        replay = replay[0].lower()
        if replay == "y":
            score = 0
            count = 15
            clear_screen()
            input("Press enter to continue")
            clear_screen()
            play_game()
        elif replay == "n":
            clear_screen()
            print(f"Sad :-( Until next time!\nYour final score was {score}")
            time.sleep(5)
            clear_screen()
            break
    else: 
        clear_screen()
    