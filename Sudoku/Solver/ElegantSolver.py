import Engine
import BruteForce
import IO


class ElegantSolver:
    def __init__(self, file_path):
        # Load in board, and time how long it takes to solve.
        self.board = Engine.Board(file_path)

    def set_value(self, value, i, j):
        self.board.set_value(value, i, j)

    def solve(self):
        running = True
        while running:
            # Run techniques to remove any possible values from cells
            result1 = self.double()
            result2 = self.hidden_double()
            result3 = self.pointing_double()
            result4 = self.triple()
            result5 = self.hidden_triple()
            result6 = self.quad()
            result7 = self.hidden_quad()
            result8 = self.x_wing()
            result9 = self.swordfish()

            # Process finding singles last as previous steps will have removed more possible values
            result10 = self.single()
            result11 = self.hidden_single()

            # Hidden doubles/triples/quads will only return true if they have removed anything.
            # Single and Hidden single will also only return true if a single was found.
            running = result1 or result2 or result3 or result4 or result5 or result6 or result7 or result8 or result9 \
                or result10 or result11

        IO.print_board(self.board.raw_board)
        solved_board, result = BruteForce.smart_brute_force(self.board)
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

        # If singles were found, return true.  Otherwise, return false
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
        found1 = self.pointing_double_row()
        found2 = self.pointing_double_column()
        found3 = self.pointing_double_box()
        found = found1 or found2 or found3
        # return found
        # board = self.board.raw_board
        # return False

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
        removed = False
        board = self.board.cell_board

        # Find single in row
        for row in range(0, 9):
            number_count = get_number_count(board, row, row + 1, 0, 9)
            result = hidden_single_remove(self, number_count)
            removed = removed or result

        # If singles were found, return true.  Otherwise, return false
        return removed

    def hidden_single_column(self):
        removed = False
        board = self.board.cell_board

        # Find single in column
        for column in range(0, 9):
            number_count = get_number_count(board, 0, 9, column, column + 1)
            result = hidden_single_remove(self, number_count)
            removed = removed or result

        # If singles were found, return true.  Otherwise, return false
        return removed

    def hidden_single_box(self):
        removed = False
        board = self.board.cell_board

        # Find single in box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                number_count = get_number_count(board, box_row * 3, (box_row + 1) * 3, box_col * 3, (box_col + 1) * 3)
                result = hidden_single_remove(self, number_count)
                removed = removed or result

        # If singles were found, return true.  Otherwise, return false
        return removed

    def double_row(self):
        removed = False
        board = self.board.cell_board

        for row in range(0, 9):
            doubles = find_doubles(board, row, row + 1, 0, 9)
            result = process_doubles(board, doubles, row, row + 1, 0, 9)
            removed = removed or result

        # If any possible values were removed, return true.  Otherwise, return false
        return removed

    def double_column(self):
        removed = False
        board = self.board.cell_board

        for column in range(0, 9):
            doubles = find_doubles(board, 0, 9, column, column + 1)
            result = process_doubles(board, doubles, 0, 9, column, column + 1)
            removed = removed or result

        # If any possible values were removed, return true.  Otherwise, return false
        return removed

    def double_box(self):
        removed = False
        board = self.board.cell_board

        # Find double in 3x3 box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                doubles = find_doubles(board, box_row * 3, (box_row + 1) * 3, box_col * 3, (box_col + 1) * 3)
                result = process_doubles(board, doubles, box_row * 3, (box_row + 1) * 3, box_col * 3, (box_col + 1) * 3)
                removed = removed or result

        # If any possible values were removed, return true.  Otherwise, return false
        return removed

    def hidden_double_row(self):
        removed = False
        board = self.board.cell_board

        # Find double in row
        for row in range(0, 9):
            number_count = get_number_count(board, row, row + 1, 0, 9)
            doubles = process_number_count(number_count, 2, 2)
            result = hidden_double_remove(board, doubles)
            removed = removed or result

        return removed

    def hidden_double_column(self):
        removed = False
        board = self.board.cell_board

        # Find double in column
        for column in range(0, 9):
            number_count = get_number_count(board, 0, 9, column, column + 1)
            doubles = process_number_count(number_count, 2, 2)
            result = hidden_double_remove(board, doubles)
            removed = removed or result

        return removed

    def hidden_double_box(self):
        removed = False
        board = self.board.cell_board

        # Find double in box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                number_count = get_number_count(board, box_row * 3, (box_row + 1) * 3, box_col * 3, (box_col + 1) * 3)
                doubles = process_number_count(number_count, 2, 2)
                result = hidden_double_remove(board, doubles)
                removed = removed or result

        return removed

    def hidden_triple_row(self):
        removed = False
        board = self.board.cell_board

        # Find double in row
        for row in range(0, 9):
            number_count = get_number_count(board, row, row + 1, 0, 9)
            triples = process_number_count(number_count, 2, 3)
            result = hidden_triple_remove(board, triples)
            removed = removed or result

        return removed

    def hidden_triple_column(self):
        removed = False
        board = self.board.cell_board

        # Find double in column
        for column in range(0, 9):
            number_count = get_number_count(board, 0, 9, column, column + 1)
            triples = process_number_count(number_count, 2, 3)
            result = hidden_triple_remove(board, triples)
            removed = removed or result

        return removed

    def hidden_triple_box(self):
        removed = False
        board = self.board.cell_board

        # Find double in box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                number_count = get_number_count(board, box_row * 3, (box_row + 1) * 3, box_col * 3, (box_col + 1) * 3)
                triples = process_number_count(number_count, 2, 3)
                result = hidden_triple_remove(board, triples)
                removed = removed or result

        return removed

    def pointing_double_row(self):
        # If a pair of empty cells within a box in the same row/column share a candidate, the candidate can be removed
        # from all other cells in the row/column
        removed = False
        board = self.board.cell_board

        # Iterate over each box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                # Get all the doubles in the box
                number_count = get_number_count(board, box_row * 3, (box_row + 1) * 3, box_col * 3, (box_col + 1) * 3)
                doubles = process_number_count(number_count, 2, 2)
                for row in range(0, 3):
                    # Syntactic sugar
                    row_start = box_row * 3 + row
                    row_end = row_start + 1

                    # print "Row", row_start
                    result = pointing_double_remove(board, doubles, row_start, row_end, 0, 9)
                    removed = removed or result

        return removed

    def pointing_double_column(self):
        # If a pair of empty cells within a box in the same row/column share a candidate, the candidate can be removed
        # from all other cells in the row/column
        removed = False
        board = self.board.cell_board

        # Iterate over each box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                # Get all the doubles in the box
                number_count = get_number_count(board, box_row * 3, (box_row + 1) * 3, box_col * 3, (box_col + 1) * 3)
                doubles = process_number_count(number_count, 2, 2)
                for col in range(0, 3):
                    # Syntactic sugar
                    col_start = box_col * 3 + col
                    col_end = col_start + 1

                    # Process the found doubles from the box, but process the entire column
                    result = pointing_double_remove(board, doubles, 0, 9, col_start, col_end)
                    removed = removed or result

        return removed

    def pointing_double_box(self):
        # If a pair of empty cells within a box in the same row/column share a candidate, the candidate can be removed
        # from all other cells in the box if the candidate is not found in any other cells in the row/column
        removed = False
        board = self.board.cell_board

        # Iterate over each box
        for box_row in range(0, 3):
            for box_col in range(0, 3):
                for row in range(0, 3):
                    # Syntactic sugar
                    row_start = box_row * 3 + row
                    row_end = row_start + 1

                    # Get all the doubles in the row
                    number_count = get_number_count(board, row_start, row_end, 0, 9)
                    doubles = process_number_count(number_count, 2, 2)

                    result = pointing_double_remove(board, doubles, row_start, row_end, box_col * 3, (box_col + 1) * 3)
                    removed = removed or result

                for col in range(0, 3):
                    # Syntactic sugar
                    col_start = box_col * 3 + col
                    col_end = col_start + 1

                    # Get all the doubles in the row
                    number_count = get_number_count(board, 0, 9, col_start, col_end)
                    doubles = process_number_count(number_count, 2, 2)

                    result = pointing_double_remove(board, doubles, box_row * 3, (box_row + 1) * 3, col_start, col_end)
                    removed = removed or result

        return removed


