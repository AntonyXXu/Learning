import collections
from random import randrange
PLAYER1 = "X"
PLAYER2 = "O"

TIE = "Tie"
PLAYER1WIN = "X wins"
PLAYER2WIN = "O wins"


class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [['-' for _ in range(self.cols)]
                      for _ in range(self.rows)]
        self.availableRows = [self.rows - 1 for _ in range(self.cols)]

    def show(self):
        print('|'.join([str(col) for col in range(self.cols)]))
        for row in self.board:
            print('|'.join(row))
        print("")


class ConnectFourGame:
    def __init__(self):
        self.board = Board()
        self.ai_1 = AI(PLAYER1)
        self.ai_2 = AI(PLAYER2)
        self.current_ai = self.ai_1
        self.gameActive = True

    def playGame(self):
        while self.gameActive:
            playCoordinates = self.playTurn()
            print(playCoordinates)
            self.board.show()
            gameStatus = self.checkGameStatus(playCoordinates)
            if gameStatus:
                self.gameActive = False
                print(gameStatus)

            self.swapPlayers()

    def playTurn(self):
        # col = self.current_ai.randomColumn()
        # while self.board.availableRows[col] < 0:
        #     col = self.current_ai.randomColumn()
        col = self.current_ai.playMove(self.board)
        print(col)
        row = self.board.availableRows[col]
        self.board.availableRows[col] -= 1
        self.board.board[row][col] = self.current_ai.player
        return (row, col)

    def checkGameStatus(self, playCoordinates):
        tie = True
        for availableRow in self.board.availableRows:
            if availableRow >= 0:
                tie = False
        if tie:
            return TIE
        if (self.countContinuousPieces(playCoordinates, 1, 0) >= 4
            or self.countContinuousPieces(playCoordinates, 0, -1) + self.countContinuousPieces(playCoordinates, 0, 1) - 1 >= 4
            or self.countContinuousPieces(playCoordinates, -1, -1) + self.countContinuousPieces(playCoordinates, 1, 1) - 1 >= 4
                or self.countContinuousPieces(playCoordinates, -1, 1) + self.countContinuousPieces(playCoordinates, 1, -1) - 1 >= 4):
            if self.current_ai.player == PLAYER1:
                return PLAYER1WIN
            else:
                return PLAYER2WIN
        return None

    def countContinuousPieces(self, playCoordinates,  v_direction, h_direction):
        row, col = playCoordinates
        continuous = 0
        while (row >= 0 and col >= 0 and row < self.board.rows and col < self.board.cols
               and self.board.board[row][col] == self.current_ai.player):
            row += v_direction
            col += h_direction
            continuous += 1
        return continuous

    def swapPlayers(self):
        if self.current_ai == self.ai_1:
            self.current_ai = self.ai_2
        else:
            self.current_ai = self.ai_1


class AI:
    def __init__(self, player):
        self.player = player

    def randomColumn(self):
        return randrange(7)

    def playMove(self, board):
        for col in range(board.cols):
            row = board.availableRows[col]
            if row < 0:
                continue
            board.board[row][col] = self.player
            if self.player == PLAYER1:
                win = PLAYER1WIN
            else:
                win = PLAYER2WIN
            coordinates = (row, col)
            if self.checkGameStatus(coordinates, board) == win:
                board.board[row][col] = '-'
                print("WIN WITH AI")
                return col
            board.board[row][col] = '-'
        col = self.randomColumn()
        while board.availableRows[col] < 0:
            col = self.randomColumn()
        return col

    def checkGameStatus(self, playCoordinates, board):
        tie = True
        for availableRow in board.availableRows:
            if availableRow >= 0:
                tie = False
        if tie:
            return TIE
        if (self.countContinuousPieces(playCoordinates, 1, 0, board) >= 4
            or self.countContinuousPieces(playCoordinates, 0, -1, board) + self.countContinuousPieces(playCoordinates, 0, 1, board) - 1 >= 4
            or self.countContinuousPieces(playCoordinates, -1, -1, board) + self.countContinuousPieces(playCoordinates, 1, 1, board) - 1 >= 4
                or self.countContinuousPieces(playCoordinates, -1, 1, board) + self.countContinuousPieces(playCoordinates, 1, -1, board) - 1 >= 4):
            if self.player == PLAYER1:
                return PLAYER1WIN
            else:
                return PLAYER2WIN
        return None

    def countContinuousPieces(self, playCoordinates,  v_direction, h_direction, board):
        row, col = playCoordinates
        continuous = 0
        while (row >= 0 and col >= 0 and row < board.rows and col < board.cols
               and board.board[row][col] == self.player):
            row += v_direction
            col += h_direction
            continuous += 1
        return continuous


game = ConnectFourGame()
game.playGame()
