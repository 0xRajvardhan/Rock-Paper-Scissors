import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True


print("Computer's Turn: Rock(r) Paper(p) or Scissors(s) ?\n")

randNo = random.randint(1, 3)

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = "s"

you = input("Your Turn: Rock(r) Paper(p) or Scissors(s) ?\n")

a = gameWin(comp, you)

print(f"Computer chose: {comp}")
print(f"You chose: {you}")

if a == None:
    print("The game is tie!")
elif a:
    print("You win!")
else:
    print("You lose :(")


'''
Game name => Rock Paper Scissors
Code Author => Rajvardhan Singh

'''
