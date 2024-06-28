#GAME PLAY

import os
import time
import sys
from game_board_class import Board

board = Board()  # Instance of the class *again*

def clear():
    os.system('cls')

def print_header():
    """This function prints the header."""
    print("Welcome to this Tic Tac Toe game.")

def refresh_board():
    """This function refreshes the screen, and prints the board again."""
    time.sleep(1)
    clear()
    print_header()
    board.display()
print("Hey there, welcome to my tictactoe game!")
time.sleep(2)
clear()
print("Goodluck to both players!")
time.sleep(1)
clear()


while True:
    #refresh the screen
    refresh_board()

    #taking X input
    while True:
        x_choice = input("\nX Please input from 1 - 9: ")
        if x_choice.isdigit():
            x_choice = int(x_choice)
            if 1 <= x_choice <= 9:
                break
            else:
                print("Please input a value within the given range")
        else:
            print("Invalid.")

    #updating the board based on user input.
    board.update_cells(x_choice, 'X')

    #refresh the board
    refresh_board()

    #checking for X win
    if board.checking_winner("X") == True:
        print("\n X is the winner!\n")
        ask_to_play_X = input("Do you wish to play again? (yes/no): ").lower()
        if ask_to_play_X == "yes":
            board.reset()
            continue
        else:
            exit()

    #checking for a Tie
    if board.checking_tie() == True:
        print("\n It's a Tie!\n")
        ask_to_play_tie_X = input("Do you wish to play again? (yes/no): ").lower()
        if ask_to_play_tie_X == "yes":
            board.reset()
            continue
        else:
            exit()

    #taking O input
    while True:
        x_choice = input("\nO Please input from 1 - 9: ")
        if x_choice.isdigit():
            x_choice = int(x_choice)
            if 1 <= x_choice <= 9:
                break
            else:
                print("Please input a value within the given range")
        else:
            print("Invalid.")
    board.update_cells(x_choice, 'O')

    #refresh the board
    refresh_board()

    #checking for O win
    if board.checking_winner("O") == True:
        print("\n O is the winner! \n")
        ask_to_play_O = input("Do you wish to play again? (yes/no): ").lower()
        if ask_to_play_O == "yes":
            board.reset()
            continue
        else:
            exit()

    #checking for Tie 0