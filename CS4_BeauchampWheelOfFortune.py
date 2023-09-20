import random
def convert_phrase(phrase): # Converts the phrase into the clue, and creates a cluelist
    clue=""
    cluelist=[]
    for letter in phrase: # Converts phrase into clue
        if letter==" ":
            clue=clue+" "
        else:
            clue=clue+"_"
   
    for letter in clue: # Converts clue into a list for later use.
        cluelist.append(letter)
    return clue,cluelist


def spin_guess(score): #Spins and gets a guess
    values=[1000,300,350,500,800,700,900,300,5000,550,400,300,500,600,750,450,900,500,400,"bankrupt"]
    spin=random.choice(values) # Spins the wheel
    if spin=="bankrupt":
        score=0
        values.pop() # Removes bankrupt option
        print("You went Bankrupt!")
        print("Lets spin again")
        spin=random.choice(values)
    print("each letter will be worth $:",spin)
    guess=input("Guess a letter") # Gets a guess
    return score,spin,guess

def update_clue(clue,guess,phrase,lives,spin,score,cluelist):
    if guess in phrase: # Check if the guess is in the phrase
       
       
        for i in range(len(phrase)): # Updates clue to include guessed letters
            if guess==phrase[i]:
                cluelist[i]=guess
                score+=spin
        clue=""
        for thing in cluelist: # Converts cluelist in a string to print out
            clue=clue+thing
        print(clue)
       
       
    else: # If the guess isn't in the phrase, you lose a life.
        lives-=1
        print(guess+" is not in the puzzle, I am sorry, you lose 1 life :(")
        print(clue)
    return score,clue

def wof(): # Main game loop
   
   
    my_phrases=["i love school", "join robotics","today is friday","mac and cheese is good"]
    phrase=random.choice(my_phrases) # Chooses the phrase for the game
    score=0
    lives=5
    clue,cluelist=convert_phrase(phrase)
    print(clue)
    #score,spin,guess=spin_guess(score)
    #print(score,spin,guess)
    while lives>0 and clue!=phrase: # Runs the game until it ends
        score,spin,guess=spin_guess(score)
        score,clue=update_clue(clue,guess,phrase,lives,spin,score,cluelist)
    if lives==0: # If you lose all your lives, you lose
        print("you lose, go home")
    else: # If you guess the phrase, you win!
        print("you win!")
        print("what will you do with your $"+ str(score)+"?")
wof()