import IO
import Solve


# 1 Singles in box
# 1 Hidden Singles in row/column/box
# 0 Values locked to row/column in box
# 1 Pairs in row/column/box
# 0 Triples in row/column/box
# 0 Quads in row/column/box
# 1 Hidden Pairs in row/column/box
# 0 Hidden Triples in row/column/box (rare)
# 0 Hidden Quads in a row/column/box (rare)
# 0 X-Wing
# 0 Swordfish

class Cell:
    def __init__(self, value=None):
        # Initialize possible values from 1 to 9
        self.possibleValues = [i for i in range(1, 10)]
        self.value = 0

        # Initialize value.
        if value is None:
            self.set_value(0)
        else:
            self.set_value(value)

    def set_value(self, value):
        self.value = value
        if value is not 0:
            self.possibleValues = []
        return

    def remove_possible_value(self, value):
        if value in self.possibleValues:
            self.possibleValues.remove(value)
            return True
        return False

    def add_possible_value(self, value):
        if value not in self.possibleValues:
            self.possibleValues.append(value)
            self.possibleValues.sort()
        return


class Board:
    def __init__(self, file_path):
        self.raw_board = IO.load_board(file_path)
        self.cell_board = []
        for i in range(0, 9):
            row = []
            for j in range(0, 9):
                row.append(Cell(self.raw_board[i][j]))
            self.cell_board.append(row)

        for i in range(0, 9):
            for j in range(0, 9):
                self.remove_possible_value(i, j)

    def set_value(self, value, row, column):
        self.raw_board[row][column] = value
        self.cell_board[row][column].set_value(value)
        self.remove_possible_value(row, column)

    def remove_possible_value(self, row, column):
        self.remove_pv_row(row, column)
        self.remove_pv_column(row, column)
        self.remove_pv_box(row, column)

    def remove_possible_value_optimized(self, row, column):
        x = 3 * (row / 3)
        y = 3 * (column / 3)
        value = self.cell_board[row][column].value

        for i in range(0, 9):
            self.cell_board[row][i].remove_possible_value(value)
            self.cell_board[i][column].remove_possible_value(value)
            self.cell_board[x + (i / 3)][y + (i % 3)].remove_possible_value(value)

    def remove_pv_row(self, row, column):
        value = self.cell_board[row][column].value
        for j in range(0, 9):
            self.cell_board[row][j].remove_possible_value(value)
        return

    def remove_pv_column(self, row, column):
        value = self.cell_board[row][column].value
        for i in range(0, 9):
            self.cell_board[i][column].remove_possible_value(value)
        return

    def remove_pv_box(self, row, column):
        x = 3 * (row / 3)
        y = 3 * (column / 3)

        value = self.cell_board[row][column].value

        for i in range(x, x + 3):
            for j in range(y, y + 3):
                self.cell_board[i][j].remove_possible_value(value)
        return


