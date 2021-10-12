import os
import random
import json


wordBank = []
wrongAnswers = []
correctGuesses = []

global currentPlayer 
global currentPlayerID 
currentPlayer = None
currentPlayerID = None
## I Need to set all to global or all to local
def loadWords():
    f = open("wordBank.txt", "r")
    for x in f:
        wordBank.append(str(x.strip()))
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
def loadPlayerData():
    id = 0
    with open('players.json') as f:
         players = json.load(f)
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")     
    print("|                                            |")
    if currentPlayer == None:
        print("|    Current Player:                         |")
    else:
        print("|    Current Player: ", currentPlayer["playerFirstName"], currentPlayer["playerLastName"], currentPlayer["playerHighScore"], "|")
    print("|                                            |")
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    print("|  ID |  First Name | Last Name  | HighScore |")
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    for x in players["players"]:
        print("| ", id, " | ", x["playerFirstName"], " | ", x["playerLastName"], " | ", x["playerHighScore"] ," |" )
        id = id + 1
    ##print(json.dumps(players))
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    print("|  enter ID Number for selecting a player    |")
    print("|        [n] for New player                  |")
    print("|        [d] remove a player                 |")
    print("|        [q] to go back                      |")
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
def newPlayer():
    print("Enter first name")
    playerFirstName = input()
    print("Enter last name")
    playerLastName = input()
    x = {
    "playerFirstName": playerFirstName,
    "playerLastName": playerLastName,
    "playerHighScore": 0
    }
    filename='players.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["players"].append(x)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    clr()
    displayPlayerlog()
def displayPlayerlog(): 
    id = 0
    loadPlayerData() 
    selectPlayer = input()
    if selectPlayer == "n":
        newPlayer()
    elif selectPlayer == "d":
        ##deletePlayer()
        deletePlayer()
    elif selectPlayer == "q":
        clr()
        startup()
    else:
        
        selectPlayer = int(selectPlayer)
        filename='players.json'
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            for x in file_data["players"]:
                if id == selectPlayer:
                    global currentPlayer
                    currentPlayer = x
                    print(currentPlayer["playerFirstName"])
                    global currentPlayerID
                    currentPlayerID = id 
                id = id + 1     
    clr()
    displayPlayerlog()
