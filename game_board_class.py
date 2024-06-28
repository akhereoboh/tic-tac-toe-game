#GAME CLASS IE BOARD

import os
import time
import sys

def clear():
    os.system('cls')

class Board():

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        """This method displays the board"""
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))
        print("___________ ")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("___________ ")
        print(" %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9]))

    def update_cells(self, cell_number, player):
        """This method updates the cells if a user inputs a value"""
        if self.cells[cell_number] == " ":
            self.cells[cell_number] = player
        else:
            print("Oops, space already taken.")
            time.sleep(1)

    def checking_winner(self, player):
        """This method checks for a winner in the game"""
        #checking horizontal firstrole
        if self.cells[1] == self.cells[2] == self.cells[3] and self.cells[1] == player:
            return True
        #checking horizontal second role
        elif self.cells[4] == self.cells[5] == self.cells[6] and self.cells[4] == player:
            return True
        #checking horizontal third role
        elif self.cells[7] == self.cells[8] == self.cells[9] and self.cells[7] == player:
            return True

        # checking vertical first column
        elif self.cells[1] == self.cells[4] == self.cells[7] and self.cells[1] == player:
            return True
        # checking vertical second column
        elif self.cells[2] == self.cells[5] == self.cells[8] and self.cells[2] == player:
            return True
        # checking vertical third column
        elif self.cells[3] == self.cells[6] == self.cells[9] and self.cells[3] == player:
            return True

        # checking diagonal left column
        elif self.cells[1] == self.cells[5] == self.cells[9] and self.cells[1] == player:
            return True
        # checking diagonal right column
        elif self.cells[3] == self.cells[5] == self.cells[7] and self.cells[3] == player:
            return True

        return False

    def checking_tie(self):
        """This method checks for a tie in the game"""
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1

        if used_cells == 9:
            return True

        else:
            return False



    def reset(self):
        """This method resets the board to default"""
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]



board = Board()  # Instance of the class