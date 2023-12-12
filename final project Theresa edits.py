import random

#rounds = int(input("How many times do you want to guess numbers?"))  # Asks how many times a player wants to play the guessing game

def guess_game(lowerBound,upperBound, guess, correctValue):
############## Defining the valueplayers are trying to guess based on their range ##############
    
 
    # lowerBound = int(input("What number do you want the lower boundary to be?"))  # Asks player to define lower and upper boundaries
    # upperBound = int(input("What number do you want the upper boundary to be?"))

    playerGuesses = []  # Initialize list to track player's guesses
    print('value to be guessed', correctValue)
    print('your guess', guess)

    ############## Identifying Quartiles ################
    quarterOfRange = upperBound / 4
    firstQuartile = int(quarterOfRange + lowerBound)
    median = int(quarterOfRange + firstQuartile)
    thirdQuartile = int(quarterOfRange + median)
    fourthQuartile = int(upperBound - quarterOfRange)

    ############## Ranges of the Quartiles ##############
    minimum = lowerBound
    firstQRange = range(firstQuartile, median)
    secondQRange = range(median, thirdQuartile)
    thirdQRange = range(thirdQuartile, upperBound)
    maximum = upperBound

    ############## Defining Messages ####################
    w1 = "You're very warm"  # warmest guess without being correct
    w2 = "You're warm"  # Second warmest guess without being correct
    n = "You're not hot or cold"  # If the guess is inbetween the minimum or maximum and the correct value
    c2 = "You're getting cold"  # second coldest guess without being correct
    c1 = "Youre very cold"  # coldest guess withoyt being correct
    correct = "Yay! You guessed the number!"

    ############## Mapping Guesses To Messages ##########
    # guess = int(input("What do you think the correct number is?"))

    
    if guess == correctValue:
        return 'You got it right'
    if correctValue == minimum:  # If the correct value is the lowest possible number in range then this is how the messages will map to the guesses
        if guess == minimum:
            return correct
        elif guess in firstQRange:
            return w1
        elif guess in secondQRange:
            return w2
        elif guess in thirdQRange:
            return n
        elif guess == maximum:
            return c2

    elif correctValue in firstQRange:
        if guess == minimum:
            return w2
        elif guess in firstQRange and guess != correctValue:
            return w1
        elif guess in firstQRange and guess == correctValue:
            return correct
        elif guess in secondQRange:
            return w2
        elif guess in thirdQRange:
            return n
        elif guess == maximum:
            return c2

    elif correctValue in secondQRange:
        if guess == minimum:
            return n
        elif guess in firstQRange:
            return w2
        elif guess in secondQRange and guess != correctValue:
            return w1
        elif guess in secondQRange and guess == correctValue:
            return correct
        elif guess in thirdQRange:
            return w2

##### Theresa's Additions #####

    elif correctValue in thirdQRange:
        if guess == minimum:
            return c1
        elif guess in firstQRange:
            return c2
        elif guess in secondQRange:
            return w2
        elif guess in thirdQRange and guess != correctValue:
            return w1
        elif guess in thirdQRange and guess == correctValue:
            return correct
        elif guess == maximum:
            return w1
    
    elif correctValue == maximum:
        if guess == minimum:
            return c1
        elif guess in firstQRange:
            return c2
        elif guess in secondQRange:
            return n
        elif guess == thirdQRange:
            return w2
        elif guess in maximum and guess != correctValue:
            return w1
        elif guess in maximum and guess == correctValue:
            return correct