def stats():
    clr()
    id = 0
    with open('players.json') as f:
         players = json.load(f)
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    print("| leaderBoard |              Score           |")
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    for x in players["players"]:
        print("| ", id, " | ",  x["playerHighScore"] ," |" )
        id = id + 1
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    print("|        [b] to go back                      |")
    print("|=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
    menuInput = input()
    if menuInput == "b":
        clr()
        startup()
def selections():
    menuInput = input()
    if menuInput == "1":
       playGame()
    elif menuInput == "2":
        stats()
       # input the file storing players 
    elif menuInput == "3":
        clr()
        displayPlayerlog()
    elif menuInput == "4":
        clr()
        exit()
    else :
        clr()
        startup()
def endGameSelections(score):
    y = {"playerHighScore" : score}
    filename='players.json'
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        print(currentPlayer)
        input()
        currentPlayer.update(y)
        print(currentPlayerID)
        file_data["players"][currentPlayerID] =  currentPlayer
        input()
        file.seek(0)
        json.dump(file_data, file, indent = 4)
    print("Score: ", score)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("    Return[1] New Game[2] Quit Game[3]")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    x = input()
    if x == "1":
        clr()
        cleargame()
        startup()
    elif x == '2':
        clr()
        cleargame()
        playGame()
    elif x == '3':
        clr()
        cleargame()
        quit()
    else:
        input()
        

def printMain():
    print("  _    _                     __  __             ")
    print(" | |  | |                   |  \/  |            ")
    print(" | |__| | __ _ _ __   __ _  | \  / | __ _ _ __  ")
    print(" |  __  |/ _` | '_ \ / _` | | |\/| |/ _` | '_ \ ")
    print(" | |  | | (_| | | | | (_| | | |  | | (_| | | | |")
    print(" |_|  |_|\__,_|_| |_|\__, | |_|  |_|\__,_|_| |_|")
    print("                      __/ |                     ")
    print("                     |___/                      ")
    print("-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    if currentPlayer == None:
        print("  Current Player: ")
    else:
        print("  Current Player: ", currentPlayer["playerFirstName"], currentPlayer["playerLastName"], currentPlayer["playerHighScore"])
    print(" ")
    print("     PLAY[1]  STATS[2]  PLAYERS[3]  QUIT[4] ")
    print(" ")
    print("-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")  
def startup():
    loadWords()
    printMain()
    selections()
def printword(selectedWord):
    for x in selectedWord:
         print( " "+x+" ", end=" ")
    print(" \n")
def cleargame():
    wrongAnswers.clear()
    correctGuesses.clear()
def testguess(selectedWord, atempts):
    score = 0
    isvalid = False
    inUse = False
    alreadyAtempted = False
    ammountGuess = 0
    clr()
    setBoard(atempts)
    for x in correctGuesses:
        score = score + 100
    print("                        Score:", score)
    for x in selectedWord:
        for l in correctGuesses:
            if x == l:   
                print( " "+l+" ", end=" ")
                isvalid = True
                ammountGuess = ammountGuess + 1
        if isvalid != True:  
            print( " _ ", end=" ")
        isvalid = False ##USed to prevent redundency __
    print(" \n")
    for l in wrongAnswers:
        print( l + " ", end=" ")
    print(" \n")

    if ammountGuess == len(str(selectedWord)):
            atempts = 0
            clr()
            print("you win")
            printword(selectedWord)
            endGameSelections(score)
    guess = input()
    if guess.isalpha() == False:
        testguess(selectedWord, atempts)
    else:
        guess = guess.lower()
        inWord = selectedWord.find(guess)
        if inWord == -1:
            
            for x in wrongAnswers:
                if guess == x:
                    alreadyAtempted = True
            if alreadyAtempted == False:
                wrongAnswers.append(guess)
                atempts = atempts + 1
        else:
           
            for x in correctGuesses:
                if guess == x:
                    inUse = True
            if inUse == False:
                correctGuesses.append(guess)
    if atempts != 6:
        if ammountGuess == len(str(selectedWord)):
            atempts = 0
            clr()
            print("you win")
            printword(selectedWord)
            endGameSelections(score)
        else:
            testguess(selectedWord, atempts)
    else: 
        atempts = 6
        clr()
        setBoard(atempts)
        printword(selectedWord)
        endGameSelections(score)
def setBoard(atempts):
    if atempts == 0:
        print("          +---+")
        print("          |   |")
        print("              |")
        print("              |")
        print("              |")
        print("              |")
        print("      =========")
        print(" ")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
    elif atempts == 1:
        print("          +---+")
        print("          |   |")
        print("          O   |")
        print("              |")
        print("              |")
        print("              |")
        print("      =========")
        print(" ")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
    elif atempts == 2:
        print("          +---+")
        print("          |   |")
        print("          O   |")
        print("          |   |")
        print("              |")
        print("              |")
        print("      =========")
        print(" ")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
    elif atempts == 3:
        print("          +---+")
        print("          |   |")
        print("          O   |")
        print("         /|   |")
        print("              |")
        print("              |")
        print("      =========")
        print(" ")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
    elif atempts == 4:
        print("          +---+")
        print("          |   |")
        print("          O   |")
        print("         /|\  |")
        print("              |")
        print("              |")
        print("      =========")
        print(" ")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
    elif atempts == 5:
        print("          +---+")
        print("          |   |")
        print("          O   |")
        print("         /|\  |")
        print("         /    |")
        print("              |")
        print("      =========")
        print(" ")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
    elif atempts == 6:
        print("          +---+")
        print("          |   |")
        print("          O   |")
        print("         /|\  |")
        print("         / \  |")
        print("              |")
        print("      =========")
        print("      GAME OVER")
        print("-=-=-=-=-=-=-=-=-=-=-=-")
def playGame():
    selectedWord = wordBank[random.randrange(0,20)]
    testguess(selectedWord, 0)
    clr()
def deletePlayer():
    print("select a player to delete")
    selectPlayer = input()
    selectPlayer = int(selectPlayer)
    filename='players.json'
    with open(filename) as file:
        file_data = json.load(file)
    file_data["players"].pop(selectPlayer)
    with open(filename, 'w') as file:
        json.dump(file_data, file, indent = 4)
        input("Json Dump")
    input()
    clr()
    displayPlayerlog()


clr()
startup()

