import random 

GAMEISOVER = 0
GAMEISLIVE = 1
PLAYAGAIN = 2


theBoard = {"top-Left" : " ", "top-Middle" : " ", "top-Right" : " ", \
            "mid-Left" : " ", "mid-Middle" : " ", "mid-Right" : " ", \
            "low-Left" : " ", "low-Middle" : " ", "low-Right" : " "}

setup = {"player":' ', 'computer':' '}

possibleMoves = []

currentPlayer = ' '

def printBoard():
    print("\n")
    print(theBoard['top-Left'] + '|' + theBoard['top-Middle'] + '|' + theBoard['top-Right'] )
    print('-----')
    print(theBoard['mid-Left'] + '|' + theBoard['mid-Middle'] + '|' + theBoard['mid-Right'] ) 
    print('-----')
    print(theBoard['low-Left'] + '|' + theBoard['low-Middle'] + '|' + theBoard['low-Right'] )
    print("\n")

def isBoardFull():
    for key in theBoard.keys():
        if theBoard[key] == ' ':
            return False
    return True

def minMax(depth, isMaximizing):
    if isWinner(setup["computer"]) and isMaximizing:
        return 1
    if isWinner(setup["player"]) and not isMaximizing:
        return -1
    if isBoardFull():
        return 0
    
    if isMaximizing:
        max_val = float('-inf')
        for key in possibleMoves:
            if theBoard[key] == ' ':
                theBoard[key] = setup["computer"]
                eval = minMax(depth + 1, False)
                theBoard[key] = ' '
                max_val = max(max_val, eval)
        return max_val
    else:
        min_val = float('inf')
        for key in possibleMoves:
            if theBoard[key] == ' ':
                theBoard[key] = setup["player"]
                eval = minMax(depth + 1, True)
                theBoard[key] = ' '
                min_val = min(min_val, eval)
        return min_val

def move(choice, piece):
    theBoard[choice] = piece

def whoStarts():
    return random.choice(['computer', 'player'])

def playerMove(piece):
    print("Make a move! Choose (top-, mid-, low-) and (Left, Middle, Right)" ) 
    choice = input()
    while not((choice == 'top-Left' or choice == 'top-Middle' or choice == 'top-Right' or \
              choice == 'mid-Left' or choice == 'mid-Middle' or choice == 'mid-Right' or \
              choice == 'low-Left' or choice == 'low-Middle' or choice == 'low-Right') and theBoard[choice] == ' '):
        print("Either is the tile taken or wrong input. Please choose (top-, mid-, low-) & (Left, Middle, Right) and a free tile")
        choice = input()
    move(choice, piece)

def computerMove(piece):
    move(random.choice(possibleMoves), piece)


def computerAiMove():
    bestScore = float('-inf')
    bestMove = ' '
    for key in possibleMoves:
        if theBoard[key] == ' ':
            theBoard[key] = setup["computer"]
            score = minMax(0, False)
            theBoard[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    move(bestMove, setup['computer'])

def nextMove(currentPlayer, setup):
    if isWinner(currentPlayer):
        return
    if currentPlayer == 'computer':
        computerAiMove()
        return 'player'
    else:
        playerMove(setup.get('player'))
        return 'computer'

def isWinner(piece):
    return ((theBoard['top-Right'] == piece and theBoard['mid-Right'] == piece and theBoard['low-Right'] == piece) or \
            (theBoard['top-Middle'] == piece and theBoard['mid-Middle'] == piece and theBoard['low-Middle'] == piece) or \
            (theBoard['top-Left'] == piece and theBoard['mid-Left'] == piece and theBoard['low-Left'] == piece) or \
            (theBoard['top-Left'] == piece and theBoard['top-Middle'] == piece and theBoard['top-Right'] == piece) or \
            (theBoard['mid-Left'] == piece and theBoard['mid-Middle'] == piece and theBoard['mid-Right'] == piece) or \
            (theBoard['low-Left'] == piece and theBoard['low-Middle'] == piece and theBoard['low-Right'] == piece) or \
            (theBoard['top-Left'] == piece and theBoard['mid-Middle'] == piece and theBoard['low-Right'] == piece) or \
            (theBoard['low-Left'] == piece and theBoard['mid-Middle'] == piece and theBoard['top-Right'] == piece))



while True:
    theBoard = {"top-Left" : " ", "top-Middle" : " ", "top-Right" : " ", \
            "mid-Left" : " ", "mid-Middle" : " ", "mid-Right" : " ", \
            "low-Left" : " ", "low-Middle" : " ", "low-Right" : " "}
    possibleMoves = []
    for key in theBoard.keys():
        possibleMoves.append(key)
    print(possibleMoves)
    print("Welcome to a game of tic-tac-toe!")
    print("Do you wanna be X or O??")

    # asks user for input and sets that choice for the game
    choice = input().upper()
    while not(choice == 'X' or choice == 'O'):
        print("Wrong input!! Please pick either X or O!")
        choice = input().upper()
    if choice == 'X':
        setup['player'] = 'X'
        setup['computer'] = 'O'
    else:
        setup['player'] = 'O'
        setup['computer'] = 'X'
    

    # decides who starts between the player or computer 
    if whoStarts() == 'computer':
        currentPlayer = 'computer'
    else:
        currentPlayer = 'player'

    print(currentPlayer + " starts!")
    printBoard()
    gameStatus = GAMEISLIVE

    while True:
        oldPlayer = currentPlayer
        currentPlayer = nextMove(currentPlayer, setup)
        while( not isWinner(setup[oldPlayer]) and not isBoardFull()):
            printBoard()
            oldPlayer = currentPlayer
            currentPlayer = nextMove(currentPlayer, setup)

        printBoard()
        if not isBoardFull():
            print("The " + oldPlayer + " wins!!")
        else:
            print("No one won :( !")

        
        print("Wanna play again? Enter 'Y/N'")
        choice = input().upper()
        while not(choice == 'Y' or choice == 'N'):
            print("Wrong input!! Please pick either Y or N!")
            choice = input().upper()
        if choice == 'Y':
            break
        else:
            exit()



