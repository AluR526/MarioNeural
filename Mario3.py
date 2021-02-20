import os
import pyautogui
import time
from random import seed
from random import randint
import sys

seed(4)

initialCaptureScore = True

myRounds = []
myRoundScores = []
myBestRounds = []
myBestRoundScores = []
iterationCounter = 1
iterationCounterProgressed = 1

def buttonPress(nameOfKey):
    # HAVE TO ADD TIME BETWEEN KEY DOWN AND UP OR ELSE IT WONT RECOGNIZE COMMAND. Shortcut for button press
    pyautogui.keyDown(nameOfKey)
    time.sleep(.2)
    pyautogui.keyUp(nameOfKey)

def saveProgress():
    global myBestRounds
    global myBestRoundScores

    #Save Progress. This saves to myRoundScores how far mario got.
    file = open("C:\\Users\\SFU\\Desktop\\MathThesis\\Score.txt", "r")
    myTextFileContent = file.readlines()
    myTextFileContent[0] = myTextFileContent[0].replace('\n', '')
    myScore = (int(myTextFileContent[0],16)*256) + int(myTextFileContent[1],16)

    #Death Check
    if myScore == 16384 or myTextFileContent[2] == "38":
        myRoundScores.append(0)
    else:
        myRoundScores.append(myScore)

    #Win Check
    if myTextFileContent[0] == "20":
        print("WOW WE WON")
        myBestRounds.append(myRounds[len(myRounds)-1])
        myBestRoundScores.append("-999")
        sys.exit()

def iterationTransition():
    #Two things happening here. The scores of the however many trials - one must be above zero and it must be greator than the previous round (zero if its the very first round). Working with Bests
    global myRounds
    global myRoundScores
    global myBestRounds
    global myBestRoundScores
    global iterationCounter
    global iterationCounterProgressed

    counter = 0
    max = 0
    maxPos = -1
    for b in myRoundScores:
        if b > max:
            max = b
            maxPos = counter
        counter = counter + 1
    if maxPos != -1:
        if iterationCounterProgressed == 1:
            myBestRoundScores.append(max)
            myBestRounds.append(myRounds[maxPos])
            iterationCounterProgressed = iterationCounterProgressed + 1
        else:
            #The end is 0A*75. If the score is closer to the end continue
            if (abs(  ( int("75",16)    +    (int("0A",16)*256) )   -max)) < (abs(  ( int("75",16)   +   (int("0A",16)*256) )   -myBestRoundScores[iterationCounterProgressed - 2])):
                myBestRoundScores.append(max)
                myBestRounds.append(myRounds[maxPos])
                iterationCounterProgressed = iterationCounterProgressed + 1
    #Fail safe 1. If we are dead go back an iteration
    else:
        if iterationCounterProgressed > 1:
            iterationCounterProgressed = iterationCounterProgressed - 1
            myBestRounds.pop()
            myBestRoundScores.pop()


    # Increase Iteration
    iterationCounter = iterationCounter + 1

def launch():
    #Open emulator
    os.system("start C:\\Users\\SFU\\Desktop\\MathThesis\\fceux-2.2.3-win32\\fceux.exe")
    time.sleep(2)

    #Load Game
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("fn")
    buttonPress("f1")
    pyautogui.keyUp("fn")
    pyautogui.keyUp("ctrl")
    time.sleep(2)

def captureScore():
    global initialCaptureScore

    #Open Hex Editor
    buttonPress("o")
    time.sleep(.2)

    #Search Hex Editor
    pyautogui.keyDown("ctrl")
    buttonPress("a")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Enter First Value (X Multiplier)
    pyautogui.typewrite("0075")
    buttonPress("enter")
    time.sleep(.2)

    #Copy Value
    pyautogui.keyDown("ctrl")
    buttonPress("c")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Open Terminal
    buttonPress("win")
    pyautogui.typewrite("cmd")
    buttonPress("enter")
    time.sleep(.2)

    #Change Directory
    pyautogui.typewrite("cd C:\\Users\\SFU\\Desktop\\MathThesis")
    buttonPress("enter")
    time.sleep(.2)

    #Create txt file
    pyautogui.typewrite("Notepad Score.txt")
    buttonPress("enter")
    time.sleep(.2)

    #Create file authentication and write to file
    buttonPress("enter")
    pyautogui.keyDown("ctrl")
    buttonPress("v")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Back to Hex Editor
    pyautogui.keyDown("alt")
    buttonPress("tab")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    #Search Hex Editor 2
    pyautogui.keyDown("ctrl")
    buttonPress("a")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Enter First Value (X Value) 2
    pyautogui.typewrite("0090")
    buttonPress("enter")
    time.sleep(.2)

    #Copy Value 2
    pyautogui.keyDown("ctrl")
    buttonPress("c")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Back to Notepad
    pyautogui.keyDown("alt")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    #write to file 2
    buttonPress("enter")
    pyautogui.keyDown("ctrl")
    buttonPress("v")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Back to Hex Editor 3
    pyautogui.keyDown("alt")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    # Search Hex Editor 3
    pyautogui.keyDown("ctrl")
    buttonPress("a")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    # Enter First Value (X Value) 3
    pyautogui.typewrite("000CDE")
    buttonPress("enter")
    time.sleep(.2)

    # Copy Value 3
    pyautogui.keyDown("ctrl")
    buttonPress("c")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    # Back to Notepad 3
    pyautogui.keyDown("alt")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    # write to file 3
    buttonPress("enter")
    pyautogui.keyDown("ctrl")
    buttonPress("v")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)


    #Save file
    pyautogui.keyDown("ctrl")
    buttonPress("s")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Exit terminal
    pyautogui.keyDown("alt")
    buttonPress("tab")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    pyautogui.typewrite("exit")
    buttonPress("enter")
    time.sleep(.2)

    #Save Progress
    saveProgress()

    #Return to game
    pyautogui.keyDown("alt")
    buttonPress("tab")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    initialCaptureScore = False

