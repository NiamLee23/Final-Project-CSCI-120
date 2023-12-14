import random

#rounds = int(input("How many times do you want to guess numbers?"))  # Asks how many times a player wants to play the guessing game

def guess_game(lowerBound,upperBound, guess, correctValue):
############## Defining the valueplayers are trying to guess based on their range ##############
    
 
    # lowerBound = int(input("What number do you want the lower boundary to be?"))  # Asks player to define lower and upper boundaries
    # upperBound = int(input("What number do you want the upper boundary to be?"))

    playerGuesses = []  # Initialize list to track player's guesses
    print('value to be guessed', correctValue)
    print('your guess', guess)

    ############## Defining Messages ####################
    w1 = "You're very warm"  # warmest guess without being correct
    w2 = "You're warm"  # Second warmest guess without being correct
    n = "You're not hot or cold"  # If the guess is inbetween the minimum or maximum and the correct value
    c2 = "You're getting cold"  # second coldest guess without being correct
    c1 = "Youre very cold"  # coldest guess withoyt being correct
    correct = "Yay! You guessed the number!"

############## Mapping Guesses To Messages ##########

    differenceBetweenGuessAndCorrect = guess - correctValue

    if abs(differenceBetweenGuessAndCorrect) == 1:
        return w1

    elif abs(differenceBetweenGuessAndCorrect) == 2:
        return w2
    
    elif abs(differenceBetweenGuessAndCorrect) >= 3 and abs(differenceBetweenGuessAndCorrect) <= 5:
        return c2
    
    elif abs(differenceBetweenGuessAndCorrect) > 5:
        return c1
    
    elif differenceBetweenGuessAndCorrect == 0:
        return correct
