#!/usr/bin/env python3
#Python script dice-like ( generate a random integer)


import string
import random

def random_dice():
    #choose the number of dice faces
    dice_length=6
    print("The dice contains 6 faces.")
    number=input("If you want to change this number, please tape a number, else press ENTER: ")
    if number != '':
        try:
            dice_length=int(number)
        except:
            print(" error encountered, using 6 as dice faces number")
    #Dicing
    print("dicing ...")
    randdice=random.randint(1,dice_length)
    print (randdice)
    while True:
        decision=input("dice again? (y/n)")
        if decision == 'y':
            print("dicing ...")
            randdice=random.randint(1,dice_length)
            print (randdice)
        elif decision == 'n':
            print("Exiting.")
            break
                

def main():
    random_dice()

if __name__ == "__main__":
    main()
