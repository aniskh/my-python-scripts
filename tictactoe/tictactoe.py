#!/usr/bin/env python3
#Python game: tic tac toe ( two players )

import colored
import sys

def play(game,positions,player,character):
    while True:
        print(game)
        entry=input("Player"+player+" ("+character+"): Enter a number (1-9): ")
        try:
            plays = int(entry)
            if (plays >=1) and (plays <= 9):
                liste=list(game)
                position=positions[ plays - 1 ]
                if liste[position] == ' ':
                    liste[position] = character
                    game=''.join(liste)
                    break
                else:
                    colored.logcol("Error, already chosen, choose another",'err')
            else:
                colored.logcol("Error, enter a number between 1 and 9", 'err')
        except:
            colored.logcol("Error, what you entered is not a  number", 'err')
    return game

def tie(game,positions):
    check = True
    for i in range(0,9):
        if game[positions[i]] == ' ':
            check = False
    if check:
        colored.logcol("A TIE, no one wins:",'warn')
        print(game)
        sys.exit()

def win(game,positions,character):    
    if game[positions[0]] == character:
        if game[positions[1]] == character and game[positions[2]] == character:
            return True
        if game[positions[4]] == character and game[positions[8]] == character:
            return True
        if game[positions[3]] == character and game[positions[6]] == character:
            return True
    if game[positions[1]] == character and game[positions[4]] == character and game[positions[7]] == character:
        return True
    if game[positions[2]] == character:
        if game[positions[4]] == character and game[positions[6]] == character:
            return True
        if game[positions[5]] == character and game[positions[8]] == character:
            return True
    if game[positions[3]] == character and game[positions[4]] == character and game[positions[5]] == character:
        return True
    if game[positions[6]] == character and game[positions[7]] == character and game[positions[8]] == character:
        return True
    return False

def tictactoe():
    print("Welcome to TIC TAC TOE game")
    game="   |   |   \n   |   |   \n___|___|___\n   |   |   \n   |   |   \n___|___|___\n   |   |   \n   |   |   "
    positions=[13, 17, 21, 49, 53, 57, 85, 89, 93]
    while True:
        game=play(game,positions,'1','X')
        if win(game,positions,'X'):
            colored.logcol("PLAYER1 wins !!!",'ok')
            print(game)
            sys.exit()
        tie(game,positions)
        game=play(game,positions,'2','O')
        if win(game,positions,'O'):
            colored.logcol("PLAYER2 wins !!!",'ok')
            print(game)
            sys.exit()
        tie(game,positions)
        
        
def main():
    tictactoe()

if __name__ == "__main__":
    main()
