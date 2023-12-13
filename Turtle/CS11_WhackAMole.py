# Import stuff to use later
import turtle
import random
import os

screen = turtle.Screen() # Make a screen object
timerTurtle = turtle.Turtle() # Make a turtle to display the time left
scoringTurtle = turtle.Turtle() # Make a turtle to display the score
turtles = [] # Make an empty list of turtles.

def setup(numberOfTurtles, time):
    global playerScore # Declare playerScore and timeLeft as global variables
    global timeLeft
    os.system('cls') # Clear the terminal
    playerScore = 0 # default score to 0 and time left to 10
    timeLeft = time
    screen.bgcolor("red") # Set background color to red
    timerTurtle.penup() # Setting up my utility turtles
    timerTurtle.hideturtle()
    timerTurtle.speed(0)
    timerTurtle.goto(-250, 250)
    scoringTurtle.penup()
    scoringTurtle.hideturtle()
    scoringTurtle.speed(0)
    scoringTurtle.goto(-250, 200)
    scoringTurtle.write("Score: " + str(playerScore), font = ("Arial", 20, "normal")) # Display the current score
    turtles.clear() # Clears the list of turtles
    for i in range(numberOfTurtles):
        turtles.append(turtle.Turtle()) # Creates some number of turtles
    for t in turtles: # Setup mole turtles
        t2: turtle = t
        t2.speed(0)
        t2.penup()
        turtle.register_shape("Turtle/Pictures/CS11_Mole.gif")
        t2.shape("Turtle/Pictures/CS11_Mole.gif")
    randomizeTurtleLocations() # Move the turtles to random locations

def randomizeTurtleLocations(): # Randomizes turtle locations
    # List of allowed turtle locations
    theseLocations = [(-200, 150), (0, 150), (200, 150), (-200, 0), (0,0), (200, 0), (-200, -150), (0, -150), (200, -150)]
    for t in turtles: # Sends the turtle to a random, unique location
        t2: turtle = t
        thisLocation = random.choice(theseLocations)
        theseLocations.remove(thisLocation)
        t2.goto(thisLocation)
        t2.showturtle()

def clock(): # Main game loop to increment clock and check if the game is over
    global timeLeft # Specify that timeleft is a gloabl variable, not a local one
    timeLeft -= 1 # As time passes, time goes down
    if (timeLeft < 0): # If time is less than 0, end the game
        setDown()
    else: # Otherwise update the displayed time, randomize turtle locations, and recall the function after a second
        timerTurtle.clear()
        timerTurtle.write("Time left: " + str(timeLeft), font = ("Arial", 20, "normal"))
        randomizeTurtleLocations()
        screen.ontimer(clock, 1000)

def clicked(x,y): # Defines what to do if a click is registered
    global playerScore
    xClickThreshold = 10 # Threshold for how close a click should be to a turtle to count
    yClickThreshold = 10
    for t in turtles: # For each turtle, if it was clicked, add to score and send the turtle away
        t2: turtle = t
        if abs(t2.xcor() - x) < xClickThreshold and abs(t2.ycor() - y) < yClickThreshold:
            t2.hideturtle()
            t2.goto(1000,1000)
            playerScore += 1
            scoringTurtle.clear()
            scoringTurtle.write("Score: " + str(playerScore), font = ("Arial", 20, "normal"))

def setDown(): # Prints a message telling the player their score
    print("Your score was: " + str(playerScore))
    screen.bye() # Closes the turtle window

def readScores(fileName: str = "Turtle/Text/CS11_Highscores.txt"): # Function to read scores from the files storing scores
    fileReader = open(fileName, "r") # Open the file to read
    nameScoreList = [] # Create an empty list of name score pairs
    for line in fileReader:
        nameScoreList.append((line.split(": "))) # Append each line of the highscore file to the name score list as a list of 2
    fileReader.close() # Close the file, we don't need it anymore
    for pairing in nameScoreList: # Change score to an int instead of a str
        pairing[1] = int(pairing[1])
    return nameScoreList # Give back the completed list

def sortScores(nameScoreList: list): # Just sorts name score list based on score
    nameScoreList.sort(key = lambda x: x[1], reverse = True)
    return nameScoreList

def updateScores(playerScore: int, oldNameScoreList: list): # Function to update scores with the player's score
    playerName = input("What's your name? ") # Ask the player for their name
    nameScoreList = sortScores(oldNameScoreList) # Make sure the name score list is sorted.
    playerPair = [playerName, playerScore] # Create a two element list containing player name and score
    nameScoreList.append(playerPair) # Add player to list
    for pair in nameScoreList:
        if playerPair[0] == pair[0] and not playerPair == pair: # Check if the player is already on the highscore list
            if playerPair[1] > pair[1]: # Remove the one with a lower score
                nameScoreList.remove(pair)
            else:
                nameScoreList.remove(playerPair)
            break
    nameScoreList = sortScores(nameScoreList) # Resort list
    while len(nameScoreList) > 5: # Make sure there are only 5 values
        nameScoreList.pop()
    return nameScoreList # Hand back the updated list

def writeScores(nameScoreList: list, fileName: str = "Turtle/Text/CS11_Highscores.txt"): # Function to write the new highscores to the file
    fileWriter = open(fileName, "w") # Open the file to write
    for pair in nameScoreList: # Write each pair
        fileWriter.write(pair[0] + ": " + str(pair[1]) + "\n")
    fileWriter.close() # Close the fil

setup(4, 10) # Call setup with our desired number of turtles and time to play
clock() # Start the clock
screen.onclick(clicked) # If the screen is clicked, call the clicked function
screen.mainloop() # Keep the turtle window open while the game is running
writeScores(updateScores(playerScore, readScores())) # After the window closes, do the thing to write the scores
