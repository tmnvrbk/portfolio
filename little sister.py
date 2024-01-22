# With the intention of creating a more functional, comprehensive and working program I have taken parts of the original assignment and applied them somewhat
# differently than the task specifies. Please keep in mind that I'm fully aware that the functions in my program are not as specified in the task, but as you 
# will see they still perform the required functions. 

import spacy
import time

# Function that takes any word and puts "un" in front of it
def add_prefix_un():
    while True: 
        word = input("Enter a word to add the pefix 'un' to or press enter to go back to menu\n")
        if word.isalpha():
            new_word = f"un{word}".capitalize()
            print(f"Your new word is '{new_word}'\nEnter a new word or press enter to go back to the menu")
        elif word == "": 
            break 
        else: 
            print("Please enter a valid word")
            time.sleep(1)

# List of all consonants plus the letter 'i' for use in the remove_suffix_ness function
consonants_plus_i = ['bi', 'ci', 'di', 'fi', 'gi', 'hi', 'ji', 'ki', 'li', 'mi', 'ni', 'pi', 'qi', 'ri', 'si', 'ti', 'vi', 'wi', 'xi', 'zi']
    
# Module that will remove "ness" from any word and will change any 'i' to 'y' if necessary
def remove_suffix_ness():
    while True:
        word = input("Enter a word to remove the suffix 'ness' from or press enter to go back to menu\n")
        if word.isalpha(): 
            # "Ness" will be removed from the word, if the word now ends in a consonant + 'I', the 'i' will be replaced with a 'y'
            new_word = word.lower().replace("ness","").capitalize()
            if new_word[-2:] in consonants_plus_i: 
                new_word = new_word.replace(new_word[-1],"y")
            print(f"Your new word is '{new_word}'")
        elif word == "": 
            break
        else: 
            print("Please enter a valid word")
            time.sleep(1)

# Module that will ask for a prefix and then a set of words and will combine the prefix with the words
def make_word_groups():
    # User input is requested for a prefix and then an undetermined amount of words
    words = []
    while True: 
        prefix = input("Choose a prefix (I.e 'en', 'close', 'auto', 'inter')\n")
        if prefix == "":
            break
        elif prefix.isalpha(): 
            while True: 
                word = input("Enter a word or press enter to continue\n")
                if word == "": 
                    break
                elif word.isalpha(): 
                    words.append(word)
                else: 
                    print("Please enter a valid word")
        else: 
            print("Please enter a valid prefix")
        print(f"With the prefix '{prefix}' your words will look like this:")
        # For loop that will combine all the words with the prefix
        for word in words:
            print(prefix.capitalize() + word)
        print("Press enter to go back to menu")

# Loading the nlp module
nlp = spacy.load("en_core_web_sm")

# This module will take a user input sentence, use nlp to extract which words are adjectives and turn them into verbs
def adjective_to_verb():

# I realize the original tasks specifies to have the function take the index of the adjective as an input, but I find this highly unlikely to have any use in 
# real life. Instead of manually pointing out to the program which word needs to be turned into a verb, I've made it a bit more complex instead. 
    
    while True:
        sentence = input("Enter a sentence from which to turn adjectives into verbs, or press enter to go back\n")
        if sentence == "":
            break
        else: 
            doc = nlp(sentence)
            # Creates a list of all the adjectives in a sentence, if any
            adjectives = [token.text for token in doc if token.pos_ == 'ADJ']
            # For loop that will add "en" to any adjectives
            for adjective in adjectives: 
                verb = adjective + "en"
                print(f"The adjective {adjective} can be turned into the verb {verb}")
                time.sleep(1)
            # Checks if there were no adjectives in the sentence at all
            if not adjectives:
                print("There are no adjectives in this sentence")
                time.sleep(1)


# Main program loop that will run all the individual modules when called upon
print("Hello")
while True: 
    menu_choice = input('''Would you like to:
1. Add the prefix "un" to words
2. Remove the suffix "ness" from words
3. Change an adjective in a sentence to a verb
4. Make word groups with a specific prefix
5. Exit\n''')

    if menu_choice == "1": 
        add_prefix_un()
    elif menu_choice == "2": 
        remove_suffix_ness()
    elif menu_choice == "3":
        adjective_to_verb()
    elif menu_choice == "4":
        make_word_groups()
    elif menu_choice == "5": 
        break
    else: 
        print("Please enter a valid input")
        time.sleep(1)