class ElegantSolver:
    def __init__(self, file_path):
        # Load in board, and time how long it takes to solve.
        self.board = Board(file_path)

    def set_value(self, value, i, j):
        self.board.set_value(value, i, j)

    def solve(self):
        running = True
        while running:
            # Run techniques to remove any possible values from cells
            result3 = self.double()
            result4 = self.hidden_double()
            result5 = self.triple()
            result6 = self.hidden_triple()
            result7 = self.quad()
            result8 = self.hidden_quad()
            result9 = self.x_wing()
            result0 = self.swordfish()

            # Set values in cells that have only one possible value
            result1 = self.single()
            result2 = self.hidden_single()

            # print result1, result2, result3, result4
            running = result1 or result2 or result4

        IO.print_board(self.board.raw_board)
        solved_board, result = smart_brute_force(self.board)
        IO.print_board(solved_board)
        return solved_board, result

    def single(self):
        board = self.board.cell_board
        found = False
        for i in range(0, 9):
            for j in range(0, 9):
                if len(board[i][j].possibleValues) is 1:
                    found = True
                    self.set_value(board[i][j].possibleValues[0], i, j)

        return found

    def hidden_single(self):
        found1 = self.hidden_single_row()
        found2 = self.hidden_single_column()
        found3 = self.hidden_single_box()
        found = found1 or found2 or found3
        return found

    def double(self):
        found1 = self.double_row()
        found2 = self.double_column()
        found3 = self.double_box()
        found = found1 or found2 or found3
        return found

    def hidden_double(self):
        found1 = self.hidden_double_row()
        found2 = self.hidden_double_column()
        found3 = self.hidden_double_box()
        found = found1 or found2 or found3
        return found

    def pointing_double(self):
        board = self.board.raw_board
        return False

    def triple(self):
        board = self.board.raw_board
        return False

    def hidden_triple(self):
        board = self.board.raw_board
        return False

    def pointing_triple(self):
        board = self.board.raw_board
        return False

    def quad(self):
        board = self.board.raw_board
        return False

    def hidden_quad(self):
        board = self.board.raw_board
        return False

    def x_wing(self):
        board = self.board.raw_board
        return False

    def swordfish(self):
        board = self.board.raw_board
        return False

    def hidden_single_row(self):
        number_count = [(0, []) for value in range(0, 9)]
        board = self.board.cell_board
        found = False

        # Find single in row
        for i in range(0, 9):
            for j in range(0, 9):
                for value in board[i][j].possibleValues:
                    count, location = number_count[value - 1]
                    count += 1
                    location.append((i, j))
                    number_count[value - 1] = (count, location)
            found = self.hidden_single_remove(number_count)
            number_count = [(0, []) for value in range(0, 9)]
        return found

    def hidden_single_column(self):
        number_count = [(0, []) for value in range(0, 9)]
        board = self.board.cell_board
        found = False

        # Find single in column
        for j in range(0, 9):
            for i in range(0, 9):
                for value in board[i][j].possibleValues:
                    count, location = number_count[value - 1]
                    count += 1
                    location.append((i, j))
                    number_count[value - 1] = (count, location)
            found = self.hidden_single_remove(number_count)
            number_count = [(0, []) for value in range(0, 9)]
        return found

    def hidden_single_box(self):
        number_count = [(0, []) for value in range(0, 9)]
        board = self.board.cell_board
        found = False

        # Find single in box
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        for value in board[i * 3 + k][j * 3 + l].possibleValues:
                            count, location = number_count[value - 1]
                            count += 1
                            location.append((i * 3 + k, j * 3 + l))
                            number_count[value - 1] = (count, location)
                found = self.hidden_single_remove(number_count)
                number_count = [(0, []) for value in range(0, 9)]
        return found

    def double_row(self):
        board = self.board.cell_board
        doubles = []
        removed = False

        # Find double in row
        for i in range(0, 9):
            for j in range(0, 9):
                # Append any cell with only 2 possible values
                if len(board[i][j].possibleValues) is 2:
                    doubles.append(board[i][j])
            if len(doubles) > 1:
                for k in range(0, len(doubles)):
                    if len(doubles[k].possibleValues) < 2:
                        break
                    pv_k1 = doubles[k].possibleValues[0]
                    pv_k2 = doubles[k].possibleValues[1]
                    for l in range(k + 1, len(doubles)):
                        if len(doubles[l].possibleValues) < 2:
                            break
                        pv_l1 = doubles[l].possibleValues[0]
                        pv_l2 = doubles[l].possibleValues[1]
                        if (pv_k1 == pv_l1) and (pv_k2 == pv_l2):
                            value1 = pv_k1
                            value2 = pv_k2
                            for column in range(0, 9):
                                result1 = board[i][column].remove_possible_value(value1)
                                result2 = board[i][column].remove_possible_value(value2)
                                removed = removed or result1 or result2
                            doubles[k].add_possible_value(value1)
                            doubles[k].add_possible_value(value2)
                            doubles[l].add_possible_value(value1)
                            doubles[l].add_possible_value(value2)
            doubles = []
        return removed

    def double_column(self):
        board = self.board.cell_board
        doubles = []
        removed = False
        # Find double in column
        for j in range(0, 9):
            for i in range(0, 9):
                # Append any cell with only 2 possible values
                if len(board[i][j].possibleValues) is 2:
                    doubles.append(board[i][j])

                for k in range(0, len(doubles)):
                    if len(doubles[k].possibleValues) < 2:
                        break
                    pv_k1 = doubles[k].possibleValues[0]
                    pv_k2 = doubles[k].possibleValues[1]
                    for l in range(k + 1, len(doubles)):
                        if len(doubles[l].possibleValues) < 2:
                            break
                        pv_l1 = doubles[l].possibleValues[0]
                        pv_l2 = doubles[l].possibleValues[1]
                        if (pv_k1 == pv_l1) and (pv_k2 == pv_l2):
                            value1 = pv_k1
                            value2 = pv_k2
                            for row in range(0, 9):
                                result1 = board[row][j].remove_possible_value(value1)
                                result2 = board[row][j].remove_possible_value(value2)
                                removed = removed or result1 or result2
                            doubles[k].add_possible_value(value1)
                            doubles[k].add_possible_value(value2)
                            doubles[l].add_possible_value(value1)
                            doubles[l].add_possible_value(value2)
            doubles = []
        return removed

    def double_box(self):
        board = self.board.cell_board
        doubles = []
        removed = False

        # Find double in 3x3 box
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        if len(board[i * 3 + k][j * 3 + l].possibleValues) is 2:
                            doubles.append(board[i * 3 + k][j * 3 + l])
                if len(doubles) > 1:
                    for k in range(0, len(doubles)):
                        if len(doubles[k].possibleValues) < 2:
                            break
                        pv_k1 = doubles[k].possibleValues[0]
                        pv_k2 = doubles[k].possibleValues[1]
                        for l in range(k + 1, len(doubles)):
                            if len(doubles[l].possibleValues) < 2:
                                break
                            pv_l1 = doubles[l].possibleValues[0]
                            pv_l2 = doubles[l].possibleValues[1]
                            if (pv_k1 == pv_l1) and (pv_k2 == pv_l2):
                                value1 = pv_k1
                                value2 = pv_k2
                                for row in range(0, 3):
                                    for column in range(0, 3):
                                        result1 = board[i * 3 + row][j * 3 + column].remove_possible_value(value1)
                                        result2 = board[i * 3 + row][j * 3 + column].remove_possible_value(value2)
                                        removed = removed or result1 or result2
                                doubles[k].add_possible_value(value1)
                                doubles[k].add_possible_value(value2)
                                doubles[l].add_possible_value(value1)
                                doubles[l].add_possible_value(value2)
                doubles = []
        return removed

    def hidden_double_row(self):
        number_count = [(0, []) for value in range(0, 9)]
        doubles = []
        board = self.board.cell_board
        removed = False

        # Find double in row
        for i in range(0, 9):
            for j in range(0, 9):
                for value in board[i][j].possibleValues:
                    count, location_list = number_count[value - 1]
                    count += 1
                    location_list.append((i, j))
                    number_count[value - 1] = (count, location_list)
            for value in range(1, 10):
                count, location_list = number_count[value - 1]
                if count is 2:
                    doubles.append((value, location_list))
            removed = self.hidden_double_remove(doubles)
            number_count = [(0, []) for value in range(0, 9)]
            doubles = []
        return removed

    def hidden_double_column(self):
        number_count = [(0, []) for value in range(0, 9)]
        doubles = []
        board = self.board.cell_board
        removed = False

        # Find double in column
        for j in range(0, 9):
            for i in range(0, 9):
                for value in board[i][j].possibleValues:
                    count, location = number_count[value - 1]
                    count += 1
                    location.append((i, j))
                    number_count[value - 1] = (count, location)
            for value in range(1, 10):
                if number_count[value - 1][0] is 2:
                    doubles.append((value, number_count[value - 1][1]))
            removed = self.hidden_double_remove(doubles)
            number_count = [(0, []) for value in range(0, 9)]
            doubles = []
        return removed

    def hidden_double_box(self):
        number_count = [(0, []) for value in range(0, 9)]
        doubles = []
        board = self.board.cell_board
        removed = False

        # Find double in box
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        for value in board[i * 3 + k][j * 3 + l].possibleValues:
                            count, location = number_count[value - 1]
                            count += 1
                            location.append((i * 3 + k, j * 3 + l))
                            number_count[value - 1] = (count, location)
                for value in range(1, 10):
                    if number_count[value - 1][0] is 2:
                        doubles.append((value, number_count[value - 1][1]))
                removed = self.hidden_double_remove(doubles)
                number_count = [(0, []) for value in range(0, 9)]
                doubles = []
        return removed

    def pointing_double_row(self):
        number_count = [(0, []) for value in range(0, 9)]
        doubles = []
        board = self.board.cell_board
        removed = False

        # Iterate over each box
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        for value in board[i * 3 + k][j * 3 + l].possibleValues:
                            count, location = number_count[value - 1]
                            count += 1
                            location.append((i * 3 + k, j * 3 + l))
                            number_count[value - 1] = (count, location)
                for value in range(1, 10):
                    if number_count[value - 1][0] is 2:
                        doubles.append((value, number_count[value - 1][1]))
                for data in doubles:
                    count, location_list = data
                    for k in range(0, len(location_list)):
                        location_k = location_list[k]
                        for l in range(k + 1, len(location_list)):
                            location_l = location_list[l]
                            if location_k[1] == location_l[1]:
                                for m in range(0, j):
                                    return removed
        return removed

    def pointing_double_column(self):
        number_count = [(0, []) for value in range(0, 9)]
        doubles = []
        board = self.board.cell_board
        removed = False

        # Iterate over each box
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    for l in range(0, 3):
                        removed = False
        return removed

    def hidden_single_remove(self, number_count):
        found = False
        for value in range(1, 10):
                count, location = number_count[value - 1]
                if count is 1:
                    (x, y) = location[0]
                    self.set_value(value, x, y)
                    found = True

        return found

    def hidden_double_remove(self, doubles):
        board = self.board.cell_board
        removed = False

        if len(doubles) > 1:
            for k in range(0, len(doubles)):
                value1, location_list_k = doubles[k]
                location_k1 = location_list_k[0]
                location_k2 = location_list_k[1]
                for l in range(k + 1, len(doubles)):
                    value2, location_list_l = doubles[l]
                    location_l1 = location_list_l[0]
                    location_l2 = location_list_l[1]
                    if (location_k1 == location_l1) and (location_k2 == location_l2):
                        x1 = location_k1[0]
                        x2 = location_k1[0]
                        y1 = location_k1[1]
                        y2 = location_k1[1]
                        for value in range(1, value1):
                            result1 = board[x1][y1].remove_possible_value(value)
                            result2 = board[x2][y2].remove_possible_value(value)
                            removed = removed or result1 or result2
                        for value in range(value1 + 1, value2):
                            result1 = board[x1][y1].remove_possible_value(value)
                            result2 = board[x2][y2].remove_possible_value(value)
                            removed = removed or result1 or result2
                        for value in range(value2 + 1, 10):
                            result1 = board[x1][y1].remove_possible_value(value)
                            result2 = board[x2][y2].remove_possible_value(value)
                            removed = removed or result1 or result2
        return removed


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