# Functions used for single/hidden single
def hidden_single_remove(solver, number_count):
        found = False
        for value in range(1, 10):
                count, location = number_count[value - 1]
                if count is 1:
                    (x, y) = location[0]
                    solver.set_value(value, x, y)
                    found = True

        return found


# Functions used for doubles/hidden doubles/pointing pairs
def find_doubles(board, row_min, row_max, column_min, column_max):
    # List of cells that have only two possible values
    doubles = []

    # Find any cell with only two possible numbers
    for row in range(row_min, row_max):
        for column in range(column_min, column_max):
            if len(board[row][column].possibleValues) is 2:
                doubles.append((board[row][column], (row, column)))

    # Return array of found doubles
    return doubles


def process_doubles(board, doubles, row_min, row_max, column_min, column_max):
    # Represents if any possible values were removed.
    removed = False

    # To remove possible values, there needs to be a pair of doubles, not just a single cell with only two values
    if len(doubles) > 1:
        for i in range(0, len(doubles)):
            # Get cell and location information out of the list
            cell_i, location_i = doubles[i]

            # As values may be removed during a loop, only do something if there are at least 2 possible values
            if len(cell_i.possibleValues) < 2:
                break

            # Syntactic sugar to bring out possible values for cell i
            possible_value_i_1 = cell_i.possibleValues[0]
            possible_value_i_2 = cell_i.possibleValues[1]

            for j in range(i + 1, len(doubles)):
                # Get cell and location information out of the list
                cell_j, location_j = doubles[i]

                # As values may be removed during a loop, only do something if there are at least 2 possible values
                if len(cell_j.possibleValues) < 2:
                    break

                # Syntactic sugar to bring out possible values for cell j
                possible_value_j_1 = cell_j.possibleValues[0]
                possible_value_j_2 = cell_j.possibleValues[1]

                # If the two possible values for two cells match, remove the possible values for all other cells
                if (possible_value_i_1 == possible_value_j_1) and (possible_value_i_2 == possible_value_j_2):
                    value1 = possible_value_i_1
                    value2 = possible_value_i_2
                    for row in range(row_min, row_max):
                        for column in range(column_min, column_max):
                            result1 = remove_values_not_in_list(board, [value1, value2], location_i)
                            result2 = remove_values_not_in_list(board, [value1, value2], location_j)
                            removed = removed or result1 or result2

    # If any possible values were removed, return true.  Otherwise, return false
    return removed


