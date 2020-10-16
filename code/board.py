#!/usr/bin/env python3

class Cell:
    empty = '_'
    X = 'X'
    O = 'O'


class Game:

    def __init__(self):

        self.grid = [[Cell.empty for col in range(0,3)] for row in range(0,3)]
        self.count = 0
        self.turn = input("Who goes first X or O?: ").upper()
        self.play_game()


    def change_turn(self):

        if self.turn == 'O' or self.turn == 'o':
            self.turn = 'X'
            return 'X'
        if self.turn == 'X' or self.turn == 'x':
            self.turn = 'O'
            return 'O'


    def check_winner(self):

        if self.check_horizontals_verticals() or self.check_diagonals():
            print (f"{self.turn} you won!")
            return True


    def get_input(self):

        r = int(input(f"{self.turn} what row?: ")) - 1
        c = int(input(f"{self.turn} what column?: ")) - 1

        if self.check_placement(r,c):
            self.grid[r][c] = self.turn
            self.print_game()

        else:
            print(f"Invalid placement! Spot is already occupied. Please check the grid {self.print_game()}")
            self.get_input()


    def print_game(self):
        for row in self.grid:
            print(row)


    def check_placement(self, row, col):

        if self.grid[row][col] == '_':
            return True
        else:
            return False


    def play_game(self):
        while self.count < 9:
            self.count = self.count + 1
            self.get_input()
            if self.check_winner():
                break
            self.change_turn()
        else:
            print(f"game over!")


    def check_horizontals_verticals(self):
        for i in range(0,3):
            if self.grid[i][0] == self.grid[i][1]  == self.grid[i][2] != '_' or self.grid[0][i] == self.grid[1][i]  == self.grid[2][i] != '_':
                return True


    def check_diagonals(self):

        if self.grid[0][0] == self.grid[1][1]  == self.grid[2][2] != '_'  or self.grid[0][2] == self.grid[1][1]  == self.grid[2][0] != '_' :
            return True

if __name__ == "__main__":
   Game()