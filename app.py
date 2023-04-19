print("Let's play the game of rock, paper, scissors.")

import random
comp = random.randint(1,3)
if comp == 1:
    comp = "ROCK"
elif comp == 2:
    comp = "PAPER"
else:
    comp = "SCISSORS"

while True:
    typed = input("Type 'rock' or 'paper' or 'scissors': ")
    if typed.upper() == 'ROCK':
        user = 'ROCK'
        print(f"Computer: {comp}")
        print(f"User: {user}")
        break
    elif typed.upper() == 'PAPER':
        user = 'PAPER'
        print(f"Computer: {comp}")
        print(f"User: {user}")
        break
    elif typed.upper() == 'SCISSORS':
        user = 'SCISSORS'
        print(f"Computer: {comp}")
        print(f"User: {user}")
        break
    else:
        print("Let's try this again")
