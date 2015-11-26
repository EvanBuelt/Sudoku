import IO
import Solve

# Singles in box
# Hidden Singles in row/column/box
# Values locked to row/column in box
# Pairs in row/column/box
# Triples in row/column/box
# Quads in row/column/box
# Hidden Pairs in row/column/box
# Hidden Triples/Quads in row/column/box (rare)
# X-Wing
# Swordfish

class Cell:
    def __init__(self, value = None):
        # Initialize possible values from 1 to 9
        self.possibleValues = [i for i in range(1,10)]
        
        # Initialize value.
        if value is None:
            self.setValue(0)
        else :
            self.setValue(value)

    def setValue(self, value):
        self.value = value
        if value is not 0:
            self.possibleValues = []
        return
    
    def removePV(self, value):
        if value in self.possibleValues:
            self.possibleValues.remove(value)
        return

    def addPV(self, value):
        if value not in self.possibleValues:
            self.possibleValues.append(value)
        return

class Board:
    def __init__(self, filePath):
        self.board = IO.loadBoard(filePath)
        self._board = []
        for i in range(0,9):
            row = []
            for j in range(0,9):
                row.append(Cell(self.board[i][j]))
            self._board.append(row)

        for i in range(0,9):
            for j in range(0,9):
                self.removePV(i, j)

    def setValue(self, value, row, column):
        self.board[row][column] = value
        self._board[row][column].setValue(value)
        self.removePV(row, column)
        
    def removePV(self, row, column):
        self.removePV_Row(row, column)
        self.removePV_Column(row, column)
        self.removePV_Box(row, column)

    def removePVOptimized(self, row, column):
        x = 3 * (row/3)
        y = 3 * (column/3)
        value = self._board[row][column].value

        for i in range(0,9):
            self._board[row][i].removePV(value)
            self._board[i][column].removePV(value)
            self._board[x + (i/3)][y + (i%3)].removePV(value)
        
    def removePV_Row(self, row, column):
        value = self._board[row][column].value
        for j in range(0, 9):
            self._board[row][j].removePV(value)
        return

    def removePV_Column(self, row, column):
        value = self._board[row][column].value
        for i in range(0, 9):
            self._board[i][column].removePV(value)
        return

    def removePV_Box(self, row, column):
        x = 3 * (row/3)
        y = 3 * (column/3)

        value = self._board[row][column].value
        
        for i in range(x,x+3):
            for j in range(y,y+3):
                self._board[i][j].removePV(value)
        return

