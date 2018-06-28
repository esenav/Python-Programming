"""
Hangman.py
Hangman game
Created by Evaldas Senavaitis
"""
import random, sys

def generating(secret_word, lives):
    """
    secret_word: is our word which we have to guess
    lives: is the number of lifes we have when we choose our level
    game_state: is a dictonary object which was told us in the task
    returns a dictonary object for the whole game to be executed
    """
    # generating dictonary object as it was asked to do so and then returning it as global variable
    game_state = {'word':secret_word, 'lives':lives, 'secret_guess': ['*'] * len(secret_word), 'used':[]}
    return game_state

def won_game(game_state):
    """
    won_game function is used to check whenever is game is won or not
    game_state :a dictonary object from a generating function
    returns if game is won or not
    """
    # If there are no '*' in a 'secret_guess' game is won
    return '*' not in game_state['secret_guess']

def lives_remaining(game_state):
    """
    lives_remaining just returns a number of lives remaining
    game_state :a dictonary object from a generating function
    returns lifes left
    """
    return game_state['lives']

def secret_word(game_state) :
    """
    secret_word returns a secret word in a case of '*'
    game_state: a dictonary object from a generating function
    returns word with '*'
    """
    return game_state['secret_guess']

def remaining_game(game_state) :
    """
    remaining_game function is used to return a nice format of the game for the user
    game_state: a dictonary object from a generating function
    returns a neatly looking game
    """
    return "WORD: {}; you have {} lives left".format(''.join(game_state['secret_guess']), game_state['lives'])

def updating(game_state, so_far) :
    """
    updating functions checks the inputed letter
    game_state: is game from play_game
    so_far: is current_guess which is inputed by the user
    returns most difficult game part of changing the '*' with a letter
    """
    # This checks if guessed letter in a word is in a secret word and automaticly it is added to a used list
    # If the letter is already used no lives will be decremented
    # if letter is not in the word it is going to be added to a list and one life will be decremented
    if so_far in game_state['word'] and so_far not in game_state['used']:
        for i, wrong in enumerate(game_state['word']):
            if wrong==so_far:
                game_state['secret_guess'][i]=so_far
                game_state['used']+=so_far
    elif so_far in game_state['used']:
        print("Letter was already used no lives decremented")
    else:
        print("Letter does not occur in the word")
        game_state['used']+=so_far
        game_state['lives']-=1

def play_game(word, lives):
    """
    play_game function generates the whole game, checks if the game is won or not
    word: is taken as random_word which was randomly picked from a file of words
    lives: is a number of lives depending on a level
    returns a guessed letter how many times it occurs in a word and if the game is won or not
    """
    # Ask for user to input a letter, takes generating function from above to check word and lifes then prints out appropriate messages
    game=generating(word, lives)
    while lives_remaining(game)>0 and not won_game(game):
        print(remaining_game(game))
        current_guess = str(input("Guess a letter: "))
        # Checks if a letter is upper case or not
        while current_guess.isupper()!= True:
            if current_guess.isdigit() or current_guess.islower():
                current_guess = input("Invalid input, please try again to input upper case letter:")
        updating(game, current_guess)
        # Prints a inputed letter and counts how many times it occurs in the word
        if current_guess in game['word']:
            print("Letter", current_guess,"occurs", game['secret_guess'].count(current_guess),"in word")
    # If Word is guessed launches won_game function
    if won_game(game):
        print("You guessted the word correctly",game['word'])
    # If there is no lifes left you lost the game
    elif game['lives']==0:
        print("You out of lives and you lost the word was:", game['word'])

def Main():
    """
    Main function is used just to play game again when game is ended its more efficent then a while loop
    """
    
    try:
        #opens a file reads, splits it and random picks it from a file
        print("Welcome to the HangMan game! Good luck!")
        fileN=input("Please enter file name:")
        fileName=open(fileN)
        read_file=fileName.read().split()
        random_word=random.choice(read_file)
    except IOError as e :
        print("Invalid input")
        sys.exit()
    #Ask user to choose a level of difficulty
    print("Choose level difficulty from easy, intermediate and hard")
    level=str(input("Write your chosen level:"))
    if (level!="easy" and level!="intermediate" and level!="hard"):
        level=input("Invalid input please try again:")
    if level=="easy":
        print("You have chosen Easy mode")
        lives=10
        play_game(random_word, lives)
    if level=="intermediate":
        print("You have chosen Intermediate mode")
        lives=7
        play_game(random_word, lives)
    if level=="hard":
        print("You have chosen Hard mode")
        lives=5
        play_game(random_word, lives)
    # Ask a user to play game again or not 
    print("If you want to play again enter Yes if not No")
    playAgain=input("Yes or No? :")
    if playAgain=="Yes":
        Main()
    else:sys.exit()
Main()
    
