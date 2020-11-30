# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:57:39 2020

@author: OCAC
"""
board=[" " for x in range(10)]

def insertPosition(letter,pos):
    board[pos]=letter

def spaceIsfree(pos):
    return board[pos]==" "
 
def printBoard(board):
    print("   |   |   ")
    print(" "+board[1]+" | "+board[2]+" | "+board[3] )
    print("   |   |   ")
    print("------------")
    
    print("   |   |   ")
    print(" "+board[4]+" | "+board[5]+" | "+board[6] )
    print("   |   |   ")
    print("------------")
    
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | "+board[9] )
    print("   |   |   ")
    
def isBoardfull(board):
    if board.count(" ")>1:                         #counts number of free spaces
        return False
    else:
        return True
    
def isWinner(boa,let): 
    return (boa[1]==let and boa[2]==let and boa[3]==let) or \
    (boa[4]==let and boa[5]==let and boa[6]==let) or \
    (boa[7]==let and boa[8]==let and boa[9]==let) or \
    (boa[1]==let and boa[4]==let and boa[7]==let) or \
    (boa[2]==let and boa[5]==let and boa[8]==let) or \
    (boa[3]==let and boa[6]==let and boa[9]==let) or \
    (boa[1]==let and boa[5]==let and boa[9]==let) or \
    (boa[3]==let and boa[5]==let and boa[7]==let)
    
def playerMove():
    run=True
    while run:
        move=input("Please Select A Position To Enter \"X\"Between 1 to 9:")
        try:
            move =int(move)
            if move>0 and move <10:
                if spaceIsfree(move):
                    run =False
                    insertPosition("X",move)
                else:
                    print("Sorry!The Space Is Occupied")
            else:
                print("Please Type a Valid Number between 1-9!")
        except:                                                    #if try failed
            print("Plaese Type a Number!")
            
def computerMove():
    possibleMoves=[x for x,letter in enumerate(board) if letter ==" " and x!=0]
    move=0
    
    for let in ["O","X"]:
        for i in possibleMoves:
            boardCopy=board[:]
            boardCopy[i]=let
            if isWinner(boardCopy,let):
                move=i
                return move
            
    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen)>0:
        move =selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move=5
        return move
    
    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen)>0:
        move=selectRandom(edgesOpen)
        return move
    
def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]    
    
def main():
    print("Welcome To The Game!")
    printBoard(board)
    
    while not(isBoardfull(board)):
        if not(isWinner(board,"O")):
            playerMove()
            printBoard(board)
        else:
            print("Sorry You Loose!")
            break
        
        if not(isWinner(board,"X")):
            move=computerMove()
            if move==None:
                print(" ")
                break
            else:
                insertPosition("O",move)
                print("Computer Placed an \"O\" on position",move,":")
                printBoard(board)        
        else:
            print("You Win!")
            break
    
    
    if isBoardfull(board):
        print("The Game Is Tied!")
        
        
while True:
    decision=input("Do You want to Play? (y/n):")
    if decision.lower()=="y":
        board=[" " for x in range(10)]
        print("--------------------------------")
        main()
    else:
        break
    