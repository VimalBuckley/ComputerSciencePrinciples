import random
import time
import os

class enemy:
    def __init__(self, name, inputMinAtk,inputMaxAtk):
        self.name = name
        self.minAtk = inputMinAtk
        self.maxAtk = inputMaxAtk

atkMin = 1
atkMax = 6

rabbitFightCount  = 0

deathByHidingInCave = [" You stay in the cave. \n\n\n\n\n\n", " You are still in the cave. \n\n\n\n\n\n", " Why are you here again? \n\n\n\n\n\n", "Are you ever going to leave? \n\n\n\n\n\n\n"]
deathByRabbit = [" You were obliterated by a rabbit...\n ... somehow."]
deathByHidingFromAuthorities1 = [" You decided to hide from the authorities.", " First, you went into the woods and built a house.", " You lived there for 71 years, without seeing anyone else.", " Then, without warning, a team of 7 authorities appeared in your house while you were eating lunch and apprehended you."]
deathByHidingFromAuthorities2 = [" You decided to hide from the authorities.", " First, you went into the woods and built a house.", " You lived there for 71 years, without seeing anyone else.", " Then, the ground starts moving.", " The Lion appears behind you and obliterates you, your house, and the entire earth."]
deathByLion = [" You were obliterated by The Lion in one attack.", " In just three days, the rest of the world have been destroyed by The Lion's claws."]
deathByWaitingTooLong = [" You killed the rabbit..."," ...but you hear fighting oustide the cave!"," You realize the lion took over the world while you were fighting rabbits!"," You are the only one left!"," You turn and see the lion"," You have fought 7 rabbits. You can fight the lion...right?"," ...right?"," right?"]
rabbit = enemy("rabbit", 0,3)
lion = enemy("lion", 3, 8)

def wait(seconds):
    time.sleep(seconds)

def choose(option1, option2):
    wait(0.75)
    choice = input("Choose '" + option1 + "' or '" + option2 + "' " )
    wait(0.75)
    while choice != option1 and choice != option2:
        print("That isn't a valid choice. Please choose again")
        wait(0.75)
        choice = input("Choose '" + option1 + "' or '" + option2 + "' " )
        wait(0.75)
    return choice == option1

def win():
    if rabbitFightCount > 5:
        message = ["You won, but now what?","You are the only person left.","You decide to go in the forest and build a house.","You live there for 71 years.","'~'"]
    else:
        message = [" The lion appraoches.", " You are scared", " The lion attacks", " You step to the side", " The lion falls to the ground", " You attack.", " The lion can't dodge it.", "You won", ":D"]
    for line in message:
        print(line)
        wait(0.75)

def lose(reason):
    print("\n")
    for line in reason:
        print(line)
        wait(0.75)
    print("You lose!")
    wait(0.75)
    print(":(")

def rollTwoDice(min, max):
    return random.randint(min, max) + random.randint(min,max)

def increaseStats():
    global atkMax
    print("\nYour max attack increased by 2!")
    wait(0.75)
    atkMax += 1
    print("It's now", atkMax * 2)
    wait(0.75)
    print("Do you want to keep fighting rabits, or do you want to try and fight the lion?")
    if choose("rabbit", "lion"):
        combat(rabbit)
    else:
        combat(lion)

def combat(enemy):
    yourAttack = rollTwoDice(atkMin, atkMax)
    enemyAttack = rollTwoDice(enemy.minAtk, enemy.maxAtk)
    print("\nYou entered a battle!!")
    wait(0.75)
    print("You're fighting a " + enemy.name + "!")
    wait(0.75)
    print("You rolled a " + str(yourAttack) + "!")
    wait(0.75)
    print("The", enemy.name, "rolled a " + str(enemyAttack) + "!")
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
            global rabbitFightCount
            rabbitFightCount += 1
            if rabbitFightCount > 7:
                lose(deathByWaitingTooLong)
            else:
                increaseStats()

def cave():
    print("\nYou enter the cave...")
    wait(0.75)
    print("Suddenly you hear a noise. When you look over, you see a rabbit, glaring at you")
    wait(0.75)
    print("Will you fight the rabbit, or hide in the cave?")
    if choose("fight", "hide"):
        combat(rabbit)
    else:
        lose(deathByHidingInCave)

def field():
    print("\nWhen you open your eyes, you find yourself stand in an empty field...")
    wait(0.75)
    print("But then you hear a loud roar. Turning around, you come face to face with a lion!")
    wait(0.75)
    print("You also spot a small opening to a cave that the lion couldn't fit in")
    wait(0.75)
    print("Will you try to fight the lion, or run into the cave?")
    if choose("fight", "run"):
        combat(lion)
    else:
        cave()

def takeTrain():
    print("\nYou board the train...")
    wait(0.75)
    print("Conductor: Welcome aboard all you brave heroes who are going to fight the mighty lion!")
    wait(0.75)
    print("Will you stay on the train, or get off and try to hide from the government?")
    if choose("fight", "hide"):
        field()
    else:
        lose(random.choice(deathByHidingFromAuthorities1, deathByHidingFromAuthorities2))
    
def talkToMan():
    print("\nYou go over to talk to the man")
    wait(0.75)
    print("He says: All people over the age of -1 are being recruited to fight the mighty lion terroizing the earth")  
    wait(0.75)
    print("Will you go to help stop the lion, or live a life on the run from the authorities?")
    if choose("fight", "hide"):
        takeTrain()
    else: 
        lose(random.choice([deathByHidingFromAuthorities1, deathByHidingFromAuthorities2]))

def city():
    print("\nWelcome to the city!")
    wait(0.75)
    print("You see a old man waving his hand at you, but then behind you, you hear:")
    wait(0.75)
    print("Last call for the train!!")
    wait(0.75)
    print("Will you go talk to the old man or board the train?")
    if choose("talk", "train"):
        talkToMan()
    else:
        takeTrain()

def start():
    os.system('cls') # Clears the console
    print("Welcome player!")
    wait(0.75)
    print("Do you want to start in the fields or the city?")
    if choose("field", "city"):
        field()
    else:
        city()

start()
