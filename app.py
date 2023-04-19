print("Let's play the game of rock, paper, scissors.")
while True:
    typed = input("Type 'rock' or 'paper' or 'scissors': ")
    if typed.upper() == 'ROCK':
        rock = typed.upper()
        #print(rock)
        break
    elif typed.upper() == 'PAPER':
        paper = typed.upper()
        #print(paper)
        break
    elif typed.upper() == 'SCISSORS':
        scissors = typed.upper()
        #print(scissors)
        break
    else:
        print("Let's try this again")


