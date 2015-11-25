import datetime

def loadBoard(filePath):

    # Load 9x9 Sudoku Board
    SudokuFile = open(filePath, 'r')

    board = []
    rawData = SudokuFile.read()
    data = rawData.splitlines()

    # Add each row from the file to the board
    for row in data:
        board.append(row.split(' '))

    # Convert each item from a string to an integer
    for i in range(0,9):
        for j in range(0,9):
            board[i][j] = int(board[i][j])

    # return 9x9 board
    return board

def bruteForce(board):

    # Return true if solved.  This will bring the correct board up through the chain of calls.
    if isSolvedBoard(board):
        return board, True
    # If board is not valid, move up the call chain once.
    if not isValidBoard(board):
        return board, False

    # Find the first blank space from the top left
    x, y = findBlank(board)

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

def findBlank(board):
    
    # Checks across the row then down for the first blank spot.  
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] is 0:
                
                # Return the coordinates for the first blank spot
                return i,j
            
    # If no blank spot found, return (-1, -1)
    return -1,-1

def isValidBoard(board):
    
    # Returns true if every row, column, and 3x3 box contains no duplicates
    isValid = checkRows(board) and checkColumns(board) and checkBoxes(board)
    return isValid

def isSolvedBoard(board):
    
    # Check if the board is valid first. If not, then the board cannot be solved.
    if not isValidBoard(board):
        return False

    # Create list of numbers from 1 to 9.
    nums = [i+1 for i in range(0,9)]
    for i in range(0,9):
        for j in range(0,9):
            
            # If any part of the board is blank, then the board is not solved
            if board[i][j] not in nums:
                return False
    return True

def checkRows(board):
    for i in range(0,9):
        
        # Create a list of values from 1 to 9 to be checked later and removed
        nums = [x+1 for x in range(0,9)]
        for j in range(0,9):
            value = board[i][j]
            
            # A value of 0 is used to show a blank square.  If it is 0, do nothing
            if value is not 0:
                
                # If the current value is in the list, then it has not been found.  Remove from the list of nums
                # Otherwise, it has been previously found in the row, and so the board is 
                if value in nums:
                    nums.remove(value)
                else:
                    return False
    return True

def checkColumns(board):
    for i in range(0,9):
        
        # Create a list of values from 1 to 9 to be checked later and removed
        nums = [x+1 for x in range(0,9)]
        for j in range(0,9):
            value = board[j][i]
            
            # A value of 0 is used to show a blank square.  If it is 0, do nothing
            if value is not 0:
                
                # If the current value is in the list, then it has not been found.  Remove from the list of nums
                # Otherwise, it has been previously found in the row, and so the board is 
                if value in nums:
                    nums.remove(value)
                else:
                    return False
    return True

def checkBoxes(board):
    
    # Check each of the 9 3x3 boxes
    for i in range(0,3):
        for j in range(0,3):
            
            # Create a list of values from 1 to 9 to be checked later and removed
            nums = [x+1 for x in range(0,9)]

            # Check each of the 9 values in the box
            for k in range(0,3):
                for l in range(0,3):
                    
                    # i and j represent the box indexes, so 3*i and 3*j represent the value index
                    value = board[3*i + k][3*j + l]

                    # A value of 0 is used to show a blank square.  If it is 0, do nothing
                    if value is not 0:

                        # If the current value is in the list, then it has not been found.  Remove from the list of nums
                        # Otherwise, it has been previously found in the row, and so the board is 
                        if value in nums:
                            nums.remove(value)
                        else:
                            return False
    return True
                    
def printBoard(board):
    output = ""
    for i in range(0,9):
        for j in range(0,9):

            # If value is 0, then add a blank.
            if board[i][j] is 0:
                output += " "

            # Otherwise, display value
            else:
                output += str(board[i][j])

            # Add a new line if at end of row
            if (j + 1) is 9:
                output += "\n"

            # Add a barrier for the 3x3 box at every 3rd column
            elif (j + 1) % 3 is 0:
                output += "|"

            # Add a blank between numbers on screen
            else:
                output += " "
                
        # Add a barrier for every 3rd row
        if (i + 1) % 3 is 0 and i is not 8:
            output += "-----+-----+-----\n"

    # Print output onto screen
    print output
    return output
    
def solveBoard(filePath):

    # Load in board, and time how long it takes to solve.
    board = loadBoard(filePath)
    startTime = datetime.datetime.now()
    solvedBoard, result = bruteForce(board)
    endTime = datetime.datetime.now()

    # Calculate the difference between the start and end time
    diffTime = endTime - startTime

    # Get the time in seconds
    time = float(diffTime.seconds) + float(diffTime.microseconds)/float(1000000)

    # Display information to the user.
    print time
    print "\nOriginal Board\n"
    printBoard(board)
    print "\nSolved Board\n"
    printBoard(solvedBoard)

    return solvedBoard, result


