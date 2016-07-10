import IO


# 1 Singles in box
# 1 Hidden Singles in row/column/box
# 0 Values locked to row/column in box
# 1 Pairs in row/column/box
# 0 Triples in row/column/box
# 0 Quads in row/column/box
# 1 Hidden Pairs in row/column/box
# 1 Hidden Triples in row/column/box (rare)
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
