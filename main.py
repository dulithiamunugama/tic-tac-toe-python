import random

#functions

def create_board():
    for row in range(3):
        for coulmn in range(3):
            print(f"| {number}", end=' ')  
            number += 1
        print()


def get_player_X_inputs():
    print("This is X turn.")
    playerX = int(input("Input your move (0-8): "))


def get_player_O_inputs():
    playerO = random.randint(0,8)
    print(f"O move to {playerO}")


def check_winner(turn):
    if turn % 2 == 0:
        print("X won")
    else:
        print("O won")



#statments

board = [] 
number = 0

create_board()

num_of_turns = 0   
