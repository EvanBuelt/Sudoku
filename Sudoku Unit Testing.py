import unittest
import Sudoku

class Test(unittest.TestCase):
    def setUp(self):
        # Partial board to see if it is valid.
        self.validBoard1 = [[1,4,5,3,2,7,6,9,8],
                            [8,3,9,6,5,4,1,0,7],
                            [6,7,2,0,0,0,0,4,3],
                            [4,0,6,0,8,5,3,7,0],
                            [0,1,8,4,0,3,9,5,0],
                            [0,0,0,2,9,6,4,0,1],
                            [3,6,7,0,4,0,0,1,9],
                            [0,8,0,7,0,1,0,0,5],
                            [0,2,0,8,0,9,0,6,0]]

        # Like above, but position (0,1) is blank as well.
        self.validBoard2 = [[1,0,5,3,2,7,6,9,8],
                            [8,3,9,6,5,4,1,2,7],
                            [6,7,2,0,0,0,0,4,3],
                            [4,0,6,0,8,5,3,7,0],
                            [0,1,8,4,0,3,9,5,0],
                            [7,5,0,2,9,6,4,0,1],
                            [3,6,7,0,4,0,0,1,9],
                            [0,8,0,7,0,1,0,3,5],
                            [0,2,0,8,0,9,0,6,0]]

        # Check to make sure a blank sudoku puzzle is valid
        self.validBoard3 = [[0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0]]

        self.solvedBoard1 = [[1,4,5,3,2,7,6,9,8],
                             [8,3,9,6,5,4,1,2,7],
                             [6,7,2,9,1,8,5,4,3],
                             [4,9,6,1,8,5,3,7,2],
                             [2,1,8,4,7,3,9,5,6],
                             [7,5,3,2,9,6,4,8,1],
                             [3,6,7,5,4,2,8,1,9],
                             [9,8,4,7,6,1,2,3,5],
                             [5,2,1,8,3,9,7,6,4]]

        self.solvedBoard2 = [[1,2,3,4,5,6,7,8,9],
                             [4,5,6,7,8,9,1,2,3],
                             [7,8,9,1,2,3,4,5,6],
                             [2,1,4,3,6,5,8,9,7],
                             [3,6,5,8,9,7,2,1,4],
                             [8,9,7,2,1,4,3,6,5],
                             [5,3,1,6,4,2,9,7,8],
                             [6,4,2,9,7,8,5,3,1],
                             [9,7,8,5,3,1,6,4,2]]

        # Valid rows, but invalid Columns
        self.invalidBoard1 = [[1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9],
                              [1,2,3,4,5,6,7,8,9]]

        # Valid Columns, but invalid Rows
        self.invalidBoard2 = [[1,1,1,1,1,1,1,1,1],
                              [2,2,2,2,2,2,2,2,2],
                              [3,3,3,3,3,3,3,3,3],
                              [4,4,4,4,4,4,4,4,4],
                              [5,5,5,5,5,5,5,5,5],
                              [6,6,6,6,6,6,6,6,6],
                              [7,7,7,7,7,7,7,7,7],
                              [8,8,8,8,8,8,8,8,8],
                              [9,9,9,9,9,9,9,9,9]]

        # Invalid Boxes, but valid column and rows
        self.invalidBoard3 = [[1,2,3,4,5,6,7,8,9],
                              [2,3,1,5,6,4,8,9,7],
                              [3,1,2,6,4,5,9,7,8],
                              [4,5,6,7,8,9,1,2,3],
                              [5,6,4,8,9,7,2,3,1],
                              [6,4,5,9,7,8,3,1,2],
                              [7,8,9,1,2,3,4,5,6],
                              [8,9,7,2,3,1,5,6,4],
                              [9,7,8,3,1,2,6,4,5]]

        # All values are same.  Invalid column, row, and boxes
        self.invalidBoard4 = [[1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1],
                              [1,1,1,1,1,1,1,1,1]]

        # Same as invalidBoard4, but different value.
        self.invalidBoard5 = [[5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5],
                              [5,5,5,5,5,5,5,5,5]]

    def test_loadBoard(self):
        
        loadedBoard = Sudoku.loadBoard('Unit Test Board 1.txt')
        self.assertEqual(loadedBoard, self.solvedBoard1)

    def test_findBlank(self):
        
        self.assertEqual(Sudoku.findBlank(self.validBoard1), (1, 7))
        self.assertEqual(Sudoku.findBlank(self.validBoard2), (0, 1))
        for i in range(0,9):
            for j in range(0,9):
                self.assertNotEqual(Sudoku.findBlank(self.solvedBoard1), (i, j))

    def test_isValidBoard(self):

        self.assertTrue(Sudoku.isValidBoard(self.validBoard1))
        self.assertTrue(Sudoku.isValidBoard(self.validBoard2))
        self.assertTrue(Sudoku.isValidBoard(self.validBoard3))
        self.assertTrue(Sudoku.isValidBoard(self.solvedBoard1))
        self.assertTrue(Sudoku.isValidBoard(self.solvedBoard2))
        self.assertFalse(Sudoku.isValidBoard(self.invalidBoard1))
        self.assertFalse(Sudoku.isValidBoard(self.invalidBoard2))
        self.assertFalse(Sudoku.isValidBoard(self.invalidBoard3))
        self.assertFalse(Sudoku.isValidBoard(self.invalidBoard4))
        self.assertFalse(Sudoku.isValidBoard(self.invalidBoard5))

    def test_isSolvedBoard(self):

        self.assertTrue(Sudoku.isSolvedBoard(self.solvedBoard1))
        self.assertTrue(Sudoku.isSolvedBoard(self.solvedBoard2))
        self.assertFalse(Sudoku.isSolvedBoard(self.validBoard1))
        self.assertFalse(Sudoku.isSolvedBoard(self.validBoard2))
        self.assertFalse(Sudoku.isSolvedBoard(self.validBoard3))
        self.assertFalse(Sudoku.isSolvedBoard(self.invalidBoard1))
        self.assertFalse(Sudoku.isSolvedBoard(self.invalidBoard2))
        self.assertFalse(Sudoku.isSolvedBoard(self.invalidBoard3))
        self.assertFalse(Sudoku.isSolvedBoard(self.invalidBoard4))
        self.assertFalse(Sudoku.isSolvedBoard(self.invalidBoard5))

    def test_checkColumns(self):

        self.assertTrue(Sudoku.checkColumns(self.solvedBoard1))
        self.assertTrue(Sudoku.checkColumns(self.solvedBoard2))
        self.assertTrue(Sudoku.checkColumns(self.validBoard1))
        self.assertTrue(Sudoku.checkColumns(self.validBoard2))
        self.assertTrue(Sudoku.checkColumns(self.validBoard3))
        self.assertFalse(Sudoku.checkColumns(self.invalidBoard1))
        self.assertTrue(Sudoku.checkColumns(self.invalidBoard2))
        self.assertTrue(Sudoku.checkColumns(self.invalidBoard3))
        self.assertFalse(Sudoku.checkColumns(self.invalidBoard4))
        self.assertFalse(Sudoku.checkColumns(self.invalidBoard5))

    def test_checkRows(self):
        
        self.assertTrue(Sudoku.checkRows(self.solvedBoard1))
        self.assertTrue(Sudoku.checkRows(self.solvedBoard2))
        self.assertTrue(Sudoku.checkRows(self.validBoard1))
        self.assertTrue(Sudoku.checkRows(self.validBoard2))
        self.assertTrue(Sudoku.checkRows(self.validBoard3))
        self.assertTrue(Sudoku.checkRows(self.invalidBoard1))
        self.assertFalse(Sudoku.checkRows(self.invalidBoard2))
        self.assertTrue(Sudoku.checkRows(self.invalidBoard3))
        self.assertFalse(Sudoku.checkRows(self.invalidBoard4))
        self.assertFalse(Sudoku.checkRows(self.invalidBoard5))

    def test_checkBoxes(self):

        self.assertTrue(Sudoku.checkBoxes(self.solvedBoard1))
        self.assertTrue(Sudoku.checkBoxes(self.solvedBoard2))
        self.assertTrue(Sudoku.checkBoxes(self.validBoard1))
        self.assertTrue(Sudoku.checkBoxes(self.validBoard2))
        self.assertTrue(Sudoku.checkBoxes(self.validBoard3))
        self.assertFalse(Sudoku.checkBoxes(self.invalidBoard1))
        self.assertFalse(Sudoku.checkBoxes(self.invalidBoard2))
        self.assertFalse(Sudoku.checkBoxes(self.invalidBoard3))
        self.assertFalse(Sudoku.checkBoxes(self.invalidBoard4))
        self.assertFalse(Sudoku.checkBoxes(self.invalidBoard5))

    def test_printBoard(self):
        pass

    def test_solveBoard(self):

        result1 = ([[1, 4, 5, 3, 2, 7, 6, 9, 8],
                    [8, 3, 9, 6, 5, 4, 1, 2, 7],
                    [6, 7, 2, 9, 1, 8, 5, 4, 3],
                    [4, 9, 6, 1, 8, 5, 3, 7, 2],
                    [2, 1, 8, 4, 7, 3, 9, 5, 6],
                    [7, 5, 3, 2, 9, 6, 4, 8, 1],
                    [3, 6, 7, 5, 4, 2, 8, 1, 9],
                    [9, 8, 4, 7, 6, 1, 2, 3, 5],
                    [5, 2, 1, 8, 3, 9, 7, 6, 4]], True)
        
        result2 = ([[2, 5, 3, 7, 6, 9, 1, 4, 8],
                    [1, 8, 4, 3, 5, 2, 6, 9, 7],
                    [7, 6, 9, 8, 4, 1, 5, 2, 3],
                    [5, 4, 2, 9, 3, 6, 8, 7, 1],
                    [6, 7, 8, 1, 2, 5, 4, 3, 9],
                    [9, 3, 1, 4, 8, 7, 2, 5, 6],
                    [8, 9, 7, 2, 1, 4, 3, 6, 5],
                    [3, 2, 6, 5, 9, 8, 7, 1, 4],
                    [4, 1, 5, 6, 7, 3, 9, 8, 2]], True)

        result3 = ([[5, 2, 8, 4, 7, 3, 1, 9, 6],
                    [9, 3, 1, 6, 2, 5, 4, 7, 8],
                    [7, 6, 4, 9, 1, 8, 2, 3, 5],
                    [3, 7, 9, 2, 8, 4, 5, 6, 1],
                    [8, 5, 2, 7, 6, 1, 9, 4, 3],
                    [4, 1, 6, 5, 3, 9, 7, 8, 2],
                    [1, 9, 5, 3, 4, 6, 8, 2, 7],
                    [2, 4, 3, 8, 5, 7, 6, 1, 9],
                    [6, 8, 7, 1, 9, 2, 3, 5, 4]], True)

        result4 = ([[1, 4, 5, 3, 2, 7, 6, 9, 8],
                    [8, 3, 9, 6, 5, 4, 1, 2, 7],
                    [6, 7, 2, 9, 1, 8, 5, 4, 3],
                    [4, 9, 6, 1, 8, 5, 3, 7, 2],
                    [2, 1, 8, 4, 7, 3, 9, 5, 6],
                    [7, 5, 3, 2, 9, 6, 4, 8, 1],
                    [3, 6, 7, 5, 4, 2, 8, 1, 9],
                    [9, 8, 4, 7, 6, 1, 2, 3, 5],
                    [5, 2, 1, 8, 3, 9, 7, 6, 4]], True)

        self.assertEqual(Sudoku.solveBoard('Unit Test Board 1.txt'), result1)
        self.assertEqual(Sudoku.solveBoard('Unit Test Board 2.txt'), result2)
        self.assertEqual(Sudoku.solveBoard('Unit Test Board 3.txt'), result3)
        self.assertEqual(Sudoku.solveBoard('Unit Test Board 4.txt'), result4)

if __name__ == '__main__':
    unittest.main()
