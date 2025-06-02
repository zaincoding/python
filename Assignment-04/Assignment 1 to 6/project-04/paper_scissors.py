import random

def player():
        user = input("'r' for rock, 'p' for paper, 's' for scissor: ")
        computer = random.choice(['r', 'p', 's'])

        print(computer)


        if user == computer:
                return 'tie'
        
        if is_win(user,computer):
               
               return 'You Win'
        return 'You Lose.'
        

def is_win(player,opponent):

    if (player == 'r' and opponent == 's') or  (player == 's' and opponent == 'p') \
         or (player == 'p' and opponent == 'r'):
        return True

print(player())