class ElegantSolver:
    def __init__(self, filePath):
        # Load in board, and time how long it takes to solve.
        self.board = Board(filePath)

    def setValue(self, value, i, j):
        self.board.setValue(value, i, j)
        
    def solve(self):
        running = True
        while running:
            #IO.printBoard(self.board.board)
            result3 = self.double()
            result4 = self.hiddenDouble()
            result1 = self.single()
            result2 = self.hiddenSingle()
            #IO.printBoard(self.board.board)
            #for i in range(0,9):
            #    print i
            #    for j in range(0,9):
            #        print self.board._board[i][j].possibleValues
            #    print ''
            running = result1 or result2
            #print result1, result2, result3, result4

        #for i in range(0,9):
        #    print i
        #    for j in range(0,9):
        #        print self.board._board[i][j].possibleValues
        #    print ''
        solvedBoard, result = SmartBruteForce(self.board)

        return solvedBoard, result

    def single(self):
        board = self.board._board
        found = False
        for i in range(0,9):
            for j in range(0,9):
                if len(board[i][j].possibleValues) is 1:
                    found = True
                    self.setValue(board[i][j].possibleValues[0], i, j)

        #print 'S', found
        return found
    
    def hiddenSingle(self):
        found1 = self.hiddenSingleRow()
        found2 = self.hiddenSingleColumn()
        found3 = self.hiddenSingleBox()
        #found = (self.hiddenSingleRow() or
        #         self.hiddenSingleColumn() or
        #         self.hiddenSingleBox())
        found = found1 or found2 or found3
        return found

    def double(self):
        found1 = self.doubleRow()
        found2 = self.doubleColumn()
        found3 = self.doubleBox()
        #found = (self.doubleRow() or
        #         self.doubleColumn() or
        #         self.doubleBox())
        found = found1 or found2 or found3
        return found

    def hiddenDouble(self):
        found1 = self.hiddenDoubleRow()
        found2 = self.hiddenDoubleColumn()
        found3 = self.hiddenDoubleBox()
        #found = (self.hiddenDoubleRow() or
        #         self.hiddenDoubleColumn() or
        #         self.hiddenDoubleBox())
        found = found1 or found2 or found3
        return found

    def hiddenSingleRow(self):
        numberCount = [(0, []) for value in range(0,9)]
        board = self.board._board
        found = False

        # Find single in row
        for i in range(0,9):
            for j in range(0,9):
                for value in board[i][j].possibleValues:
                    count, location = numberCount[value - 1]
                    count += 1
                    location.append((i, j))
                    numberCount[value - 1] = (count, location)
            for value in range(1,10):
                if numberCount[value - 1][0] is 1:
                    (x, y) = numberCount[value - 1][1][0]
                    self.setValue(value, x, y)
                    found = True
            numberCount = [(0, []) for value in range(0,9)]
        return found

    def hiddenSingleColumn(self):
        numberCount = [(0, []) for value in range(0,9)]
        board = self.board._board
        found = False

        # Find single in column
        for j in range(0,9):
            for i in range(0,9):
                for value in board[i][j].possibleValues:
                    count, location = numberCount[value - 1]
                    count += 1
                    location.append((i, j))
                    numberCount[value - 1] = (count, location)
            for value in range(1,10):
                if numberCount[value - 1][0] is 1:
                    (x, y) = numberCount[value - 1][1][0]
                    self.setValue(value, x, y)
                    found = True
            numberCount = [(0, []) for value in range(0,9)]
        return found

    def hiddenSingleBox(self):
        numberCount = [(0, []) for value in range(0,9)]
        board = self.board._board
        found = False

        # Find single in box
        for i in range(0,3):
            for j in range(0,3):
                for k in range(0,3):
                    for l in range(0,3):
                        for value in board[i*3 + k][j*3 +l].possibleValues:
                            count, location = numberCount[value - 1]
                            count += 1
                            location.append((i*3 + k, j*3 +l))
                            numberCount[value - 1] = (count, location)
                for value in range(1,10):
                    if numberCount[value - 1][0] is 1:
                        (x, y) = numberCount[value - 1][1][0]
                        self.setValue(value, x, y)
                        found = True
                numberCount = [(0, []) for value in range(0,9)]
        return found

    def doubleRow(self):
        board = self.board._board
        doubles = []
        found = False
        
        # Find double in row
        for i in range(0,9):
            for j in range(0,9):
                # Append any cell with only 2 possible values
                if len(board[i][j].possibleValues) is 2:
                    doubles.append(board[i][j])
            if len(doubles) > 1:
                for k in range(0, len(doubles)):
                    for l in range(k + 1, len(doubles)):
                        if (doubles[k].possibleValues[0] == doubles[l].possibleValues[0] and
                            doubles[k].possibleValues[1] == doubles[l].possibleValues[1]):
                            value1 = doubles[k].possibleValues[0]
                            value2 = doubles[k].possibleValues[1]
                            for column in range(0, 9):
                                board[i][column].removePV(value1)
                                board[i][column].removePV(value2)
                            doubles[k].addPV(value1)
                            doubles[k].addPV(value2)
                            doubles[l].addPV(value1)
                            doubles[l].addPV(value2)
                            found = True
            doubles = []
        return found

    def doubleColumn(self):
        board = self.board._board
        doubles = []
        found = False

        # Find double in column
        for j in range(0,9):
            for i in range(0,9):
                # Append any cell with only 2 possible values
                if len(board[i][j].possibleValues) is 2:
                    doubles.append(board[i][j])
            if len(doubles) > 1:
                for k in range(0, len(doubles)):
                    for l in range(k + 1, len(doubles)):
                        if (doubles[k].possibleValues[0] == doubles[l].possibleValues[0] and
                            doubles[k].possibleValues[1] == doubles[l].possibleValues[1]):
                            value1 = doubles[k].possibleValues[0]
                            value2 = doubles[k].possibleValues[1]
                            for row in range(0, 9):
                                board[row][j].removePV(value1)
                                board[row][j].removePV(value2)
                            doubles[k].addPV(value1)
                            doubles[k].addPV(value2)
                            doubles[l].addPV(value1)
                            doubles[l].addPV(value2)
                            found = True
            doubles = []
        return found

    def doubleBox(self):
        board = self.board._board
        doubles = []
        found = False

        # Find double in 3x3 box
        for i in range(0,3):
            for j in range(0,3):
                for k in range(0,3):
                    for l in range(0,3):
                        if len(board[i*3 + k][j*3 + l].possibleValues) is 2:
                            doubles.append(board[i*3 + k][j*3 + l])
                if len(doubles) > 1:
                    for k in range(0, len(doubles)):
                        for l in range(k + 1, len(doubles)):
                            if (doubles[k].possibleValues[0] == doubles[l].possibleValues[0] and
                                doubles[k].possibleValues[1] == doubles[l].possibleValues[1]):
                                value1 = doubles[k].possibleValues[0]
                                value2 = doubles[k].possibleValues[1]
                                for row in range(0, 3):
                                    for column in range(0,3):
                                        board[i*3 + row][j*3 + column].removePV(value1)
                                        board[i*3 + row][j*3 + column].removePV(value2)
                                doubles[k].addPV(value1)
                                doubles[k].addPV(value2)
                                doubles[l].addPV(value1)
                                doubles[l].addPV(value2)
                                found = True
                doubles = []
        return found

    def hiddenDoubleRow(self):
        numberCount = [(0, []) for value in range(0,9)]
        doubles = []
        board = self.board._board
        found = False

        # Find double in row
        for i in range(0,9):
            for j in range(0,9):
                for value in board[i][j].possibleValues:
                    count, location = numberCount[value - 1]
                    count += 1
                    location.append((i, j))
                    numberCount[value - 1] = (count, location)
            for value in range(1,10):
                if numberCount[value - 1][0] is 2:
                    doubles.append((value,numberCount[value-1][1]))
            if len(doubles) > 1:
                for k in range(0, len(doubles)):
                    for l in range(k + 1, len(doubles)):
                        if (doubles[k][1][0] == doubles[l][1][0] and
                            doubles[k][1][1] == doubles[l][1][1]):
                            x1 = doubles[k][1][0][0]
                            x2 = doubles[k][1][1][0]
                            y1 = doubles[k][1][0][1]
                            y2 = doubles[k][1][1][1]
                            value1 = doubles[k][0]
                            value2 = doubles[l][0]
                            for value in range(0, 9):
                                board[x1][y1].removePV(value)
                                board[x2][y2].removePV(value)
                            board[x1][y1].addPV(value1)
                            board[x1][y1].addPV(value2)
                            board[x2][y2].addPV(value1)
                            board[x2][y2].addPV(value2)
                            found = True
            numberCount = [(0, []) for value in range(0,9)]
            doubles = []
        return found

    def hiddenDoubleColumn(self):
        numberCount = [(0, []) for value in range(0,9)]
        doubles = []
        board = self.board._board
        found = False

        # Find double in column
        for j in range(0,9):
            for i in range(0,9):
                for value in board[i][j].possibleValues:
                    count, location = numberCount[value - 1]
                    count += 1
                    location.append((i, j))
                    numberCount[value - 1] = (count, location)
            for value in range(1,10):
                if numberCount[value - 1][0] is 2:
                    doubles.append((value,numberCount[value-1][1]))
            if len(doubles) > 1:
                for k in range(0, len(doubles)):
                    for l in range(k + 1, len(doubles)):
                        if (doubles[k][1][0] == doubles[l][1][0] and
                            doubles[k][1][1] == doubles[l][1][1]):
                            x1 = doubles[k][1][0][0]
                            x2 = doubles[k][1][1][0]
                            y1 = doubles[k][1][0][1]
                            y2 = doubles[k][1][1][1]
                            value1 = doubles[k][0]
                            value2 = doubles[l][0]
                            for value in range(0, 9):
                                board[x1][y1].removePV(value)
                                board[x2][y2].removePV(value)
                            board[x1][y1].addPV(value1)
                            board[x1][y1].addPV(value2)
                            board[x2][y2].addPV(value1)
                            board[x2][y2].addPV(value2)
                            found = True
            numberCount = [(0, []) for value in range(0,9)]
            doubles = []
        return found

    def hiddenDoubleBox(self):
        numberCount = [(0, []) for value in range(0,9)]
        doubles = []
        board = self.board._board
        found = False

        # Find double in box
        for i in range(0,3):
            for j in range(0,3):
                for k in range(0,3):
                    for l in range(0,3):
                        for value in board[i*3 + k][j*3 +l].possibleValues:
                            count, location = numberCount[value - 1]
                            count += 1
                            location.append((i*3 + k, j*3 +l))
                            numberCount[value - 1] = (count, location)
                for value in range(1,10):
                    if numberCount[value - 1][0] is 2:
                        doubles.append((value,numberCount[value-1][1]))
                if len(doubles) > 1:
                    for k in range(0, len(doubles)):
                        for l in range(k + 1, len(doubles)):
                            if (doubles[k][1][0] == doubles[l][1][0] and
                                doubles[k][1][1] == doubles[l][1][1]):
                                x1 = doubles[k][1][0][0]
                                x2 = doubles[k][1][1][0]
                                y1 = doubles[k][1][0][1]
                                y2 = doubles[k][1][1][1]
                                value1 = doubles[k][0]
                                value2 = doubles[l][0]
                                for value in range(0, 9):
                                    board[x1][y1].removePV(value)
                                    board[x2][y2].removePV(value)
                                board[x1][y1].addPV(value1)
                                board[x1][y1].addPV(value2)
                                board[x2][y2].addPV(value1)
                                board[x2][y2].addPV(value2)
                                found = True
                numberCount = [(0, []) for value in range(0,9)]
                doubles = []
        return found
    
