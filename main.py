import random

#functions

def create_board(number):
    for row in range(3):
        for coulmn in range(3):
            print(f"| {number}", end=' ')  
            number += 1
        print("|")




def check_winner(turn):
    if turn % 2 == 0:
        print("X won")
    else:
        print("O won")



#statments

board = [] 
location_number = 0

create_board(location_number)

num_of_turns = 0


