print("Let's play the game of rock, paper, scissors.")
while True:
    typed = input("Type 'rock' or 'paper' or 'scissors': ")
    if typed.upper() == 'ROCK' or typed.upper() == 'PAPER' or typed.upper() == 'SCISSORS':
        #print('well done')
        #import random

        break
    else:
        print("Let's try this again.")

