# Sudoku
Solves a sudoku board.  
Version 1.0
-Brute Force Method solves standard 9x9 sudoku board.
-Format of text file for board is 9 lines of 9 numbers separated by spaces.  Use 0 if box is blank.
-Functions:

loadBoard(filePath): board
filePath: File Location for board file
board: 9x9 list of list of numbers

bruteForce(board): board, result
board: 9x9 list of list of numbers
result: whether algorithm was able to find a valid solution

findBlank(board): x, y
board: 9x9 list of list of numbers
x: column of first blank box found
y: row of first blank box found

isValidBoard(board): result
board: 9x9 list of list of numbers
result: returns true if there are no repeated numbers in any row, column, or 3x3 box

isCompleteBoard(board): result
board: 9x9 list of list of numbers
result: returns true if board is valid and every box contains a valid number

check*(board): result
board: 9x9 list of list of numbers
result: returns true if row, column, or 3x3 box contains no repeated number. (3 functions for row, column, and 3x3 box)

printBoard(board):
board: 9x9 list of list of numbers

solveBoard(filePath):
filePath: File Location for board file