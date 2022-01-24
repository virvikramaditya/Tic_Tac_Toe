
print("hello sir this is my tic tac toe program")
#     this is the code for tic tac toe program
import random
board=["_","_","_",
       "_","_","_",
       "_","_","_"]
currentplayer="x"
winner=None
gamerunning=True


# so first we have to print the game board
def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("___________")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("___________")
    print(board[6]+" | "+board[7]+" | "+board[8])
# printBoard(board)    



# take players input
def playerInput(board):
    inp=int(input("enter the number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1]=="_":
        board[inp-1] = currentplayer
    else:
        print("oops player is already in that spot!")


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_": 
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True   
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[3]
        return True 

def checkRow(board):
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True  
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True                    

def checkDiagonal(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True 
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True 


def checkTie(board):
    global gamerunning
    if "_" not in board:
        printBoard(board)
        print("It is a Tie")
        gamerunning = False        


def checkwin(board):
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")



# switch the player
def switchplayer():
    global currentplayer
    if currentplayer == "x":
        currentplayer = "o"
    else:
        currentplayer = "x"

#computer
def computer(board):
    while currentplayer == "o":
        position = random.randint(0,8)
        if board[position] == "_":
            board[position] = "o"
            switchplayer()



# check for win or tie Again
while gamerunning:
    printBoard(board)
    playerInput(board)
    checkwin(board)
    checkTie(board)
    switchplayer()
    computer(board)
    checkwin(board)
    checkTie(board)





