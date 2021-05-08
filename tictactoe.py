import random as rd
board=[" " for i in range(10)]

def boraddesign(board):
    print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print("-----------")
    print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print("-----------")
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")

def inputtoboard(letter,x):
    board[x]=letter

def winner(board,l):
    if ((board[1]==l and board[2]==l and board[3]==l) or(board[4]==l and board[5]==l and board[6]==l) or(board[7]==l and board[8]==l and board[9]==l) or
    (board[1]==l and board[4]==l and board[7]==l) or
    (board[2]==l and board[5]==l and board[8]==l) or
    (board[3]==l and board[6]==l and board[9]==l) or
    (board[1]==l and board[5]==l and board[9]==l) or
    (board[3]==l and board[5]==l and board[7]==l)):
        return True
    else:
        return False

def isplaceempty(pos):
    if board[pos]==" ":
        return True
    else:
        return False

def isboardfull(board):
    if board.count(" ")>=1:
        return False
    else:
        return True

def usermove():
    run=True
    while run:
        mv=input("Enter the position: ")
        try:
            mv=int(mv)
            if (mv>0 and mv<10):
                if isplaceempty(mv):
                    inputtoboard('X',mv)
                    run=False
                else:
                    print("The position is filled already, OOPS!!")
            else:
                print("Enter a number between 1 to 9")
        except Exception as e:
            print("What is this bro, give number!")


def compmove():
    possiblemoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ["O","X"]:
        for i in possiblemoves:
            boardcpy=board[:]
            boardcpy[i]=let
            if winner(boardcpy,let):
                move=i
                return move
    corners=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners)>0:
        move=rd.choice(corners)
        return move
    if 5 in possiblemoves:
        move=5
        return move
    edges=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edges.append(i)
    if len(edges)>0:
        move=rd.choice(edges)
        return move


if __name__=="__main__":
    while True:
        play=input("Like to play a game?(y/n) ")
        if play=='y':
            board=[" " for x in range(10)]
            boraddesign(board)
            while not(isboardfull(board)):
                if not(winner(board,'O')):
                    usermove()
                    boraddesign(board)
                else:
                    print("Unexpected but a welcomed one! The computer Won(x_x) ")
                    break
                if not(winner(board,'X')):
                    move=compmove()
                    if move==0 or move==None:
                        print("Tie!")
                        break
                    else:
                        inputtoboard('O',move)
                        print("Computer turn!")
                        print(boraddesign(board))
                        print("Your turn kid!")

                else:
                    print("The force is with you, Kid!")
                    break
            if isboardfull(board):
                print("Tie!")
                break
        else:
            print("Come back if you wish!!")
            break
