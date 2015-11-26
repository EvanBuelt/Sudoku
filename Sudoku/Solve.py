def find_blank(board):
    # Checks across the row then down for the first blank spot.
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] is 0:
                # Return the coordinates for the first blank spot
                return i, j

    # If no blank spot found, return (-1, -1)
    return -1, -1


def is_solved_board(board):
    # Check if the board is valid first. If not, then the board cannot be solved.
    if not is_valid_board(board):
        return False

    # Create list of numbers from 1 to 9.
    nums = [i + 1 for i in range(0, 9)]
    for i in range(0, 9):
        for j in range(0, 9):

            # If any part of the board is blank, then the board is not solved
            if board[i][j] not in nums:
                return False
    return True


def is_valid_board(board):
    # Returns true if every row, column, and 3x3 box contains no duplicates
    is_valid = check_rows(board) and check_columns(board) and check_boxes(board)
    return is_valid


def check_rows(board):
    # Check each of the rows
    for i in range(0, 9):

        # Create a list of values from 1 to 9 to be checked later and removed
        nums = [x + 1 for x in range(0, 9)]
        for j in range(0, 9):
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


def check_columns(board):
    # Check each of the columns
    for i in range(0, 9):

        # Create a list of values from 1 to 9 to be checked later and removed
        nums = [x + 1 for x in range(0, 9)]
        for j in range(0, 9):
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


def check_boxes(board):
    # Check each of the 9 3x3 boxes
    for i in range(0, 3):
        for j in range(0, 3):

            # Create a list of values from 1 to 9 to be checked later and removed
            nums = [x + 1 for x in range(0, 9)]

            # Check each of the 9 values in the box
            for k in range(0, 3):
                for l in range(0, 3):

                    # i and j represent the box indexes, so 3*i and 3*j represent the value index
                    value = board[3 * i + k][3 * j + l]

                    # A value of 0 is used to show a blank square.  If it is 0, do nothing
                    if value is not 0:

                        # If the current value is in the list, then it has not been found.  Remove from the list of nums
                        # Otherwise, it has been previously found in the row, and so the board is 
                        if value in nums:
                            nums.remove(value)
                        else:
                            return False
    return True
