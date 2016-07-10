import Sudoku.Solver.Solve as Solve

def smart_brute_force(cell_board, raw_board=None):
    if raw_board is None:
        raw_board = cell_board.raw_board

    # Return true if solved.  This will bring the correct board up through the chain of calls.
    if Solve.is_solved_board(raw_board):
        return raw_board, True
    # If board is not valid, move up the call chain once.
    if not Solve.is_valid_board(raw_board):
        return raw_board, False

    # Find the first blank space from the top left
    x, y = Solve.find_blank(raw_board)

    # Create a copy of board to be possed down the chain
    new_board = [[raw_board[i][j] for j in range(0, 9)] for i in range(0, 9)]

    for value in cell_board.cell_board[x][y].possibleValues:

        # Place a value in the empty spot and go to the next spot.
        new_board[x][y] = value
        result_board, result = smart_brute_force(cell_board, new_board)

        # If the call below this found a solved board, bring the solved board up to the next call
        if result is True:
            return result_board, result
            # If the call below found an invalid board, replace the current spot with the next value

    # If all values were found to be invalid, go up a call and check the next value for the previous blank spot
    return raw_board, False


def brute_force(raw_board):
    # Return true if solved.  This will bring the correct board up through the chain of calls.
    if Solve.is_solved_board(raw_board):
        return raw_board, True
    # If board is not valid, move up the call chain once.
    if not Solve.is_valid_board(raw_board):
        return raw_board, False

    # Find the first blank space from the top left
    x, y = Solve.find_blank(raw_board)

    # Create a copy of board to be possed down the chain
    new_board = [[raw_board[i][j] for j in range(0, 9)] for i in range(0, 9)]

    for value in range(1, 10):

        # Place a value in the empty spot and go to the next spot.
        new_board[x][y] = value
        result_board, result = brute_force(new_board)

        # If the call below this found a solved board, bring the solved board up to the next call
        if result is True:
            return result_board, result
            # If the call below found an invalid board, replace the current spot with the next value

    # If all values were found to be invalid, go up a call and check the next value for the previous blank spot
    return raw_board, False