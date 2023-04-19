print("Let's play the game of rock, paper, scissors.")

import random
comp = random.randint(1,3)
if comp == 1:
    comp = "ROCK"
elif comp == 2:
    comp = "PAPER"
else:
    comp = "SCISSORS"

userWin = "I cannot believe this... How dare you human... You win..."
userLose = "Haha you lose! I am a superior being."
tie = "It's a tie! That wasn't too bad."

while True:
    typed = input("Type 'rock' or 'paper' or 'scissors': ")
    if typed.upper() == 'ROCK':
        user = 'ROCK'
        print(f"User: {user}")
        print(f"Computer: {comp}")
        if comp == 'ROCK':
            print(tie)
        elif comp == "PAPER":
            print(userLose)
        else: 
            print(userWin)
        break
    elif typed.upper() == 'PAPER':
        user = 'PAPER'
        print(f"User: {user}")
        print(f"Computer: {comp}")
        if comp == 'ROCK':
            print(userWin)
        elif comp == "PAPER":
            print(tie)
        else: 
            print(userLose)
        break
    elif typed.upper() == 'SCISSORS':
        user = 'SCISSORS'
        print(f"User: {user}")
        print(f"Computer: {comp}")
        if comp == 'ROCK':
            print(userLose)
        elif comp == "PAPER":
            print(userWin)
        else: 
            print(tie)
        break
    else:
        print("Let's try this again")
