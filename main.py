class Game:

    def __init__(self):
        self.matrix = [["   " for j in range(3)] for i in range(3)]
        self.names = ["Player 1", "Player 2"]
        self.is_game_on = False

    def print_board(self):
        print('\n\n')
        for i in range(3):
            print(" | ".join(self.matrix[i]))
            if i < 2:
                print("---------------")

    def start_game(self):
        print("WELCOME TO TIC-TAC-TOE!")
        input("\nTo start the game press enter...\n")

        n = input(f"Enter the name on player 1 ({self.names[0]}?): ")
        if len(n) > 0:
            self.names[0] = n
        print(f"{self.names[0]} V/S ...")
        print(f"Enter the name on player 2 ({self.names[1]}?) ", end='')
        n = input()
        if len(n) > 0:
            self.names[1] = n

        self.run_game()
        self.reset()

    def run_game(self):
        print(f"\n\n{self.names[0]} V/S {self.names[1]} ")
        print('Press enter to start')
        input()

        self.print_board()
        self.is_game_on = True
        p = 0

        for i in range(9):
            # if p:
            print(f"{self.names[p]}'s turn....")
            self.take_input(p)

            self.print_board()
            if self.check_winner(p):
                print(f"\n\n{self.names[p]} wins!")
                print("Game Over!")
                self.is_game_on = False
                break

            p = 1 - p

    def take_input(self, p):

        symbols = [" X ", " O "]

        def mn_input():
            m, n = -1, -1
            m = (input("enter row: "))
            while m not in ["1", "2", "3"]:
                print("enter valid row number")
                m = (input("enter row: "))
            n = (input("enter column: "))
            while n not in ["1", '2', '3']:
                print("enter valid column number")
                n = (input("enter column: "))
            return int(m), int(n)

        m, n = mn_input()
        while self.matrix[m - 1][n - 1] in symbols:
            print("you cannot over write on a box. Enter a different box")
            m, n = mn_input()

        self.matrix[m-1][n-1] = symbols[p]



    def check_winner(self, p):
        symbol = [" X ", " O "][p]
        for i in range(3):
            row = self.matrix[i]
            if all(elem == symbol for elem in row):
                return True
        for i in range(3):
            col = [self.matrix[0][i], self.matrix[1][i], self.matrix[2][i]]
            if all(elem == symbol for elem in col):
                return True

        diag1 = [self.matrix[i][i] for i in range(3)]
        diag2 = [self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]]
        if all(elem == symbol for elem in diag1) or all(elem == symbol for elem in diag2):
            return True

        return False

    def reset(self):
        y = input('Do you want to play again?? y/n: ')
        if y == "y":
            self.matrix = [["   " for j in range(3)] for i in range(3)]
            self.start_game()
        else:
            return



Game().start_game()
