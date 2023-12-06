import random
import statistics as stats


rounds = int(input("How many times do you want to guess numbers?")) #Asks how many times a player wants to play the guessing game

for round in range(rounds):
############## Defining the valueplayers are trying to guess based on their range ##############
    lowerBound = int(input("What number do you want the lower boundary to be?")) #Asks player to define lower and upper boundaries
    upperBound = int(input("What number do you want the upper boundary to be?")) 
    correctValue = random.choice(range(lowerBound,upperBound + 1))

############## Defining Messages ####################
    w1 = "You're very warm" #warmest guess without being correct
    w2 = "You're warm" #Second warmest guess without being correct
    n = "You're not hot or cold" #If the guess is inbetween the minimum or maximum and the correct value
    c2 = "You're getting cold" #second coldest guess without being correct
    c1 = "Youre very cold" #coldest guess withoyt being correct
    correct = "Yay! You guessed the number!"
    
############## Mapping Guesses To Messages ##########
    guess = None
    while guess != correctValue:
        guess = int(input("What do you think the correct number is?"))
        differenceBetweenGuessAndCorrect = guess - correctValue

        if abs(differenceBetweenGuessAndCorrect) == 1:
            print(w1)

        elif abs(differenceBetweenGuessAndCorrect) == 2:
            print(w2)
        
        elif abs(differenceBetweenGuessAndCorrect) >= 3 and abs(differenceBetweenGuessAndCorrect) <= 5:
            print(c2)
        
        elif abs(differenceBetweenGuessAndCorrect) > 5:
            print(c1)
        
        elif differenceBetweenGuessAndCorrect == 0:
            print(correct)
            break