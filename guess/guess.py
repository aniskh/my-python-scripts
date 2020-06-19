#!/usr/bin/env python3
#Python game: guess a number, the script help with directives ( greater, less )


import random
import colored

def random_dice():
    #define guess intervall
    guess_max=30
    #Choose a random int
    chosen=random.randint(1,guess_max)
    colored.logcol("Starting guess game:",'ok')
    colored.logcol("the number is between 0 and " + str(guess_max),'ok')
    occurance=0
    while True:
        guess_str=input("Please enter your guess: ")
        occurance +=1
        print("You have tried " + str(occurance) + " time(s)")
        try:
            guess = int(guess_str)
            if guess > chosen:
                colored.logcol("Plese choose a number less than that !",'err')
            elif guess < chosen:
                colored.logcol("Plese choose a number greater than that !",'err')
            elif guess == chosen:
                colored.logcol("Yes! That is the number congratulation !!!",'ok')
                break
        except:
            colored.logcol("Please enter an integer between 0 and " + str(guess_max),'err')
                

def main():
    random_dice()

if __name__ == "__main__":
    main()
