import datetime

def loadBoard(filePath):
    
    board = []
    SudokuFile = open(filePath, 'r')
    
    rawData = SudokuFile.read()
    data = rawData.splitlines()
    for row in data:
        board.append(row.split(' '))

    for i in range(0,9):
        for j in range(0,9):
            board[i][j] = int(board[i][j])
    
    return board

def bruteForce(board):
    if isSolvedBoard(board):
        return board, True
    if not isValidBoard(board):
        return board, False
    
    x, y = findBlank(board)
    
    newBoard = [[board[i][j] for j in range(0,9)] for i in range(0,9)]
    for value in range(1,10):
        newBoard[x][y] = value
        resultBoard, result = bruteForce(newBoard)
        if result is True:
            return resultBoard, result
    return board, False

def findBlank(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] is 0:
                return i,j
    return -1,-1

def isValidBoard(board):
    isValid = checkRows(board) and checkColumns(board) and checkBoxes(board)
    return isValid

def isSolvedBoard(board):
    if not isValidBoard(board):
        return False

    nums = [i+1 for i in range(0,9)]
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] not in nums:
                return False
    return True

def checkRows(board):
    for i in range(0,9):
        nums = [x+1 for x in range(0,9)]
        for j in range(0,9):
            value = board[i][j]
            if value is not 0:
                if value in nums:
                    nums.remove(value)
                else:
                    return False
    return True

def checkColumns(board):
    for i in range(0,9):
        nums = [x+1 for x in range(0,9)]
        for j in range(0,9):
            value = board[j][i]
            if value is not 0:
                if value in nums:
                    nums.remove(value)
                else:
                    return False
    return True

def checkBoxes(board):
    for i in range(0,3):
        for j in range(0,3):
            nums = [x+1 for x in range(0,9)]
            for k in range(0,3):
                for l in range(0,3):
                    value = board[3*i + k][3*j + l]
                    if value is not 0:
                        if value in nums:
                            nums.remove(value)
                        else:
                            return False
    return True
                    
def printBoard(board):
    output = ""
    for i in range(0,9):
        for j in range(0,9):
            output += str(board[i][j])
            if (j + 1) is 9:
                output += "\n"
            elif (j + 1) % 3 is 0:
                output += "|"
            else:
                output += " "
        if (i + 1) % 3 is 0 and i is not 8:
            output += "-----+-----+-----\n"
    print output
    
def solveBoard(filePath):

    board = loadBoard(filePath)
    startTime = datetime.datetime.now()
    solvedBoard, result = bruteForce(board)
    endTime = datetime.datetime.now()
    diffTime = endTime - startTime

    time = float(diffTime.seconds) + float(diffTime.microseconds)/float(1000000)
    print time
    print "\nOriginal Board\n"
    printBoard(board)
    print "\nSolved Board\n"
    printBoard(solvedBoard)


