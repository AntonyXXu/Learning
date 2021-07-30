class C4:
    def __init__(self, height = 8, length = 8):
        self.height = height
        self.length = length
        self.board = [['_' for _ in range(self.length)] for _ in range(self.height)]
        self.last = [height - 1] * length
    
    def __str__(self):
        firstRow = [str(i) for i in range(1, self.length + 1)]
        print('|'.join(firstRow))
        for h in range(self.height):
            print('|'.join(self.board[h]))
        return ''
    
    def play(self):
        game = True
        while game:
            self.board = [['_' for _ in range(self.length)] for _ in range(self.height)]
            player1 = None
            player2 = None
            while player1 not in ["X", "O"]:
                player1 = input("Select X or O\t").upper()
            if player1 == "X":
                player2 == "O"
            else:
                player2 == "X"
            
            currPlayer = player1
            gameOver = None
            while not gameOver:
                row, col = self.turn(currPlayer)
                gameOver = self.checkGameOver(row, col)
                if gameOver:
                    print(self)
                    print(currPlayer + " Has Won!")
                    resp = input("Play again? Y/N\t").upper()
                    if resp == "Y":
                        break
                    else:
                        game = False
                        break
                else:
                    currPlayer = "X" if currPlayer == "O" else "O"
        print("Thanks for playing")

    def turn(self, player:str):
        print(self)
        col = None
        while True:
            col = int(input('Select a column to play your piece of ' + player + "\t"))
            if self.last[col - 1] == 0:
                print("Cannot put your piece on this column")
            else:
                break
        row = self.last[col]
        self.board[row][col - 1] = player
        self.last[col] -= 1
        return row, col - 1

    def checkGameOver(self, row, col) -> str:
        # check vertical
        down = self.calcContinuous(1, 0, row, col)
        if down + 1 >= 4:
            return self.board[row][col]
        left = self.calcContinuous(0, -1, row, col)
        right = self.calcContinuous(0, 1, row, col)
        if left + right + 1 >= 4:
            return self.board[row][col]
        upLeft = left = self.calcContinuous(-1, -1, row, col)
        downRight = self.calcContinuous(1, 1, row, col)
        if upLeft + downRight + 1>= 4:
            return self.board[row][col]
        upRight = left = self.calcContinuous(-1, 1, row, col)
        downLeft = self.calcContinuous(1, -1, row, col)
        if upRight + downLeft + 1>= 4:
            return self.board[row][col]
        #No winner
        return None

    def calcContinuous(self, horizontal, vertical, row, col) -> int:
        curr = self.board[row][col]
        row += horizontal
        col += vertical
        counter = 0
        while row >= 0 and row < self.height and col >= 0 and col < self.length and self.board[row][col] == curr:
            counter += 1
            row += horizontal
            col += vertical
        return counter
            


c = C4()
c.play()
    