def captureScore2():
    #Open Hex Editor
    buttonPress("o")
    time.sleep(.2)

    #Search Hex Editor
    pyautogui.keyDown("ctrl")
    buttonPress("a")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Enter First Value (X Multiplier)
    pyautogui.typewrite("0075")
    buttonPress("enter")
    time.sleep(.2)

    #Copy Value
    pyautogui.keyDown("ctrl")
    buttonPress("c")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Get to txt document
    pyautogui.keyDown("alt")
    buttonPress("tab")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    #Delete txt document
    pyautogui.keyDown("ctrl")
    buttonPress("a")
    pyautogui.keyUp("ctrl")
    buttonPress("backspace")
    time.sleep(.2)

    #Write to File
    pyautogui.keyDown("ctrl")
    buttonPress("v")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Back to hex editor
    pyautogui.keyDown("alt")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    #Search Hex Editor 2
    pyautogui.keyDown("ctrl")
    buttonPress("a")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Enter First Value (X Value) 2
    pyautogui.typewrite("0090")
    buttonPress("enter")
    time.sleep(.2)

    #Copy Value 2
    pyautogui.keyDown("ctrl")
    buttonPress("c")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Back to Notepad
    pyautogui.keyDown("alt")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    #write to file 2
    buttonPress("enter")
    pyautogui.keyDown("ctrl")
    buttonPress("v")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    # Back to Hex Editor 3
    pyautogui.keyDown("alt")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    # Search Hex Editor 3
    pyautogui.keyDown("ctrl")
    buttonPress("a")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    # Enter First Value (X Value) 3
    pyautogui.typewrite("000CDE")
    buttonPress("enter")
    time.sleep(.2)

    # Copy Value 3
    pyautogui.keyDown("ctrl")
    buttonPress("c")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    # Back to Notepad 3
    pyautogui.keyDown("alt")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

    # write to file 3
    buttonPress("enter")
    pyautogui.keyDown("ctrl")
    buttonPress("v")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Save file
    pyautogui.keyDown("ctrl")
    buttonPress("s")
    pyautogui.keyUp("ctrl")
    time.sleep(.2)

    #Save Progress
    saveProgress()

    #Return to game
    pyautogui.keyDown("alt")
    buttonPress("tab")
    buttonPress("tab")
    pyautogui.keyUp("alt")
    time.sleep(.2)

def reinforcementBruteFixedTime():
    #myButtonList=["left","right","b","a"]
    global iterationCounter
    global myRounds
    global myBestRounds

    amountPerRound = 5

    #No button is being pressed right now (False = not pressed; True = pressed)
    leftDown = False
    rightDown = False
    bDown = False
    aDown = False

    #Generate random numbers corresponding to button presses. BLANK AMOUNT PER EACH ROUND
    myRandomNumbers = []
    # Append best previous iteration
    for a in myBestRounds:
        for b in a:
            myRandomNumbers.append(b)
    for i in range(amountPerRound):
        myRandomNumbers.append(randint(0,3))
    print("THIS IS WHAT IM ACTUALLY INPUTING: ", myRandomNumbers)

    # Load SaveState
    buttonPress("p")
    time.sleep(1)

    #Unpause
    buttonPress("enter")

    #Perform the button presses (If button is already down and it is called again - release button
    for j in myRandomNumbers:
        if j == 0:
            if leftDown == False:
                pyautogui.keyDown("a")
            else:
                pyautogui.keyUp("a")
            leftDown = not leftDown
        elif j == 1:
            if rightDown == False:
                pyautogui.keyDown("s")
            else:
                pyautogui.keyUp("s")
            rightDown = not rightDown
        elif j == 2:
            if bDown == False:
                pyautogui.keyDown("d")
            else:
                pyautogui.keyUp("d")
            bDown = not bDown
        else:
            if aDown == False:
                pyautogui.keyDown("f")
            else:
                pyautogui.keyUp("f")
            aDown = not aDown
        #Program will press a new button every BLANK SECONDS
        time.sleep(.5)

    #Turn off all buttons
    pyautogui.keyUp("left")
    pyautogui.keyUp("right")
    pyautogui.keyUp("d")
    pyautogui.keyUp("f")

    #Pause
    buttonPress("enter")

    #Record Button sequence
    myRounds.append(myRandomNumbers[amountPerRound*(iterationCounterProgressed-1)::])

    time.sleep(1)

def run(roundsPerIter):
    global myRounds
    global myRoundScores
    global myBestRounds
    global myBestRoundScores
    global iterationCounter
    global iterationCounterProgressed

    launch()
    while True:
        print("IterationCounter: ", iterationCounter)
        print("IterationCounterProgressed: ", iterationCounterProgressed)
        print()
        for b in range(roundsPerIter):
            reinforcementBruteFixedTime()
            if initialCaptureScore == True:
                captureScore()
            else:
                captureScore2()
            print("MyRounds: ", myRounds)
            print("MyRoundScores ", myRoundScores)
            print("MyBestRounds ", myBestRounds)
            print("MyBestRoundScores ", myBestRoundScores)
            print()
        iterationTransition()
        myRounds = []
        myRoundScores = []
        print("NEXT ROUND XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

run(10)