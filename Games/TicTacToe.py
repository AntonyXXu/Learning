# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:14:42 2021

@author: Test
"""

#TicTacToe
from random import randint

class TicTacToe():
    def __init__(self):
        #Initialize Board state
        self.board = [" "] * 9
        
    def showBoard(self):
        #Print the board, with its references. Alternatively just print out board required
        for i in range (len(self.board)):
            #if i is 3,6,9, create a new line
            if (i+1)%3 == 0:
                print(self.board[i] + \
            #print tic tac toe cell references
                "\t" + str((i-1)) +"|"+str(i) + "|" + str(i+1), end = "\n")
            #else separate with a tab
            else:
                print(self.board[i] + "|", end = "")
    
    def isEmpty(self,cell):
        #Cell input - 1 to get cell reference 
        return self.board[int(cell)-1] == " "
    
    def isFull(self):
        if " " in self.board:
            return False
        else:
            return True
    
    def Move(self,char,cell):
        #Move by human or computer
        assert char == "x" or char == "o", "character must be x or o"
        self.board[int(cell) - 1] = str(char)
        
    def isWinner(self,char):
        #list of possible scenarios
        return (self.board[0] == char and self.board[1] == char and self.board[2] == char) or \
            (self.board[3] == char and self.board[4] == char and self.board[5] == char) or \
            (self.board[6] == char and self.board[7] == char and self.board[8] == char) or \
            (self.board[0] == char and self.board[3] == char and self.board[6] == char) or \
            (self.board[1] == char and self.board[4] == char and self.board[7] == char) or \
            (self.board[2] == char and self.board[5] == char and self.board[8] == char) or \
            (self.board[0] == char and self.board[4] == char and self.board[8] == char) or \
            (self.board[2] == char and self.board[4] == char and self.board[6] == char)
    
    def WhoWon(self):
        #declare winner
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

     
#   Cannot use this function, need a copy of it
#    def TestWinningMove(self,char,cell):
#        #test winning moves for AI
#        #cell must be empty
#        if self.board[cell-1] != " ":
#            return False
#        else:
#            #test if cell can win, temporarily change boardstate
#            self.board[cell-1] = str(char)
#            Win = self.isWinner(char)
#            self.board[cell-1] = " "
#            return Win 
        

    def TestWinningMove(self,char,cell):
        #test winning moves for AI
        #cell must be empty
        if self.board[cell-1] != " ":
            return False
        else:
            #test if cell can win, temporarily change boardstate
            copy = self
            copy.board[cell-1] = str(char)
            Win = copy.isWinner(char)
            copy.board[cell-1] = " "
            return Win 
        
    def AI_random(self):
        #Random AI moves
        r = randint(0,9)
        while not self.isEmpty(r):
            r = randint(0,9)
        return r

    def AI_smart(self,turn):
        #AI targets game winning move, then tries to block a player win.
        for i in range (0,9):
            if self.TestWinningMove(turn,i):
                return i
        #specify player turn to test for blocking
        if turn == "x":
            playerTurn = "o"
        else:
            playerTurn = "x"
        for i in range(0,9):
            if self.TestWinningMove(playerTurn, i):
                return i
        #Take board middle, corners, then edges
        Order = "513792468"
        for i in Order:
            if self.isEmpty(i):
                return i
        
def RunGame():
    print("Welcome to TicTacToe")
    playGame = True
    while playGame:
        print("1. Player vs Player","2. Player vs Random AI", "3. Player vs Smart AI", \
                  "4. Quit", sep = "\n")
        mode = input("Select your choice: \t")
        #User inputs mode/quit
        while str(mode) not in "1234":
            mode = input("Select your choice: \t")
        
        #Quit
        if mode == "4":
            print("Thank you for playing")
            playGame = False
        
        #Player vs Player
        elif mode == "1":
            board = TicTacToe()
            turn = "x"
            gameOver = False
            while not gameOver:
                board.showBoard()
                print("\nIt is ",turn,"'s turn")
                
                #Re-input until a valid move is presented
                playerMove = "0"
                while int(playerMove) not in [i for i in range(1,10)] :
                    playerMove = input("What is your move? \t")
                    if not board.isEmpty(int(playerMove)):
                        print("That square is currently filled. Please pick another move")
                        playerMove = "0"
                board.Move(turn,int(playerMove))
                
                #Determine game over state, check winner
                Winner = board.WhoWon()
                if Winner != "":
                    board.showBoard()
                    print("Congratulations ",turn," on winning! \n" + \
                          "Play Again? \n")
                    gameOver = True
                #check if it's a tie
                elif board.isFull():
                    board.showBoard()
                    print("It's a Tie! \n" + "Play Again? \n")
                    gameOver = True
                #Swap turns, game is not over
                else:
                    if turn == "x":
                        turn = "o"
                    else:
                        turn = "x"
                        
        elif mode == "2":
            board = TicTacToe()
            turn = "x"
            gameOver = False
            
            #Player Selects x or o
            playerTurn = "0"
            while playerTurn not in "xo":
                    playerTurn = input("Play as x or o? \t").lower()
                    
            while not gameOver:
                board.showBoard()
                print("\nIt is ",turn,"'s turn")
                
                #Player Move
                if turn == playerTurn:
                    playerMove = "0"
                    while int(playerMove) not in [i for i in range(1,10)]:
                        playerMove = input("What is your move? \t")
                        if not board.isEmpty(int(playerMove)):
                            print("That square is currently filled. Please pick another move")
                            playerMove = "0"
                    board.Move(turn,int(playerMove))
                
                #Computer Move
                else:
                    print("Computer Playing...", end = "\t")
                    board.Move(turn,board.AI_random())
                    print("Played")
            
                #Determine game over state, check winner
                Winner = board.WhoWon()
                if Winner != "":
                    board.showBoard()
                    print("Congratulations ", turn," on winning! \nPlay Again? \n")
                    gameOver = True
                elif board.isFull():
                    board.showBoard()
                    print("It's a Tie! \n" + "Play Again? \n")
                    gameOver = True
                else:
                    if turn == "x":
                        turn = "o"
                    else:
                        turn = "x"
                        
        elif mode == "3":
            board = TicTacToe()
            turn = "x"
            gameOver = False
            playerTurn = "0"
            while playerTurn not in "xo":
                playerTurn = input("Play as x or o? \t").lower()
                
            while not gameOver:
                board.showBoard()
                print("\nIt is ",turn,"'s turn")
                
                if turn == playerTurn:
                    playerMove = "0"
                    while int(playerMove) not in [i for i in range(1,10)]:
                        playerMove = input("What is your move? \t")
                        if not board.isEmpty(int(playerMove)):
                            print("That square is currently filled. Please pick another move")
                            playerMove = "0"
                    board.Move(turn,int(playerMove))
                else:
                    print("Computer Playing...", end = "\t")
                    board.Move(turn,board.AI_smart(turn))
                    print("Played")
                    
                #Determine game over state
                Winner = board.WhoWon()
                if Winner != "":
                    board.showBoard()
                    print("Congratulations ", turn," on winning! \nPlay Again? \n")
                    gameOver = True
                elif board.isFull():
                    board.showBoard()
                    print("It's a Tie! \n" + "Play Again? \n")
                    gameOver = True
                else:
                    if turn == "x":
                        turn = "o"
                    else:
                        turn = "x"
        
#Create program
if __name__ == "__main__":
    RunGame()


        
        