def SmartBruteForce(cBoard, board=None):
    if board is None:
        board = cBoard.board

    # Return true if solved.  This will bring the correct board up through the chain of calls.
    if Solve.isSolvedBoard(board):
        return board, True
    # If board is not valid, move up the call chain once.
    if not Solve.isValidBoard(board):
        return board, False

    # Find the first blank space from the top left
    x, y = Solve.findBlank(board)

    # Create a copy of board to be possed down the chain
    newBoard = [[board[i][j] for j in range(0,9)] for i in range(0,9)]

    for value in cBoard._board[x][y].possibleValues:
        
        # Place a value in the empty spot and go to the next spot.
        newBoard[x][y] = value
        resultBoard, result = SmartBruteForce(cBoard, newBoard)

        # If the call below this found a solved board, bring the solved board up to the next call
        if result is True:
            return resultBoard, result
        # If the call below found an invalid board, replace the current spot with the next value

    # If all values were found to be invalid, go up a call and continue with checking the next value for the previous blank spot
    return board, False

def bruteForce(board):

    # Return true if solved.  This will bring the correct board up through the chain of calls.
    if Solve.isSolvedBoard(board):
        return board, True
    # If board is not valid, move up the call chain once.
    if not Solve.isValidBoard(board):
        return board, False

    # Find the first blank space from the top left
    x, y = Solve.findBlank(board)

    # Create a copy of board to be possed down the chain
    newBoard = [[board[i][j] for j in range(0,9)] for i in range(0,9)]

    for value in range(1,10):
        
        # Place a value in the empty spot and go to the next spot.
        newBoard[x][y] = value
        resultBoard, result = bruteForce(newBoard)

        # If the call below this found a solved board, bring the solved board up to the next call
        if result is True:
            return resultBoard, result
        # If the call below found an invalid board, replace the current spot with the next value

    # If all values were found to be invalid, go up a call and continue with checking the next value for the previous blank spot
    return board, False
