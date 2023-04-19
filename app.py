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
        print(f"User: {user}")
        print(f"Computer: {comp}")
        if comp == 'ROCK':
            print("It's a tie! Nice try")
        elif comp == "PAPER":
            print("Haha you lose! I am a superior being")
        else: 
            print("I cannot believe this... How dare you human... You win...")
        break
    elif typed.upper() == 'PAPER':
        user = 'PAPER'
        print(f"User: {user}")
        print(f"Computer: {comp}")
        if comp == 'ROCK':
            print("I cannot believe this... How dare you human... You win...")
        elif comp == "PAPER":
            print("It's a tie! Nice try")
        else: 
            print("Haha you lose! I am a superior being")
        break
    elif typed.upper() == 'SCISSORS':
        user = 'SCISSORS'
        print(f"User: {user}")
        print(f"Computer: {comp}")
        if comp == 'ROCK':
            print("Haha you lose! I am a superior being")
        elif comp == "PAPER":
            print("I cannot believe this... How dare you human... You win...")
        else: 
            print("It's a tie! Nice try")
        break
    else:
        print("Let's try this again")