def hidden_double_remove(board, doubles):
    removed = False

    if len(doubles) > 1:
        for i in range(0, len(doubles)):
            # Get the first value and its locations
            value1, location_list_i = doubles[i]

            for j in range(i + 1, len(doubles)):
                # Get the second value and its locations
                value2, location_list_j = doubles[j]

                # Get all locations of both values
                locations_list = location_list_i + location_list_j

                # Get the unique locations
                common = unique_locations(locations_list)

                # If there are exactly two unique locations, remove possible values that are not the two values
                if len(common) is 2:
                    result1 = remove_values_not_in_list(board, [value1, value2], common[0])
                    result2 = remove_values_not_in_list(board, [value1, value2], common[1])
                    removed = removed or result1 or result2
    return removed


def pointing_double_remove(board, doubles, row_min, row_max, column_min, column_max):
    removed = False

    if len(doubles) > 0:
        for i in range(0, len(doubles)):
            # Get the first value and its locations
            value, location_list = doubles[i]

            if len(location_list) is 2:

                # Get locations in the specified area
                common = return_locations_inside_area(location_list, row_min, row_max, column_min, column_max)

                # print "Common", common, len(common), "value", value

                # If there are exactly two unique locations, remove possible values that are not the two values
                if len(common) is 2:
                    remove_location_list = return_non_locations_inside_area(common, row_min, row_max, column_min, column_max)
                    for location in remove_location_list:
                        result1 = remove_values_in_list(board, [value], location)
                        removed = removed or result1
    return removed


