print("Let's play the game of rock, paper, scissors.")
while True:
    typed = input("Type 'rock' or 'paper' or 'scissors': ")
    if typed.upper() == 'ROCK':
        rock = typed.upper()
        print(f"User: {rock}")
        break
    elif typed.upper() == 'PAPER':
        paper = typed.upper()
        print(f"User: {paper}")
        break
    elif typed.upper() == 'SCISSORS':
        scissors = typed.upper()
        print(f"User: {scissors}")
        break
    else:
        print("Let's try this again")

import random
comp = random.randint(1,3)
if comp == 1:
    comp = "ROCK"
    print(f"Computer: {comp}")
elif comp == 2:
    comp = "PAPER"
    print(f"Computer: {comp}")
else:
    comp = "SCISSORS"
    print(f"Computer: {comp}")
