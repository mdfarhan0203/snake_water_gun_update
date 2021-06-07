import random

def gameWinner(player,computer):
    if player==computer:
        print("Tie")
    elif player=="s":
        if computer=="w":
            print("player1 win")
        elif computer=="g":
            print("player2 win")

    elif player=="w":
        if computer=="s":
            print("you loose")
        elif computer=="g":
            print("you win")
    elif player=="g":
        if computer=="s":
            print("you loose")
        elif computer=="w":
            print("computer win")
    else:
        print("please select any one option from above")
        

player=input("Player 1 Enter a character  For snake (s) and for water (w) and for Gun (g) ??\n")
computer=random.randint(1,3)
if computer==1:
    computer="s"
elif computer==2:
    computer="w"
elif computer==3:
    computer="g"
print(gameWinner(player,computer))

print(f"player one is enter :{player}")
print(f"player second  is enter :{computer}")