# Functions used for triples/hidden triples/pointing triples
def hidden_triple_remove(board, triples):
    removed = False

    if len(triples) > 2:
        for i in range(0, len(triples)):
            # Get the first value and its locations
            value1, location_list_i = triples[i]

            for j in range(i + 1, len(triples)):
                # Get the second value and its locations
                value2, location_list_j = triples[j]

                for k in range(j + 1, len(triples)):
                    # Get the second value and its locations
                    value3, location_list_k = triples[k]

                    # Get all locations of both values
                    locations_list = location_list_i + location_list_j + location_list_k

                    # Get the unique locations
                    common = unique_locations(locations_list)
                    if len(common) is 3:
                        result1 = remove_values_not_in_list(board, [value1, value2, value3], common[0])
                        result2 = remove_values_not_in_list(board, [value1, value2, value3], common[1])
                        result3 = remove_values_not_in_list(board, [value1, value2, value3], common[2])
                        removed = removed or result1 or result2 or result3
    return removed


# General functions for solving a sudoku board
def remove_values_not_in_list(board, value_list, location):
    x, y = location
    removal_list = []
    result = False

    for possible_value in board[x][y].possibleValues:
        if possible_value not in value_list:
            removal_list.append(possible_value)

    for value in removal_list:
        removal_result = board[x][y].remove_possible_value(value)
        result = result and removal_result

    return result


def remove_values_in_list(board, value_list, location):
    x, y = location
    removal_list = []
    result = False

    for possible_value in board[x][y].possibleValues:
        if possible_value in value_list:
            removal_list.append(possible_value)

    for value in removal_list:
        removal_result = board[x][y].remove_possible_value(value)
        result = result and removal_result

    return result


def unique_locations(locations_list):
    common = []

    for location in locations_list:
        if location not in common:
            common.append(location)

    return common


def return_non_locations_inside_area(location_list, row_min, row_max, column_min, column_max):
    return_list = []
    for row in range(row_min, row_max):
        for column in range(column_min, column_max):
            return_list.append((row, column))

    for location in location_list:
        if location in return_list:
            return_list.remove(location)

    # print "Not Box", return_list, len(return_list)
    return return_list


def return_locations_inside_area(location_list, row_min, row_max, column_min, column_max):
    return_list = []
    for (row, column) in location_list:
        if row_min <= row < row_max:
            if column_min <= column < column_max:
                return_list.append((row, column))

    # print "Box", return_list, len(return_list)
    return return_list


def get_number_count(board, row_min, row_max, column_min, column_max):
        # Setup number count to get count of each value.  The value is (index + 1).
        number_count = [(0, []) for value in range(0, 9)]

        # Iterate over every row and column requested
        for row in range(row_min, row_max):
            for column in range(column_min, column_max):

                # Iterate over every possible value at the selected location
                for value in board[row][column].possibleValues:

                    # Get the count and location (couldn't modify in place)
                    count, location = number_count[value - 1]

                    # Increment how many times the value was found (identified by (index + 1)
                    count += 1

                    # Add the location to the location list, to be used later
                    location.append((row, column))

                    # Store the new count and location back into the array
                    number_count[value - 1] = (count, location)

        return number_count


def process_number_count(number_count, count_min, count_max):
    # List of the values that appear between count_min and count max (includes min and max)
    found_list = []

    for value in range(1, 10):
        # As number count is 0 indexed, need to use value - 1, as value is 1 indexed
        count, location_list = number_count[value - 1]
        if count_min <= count <= count_max:
            found_list.append((value, location_list))

    return found_list
