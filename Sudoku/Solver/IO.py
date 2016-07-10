def load_board(file_path):
    # Load 9x9 Sudoku Board
    sudoku_file = open(file_path, 'r')

    board = []
    raw_data = sudoku_file.read()
    data = raw_data.splitlines()

    # Add each row from the file to the board
    for row in data:
        board.append(row.split(' '))

    # Convert each item from a string to an integer
    for i in range(0, 9):
        for j in range(0, 9):
            board[i][j] = int(board[i][j])

    # return 9x9 board
    return board


def print_board(board):
    output = ""
    for i in range(0, 9):
        for j in range(0, 9):

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
