# Problem Set 2, hangman.py
# Name: Kunal
# Collaborators:
# Time spent: 240 - 300min

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    for i in secret_word:
        if i in letters_guessed:
            count += 1
    if count == len(secret_word):
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    str = ""
    for i in secret_word:
        if i in letters_guessed:
            str += i
        else:
            str += "_ "
    return str



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_available = string.ascii_lowercase
    for i in letters_guessed:
        if i in letters_available:
            letters_available = letters_available.replace(i, '')
    return letters_available
   
def get_total_score(guesses_left, secret_word):
    '''
    guesses_left: integer, number of guesses left
    secret_word: string, the word the user is guessing
    returns: integer, the total score of the player
    '''
    str = ""
    for i in secret_word:
        if i not in str:
            str += i
    total_score = guesses_left * len(str)
    return total_score
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''    
    no_of_guesses = 6
    no_of_warnings = 3
    vowels = "aeiou"
    #secret_word = "panda"
    letters_available = string.ascii_lowercase
    l = []
    
    print("Welcome to the game of Hangman!")
    print("I am thinking of a word  that is", len(secret_word), "letters long.")
    
    while True:
        print("------------------")
        
        if is_word_guessed(secret_word, l):
            print("Congratulations, you won!")
            print("Your total score for this game is:", get_total_score(no_of_guesses, secret_word))
            break
        
        if no_of_guesses <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
            

        if(no_of_guesses == 1):
            print("You have", no_of_guesses, "guess left.")
        
        else:
            print("You have", no_of_guesses, "guesses left.")
       
        print("Available letters:", letters_available)
        ch = input("Please guess a letter: ")
    
        if(str.isalpha(ch)):
            ch = ch.lower()
           
            if (ch in l):
                l.append(ch)
            
                if(no_of_warnings > 0):
                    no_of_warnings -= 1
                    print("Oops! You've already guessed that letter. You now have", no_of_warnings, "warnings:", get_guessed_word(secret_word, l))
                
                else:
                    no_of_guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess", get_guessed_word(secret_word, l))
           
            elif (ch not in secret_word):
                print("That letter is not in my word:", get_guessed_word(secret_word, l))
                l.append(ch)
                no_of_guesses -= 1
                
                if(ch in vowels):
                    no_of_guesses -= 1    
            
            else:
                l.append(ch)
                print("Good guess: ", get_guessed_word(secret_word, l))
                
            letters_available = get_available_letters(l)
            
        else:
            
            if(no_of_warnings > 0):
                no_of_warnings -= 1
                print("Oops! That is not a valid letter. You have", no_of_warnings, "warnings left:", get_guessed_word(secret_word, l))
            
            else:
                no_of_guesses -= 1
                print("Oops! That is not a valid letter.", get_guessed_word(secret_word, l))
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '').strip()
    other_word = other_word.strip()
    letters_guessed = []
    
    for i in my_word:
        if str.isalpha(i):
            letters_guessed.append(i)
    
    if(len(my_word) != len(other_word)):
        return False
    
    for i in range(len(my_word)):
        if str.isalpha(my_word[i]):
            if my_word[i] != other_word[i]:
                return False
            else:
                if my_word[i] == '_' and other_word[i] in letters_guessed:
                    return False
    
    return True
            

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matches.append(word)
    
    if len(matches) == 0:
        print("No matches found.")
    else:
        for i in matches:
            print(i, end = ' ')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    no_of_guesses = 6
    no_of_warnings = 3
    vowels = "aeiou"
    #secret_word = "panda"
    letters_available = string.ascii_lowercase
    l = []
    
    print("Welcome to the game of Hangman!")
    print("I am thinking of a word  that is", len(secret_word), "letters long.")
    
    while True:
        print("------------------")
        
        if is_word_guessed(secret_word, l):
            print("Congratulations, you won!")
            print("Your total score for this game is:", get_total_score(no_of_guesses, secret_word))
            break
        
        if no_of_guesses <= 0:
            print("Sorry, you ran out of guesses. The word was", secret_word)
            break
            
        if(no_of_guesses == 1):
            print("You have", no_of_guesses, "guess left.")
        
        else:
            print("You have", no_of_guesses, "guesses left.")
       
        print("Available letters:", letters_available)
        ch = input("Please guess a letter: ")
    
        if(str.isalpha(ch)):
            ch = ch.lower()
           
            if (ch in l):
                l.append(ch)
            
                if(no_of_warnings > 0):
                    no_of_warnings -= 1
                    print("Oops! You've already guessed that letter. You now have", no_of_warnings, "warnings:", get_guessed_word(secret_word, l))
                
                else:
                    no_of_guesses -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess", get_guessed_word(secret_word, l))
           
            elif (ch not in secret_word):
                print("That letter is not in my word:", get_guessed_word(secret_word, l))
                l.append(ch)
                no_of_guesses -= 1
                
                if(ch in vowels):
                    no_of_guesses -= 1    
            
            else:
                l.append(ch)
                print("Good guess: ", get_guessed_word(secret_word, l))
                
            letters_available = get_available_letters(l)
            
        else:
            if ch == '*':
                my_word = get_guessed_word(secret_word,l)
                show_possible_matches(my_word)
            
            else:
                if(no_of_warnings > 0):
                    no_of_warnings -= 1
                    print("Oops! That is not a valid letter. You have", no_of_warnings, "warnings left:", get_guessed_word(secret_word, l))
            
                else:
                    no_of_guesses -= 1
                    print("Oops! That is not a valid letter.", get_guessed_word(secret_word, l))

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
