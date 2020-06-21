#!/usr/bin/env python3
#Python script: ask a user of a number, then tell if the number is odd or even

import colored

def odd_even():
    #Ask a user for an Integer
    print("Welcome to ODD/EVEN script")
    while True:
        entry=input("Please enter a number ( to quit please enter q): ")
        if entry =='q':
            print("Exiting ...")
            break
        try:
            yournumber = int(entry)
            if ( yournumber % 2 ) == 0:
                colored.logcol("Your number is EVEN", 'ok')
            else:
                colored.logcol("Your number is ODD", 'ok')
        except:
            colored.logcol("Error, what you entered is not a  number", 'err')


def main():
    odd_even()

if __name__ == "__main__":
    main()
