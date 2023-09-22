import random
import time

class enemy:
    def __init__(self, name, inputMinAtk,inputMaxAtk):
        self.name = name
        self.minAtk = inputMinAtk
        self.maxAtk = inputMaxAtk
atkMin = 1
atkMax = 6

deathByRabbit  = "rabbit"
deathByLion = "lion"
deathByHidingFromAuthorities1 = ""
deathByHidingInCave = ""
rabbit = enemy("rabbit", 0,3)
lion = enemy("lion", 3, 8)

def wait(seconds):
    time.sleep(seconds)

def win():
    print("You won")

def lose(reason):
    print(reason)
    wait(0.75)
    print("You lose!")
    wait(0.75)
    print(":(")

def rollTwoDice(min, max):
    return random.randint(min, max) + random.randint(min,max)

def combat(enemy):
    yourAttack = rollTwoDice(atkMin, atkMax)
    enemyAttack = rollTwoDice(enemy.minAtk, enemy.maxAtk)
    print("You entered a battle!!")
    wait(0.75)
    print("You're fighting a " + enemy.name)
    wait(0.75)
    print("You rolled a " + str(yourAttack) + "!")
    wait(0.75)
    print("Your opponent rolled a " + str(enemyAttack))
    wait(0.75)
    if (enemyAttack > yourAttack):
        print("You lost the fight!")
        wait(0.75)
        if enemy.name == "lion":
            lose(deathByLion)
        else: 
            lose(deathByRabbit)  
    else:
        print("You won the fight!")
        wait(0.75)
        if enemy.name == "lion":
            win()
        else:
            increaseStats()

def increaseStats():
    global atkMax
    print("Your max attack increased by 1!")
    wait(0.75)
    atkMax += 1
    print("It's now", atkMax)
    wait(0.75)
    choice = input("Do you want to keep fighting rabbits? Or do you want to try and fight the lion? \nChoose 'rabbit' or 'lion' ")
    if choice == "rabbit":
        combat(rabbit)
    else:
        combat(lion)

def field():
    print("field")

def talkToMan():
    print("You go over to talk to the man")
    wait(0.75)
    print("He says: All people over the age of -1 are being recruited to fight the mighty lion terroizing the earth")  
    wait(0.75)
    print("Will you go to help stop the lion, or live a life on the run from the authorities")
    wait(0.75)
    choice = input("Choose 'fight' or 'hide'")
    if choice == "fight":
        takeTrain()
    else: 
        lose(deathByHidingFromAuthorities1)
def city():
    print("city")


def start():
    print("Welcome player!")
    wait(0.75)
    print("Do you want to start in the fields or the city")
    wait(0.75)
    choice = input("Choose 'field' or 'city'")
    wait(0.75)
    if choice == "field":
        field()
    else:
        city()


