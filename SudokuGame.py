import Sudoku.Engine as Engine
import Sudoku.IO as IO
import datetime

def elegantSolverTest():
    # Load in board, and time how long it takes to solve.
    solver1 = Engine.ElegantSolver('Sudoku/Board 1.txt')
    solver2 = Engine.ElegantSolver('Sudoku/Board 2.txt')
    solver3 = Engine.ElegantSolver('Sudoku/Board 3.txt')
    solver4 = Engine.ElegantSolver('Sudoku/Board 4.txt')
    solver5 = Engine.ElegantSolver('Sudoku/Board 5.txt')
    solver6 = Engine.ElegantSolver('Sudoku/Board 6.txt')

    print "\nOriginal Board 1\n"
    IO.printBoard(solver1.board.board)
    print "\nOriginal Board 2\n"
    IO.printBoard(solver2.board.board)
    print "\nOriginal Board 3\n"
    IO.printBoard(solver3.board.board)
    print "\nOriginal Board 4\n"
    IO.printBoard(solver4.board.board)
    print "\nOriginal Board 5\n"
    IO.printBoard(solver5.board.board)
    print "\nOriginal Board 6\n"
    IO.printBoard(solver6.board.board)
    
    startTime = datetime.datetime.now()
    
    startTime1 = datetime.datetime.now()
    solvedBoard1, result = solver1.solve()
    endTime1 = datetime.datetime.now()

    startTime2 = datetime.datetime.now()
    solvedBoard2, result = solver2.solve()
    endTime2 = datetime.datetime.now()

    startTime3 = datetime.datetime.now()
    solvedBoard3, result = solver3.solve()
    endTime3 = datetime.datetime.now()

    startTime4 = datetime.datetime.now()
    solvedBoard4, result = solver4.solve()
    endTime4 = datetime.datetime.now()

    startTime5 = datetime.datetime.now()
    solvedBoard5, result = solver5.solve()
    endTime5 = datetime.datetime.now()
    
    startTime6 = datetime.datetime.now()
    solvedBoard6, result = solver6.solve()
    endTime6 = datetime.datetime.now()
    
    endTime = datetime.datetime.now()

    # Calculate the difference between the start and end time
    diffTime = endTime - startTime
    diffTime1 = endTime1 - startTime1
    diffTime2 = endTime2 - startTime2
    diffTime3 = endTime3 - startTime3
    diffTime4 = endTime4 - startTime4
    diffTime5 = endTime5 - startTime5
    diffTime6 = endTime6 - startTime6
    
    # Get the time in seconds
    time = float(diffTime.seconds) + float(diffTime.microseconds)/float(1000000)
    time1 = float(diffTime1.seconds) + float(diffTime1.microseconds)/float(1000000)
    time2 = float(diffTime2.seconds) + float(diffTime2.microseconds)/float(1000000)
    time3 = float(diffTime3.seconds) + float(diffTime3.microseconds)/float(1000000)
    time4 = float(diffTime4.seconds) + float(diffTime4.microseconds)/float(1000000)
    time5 = float(diffTime5.seconds) + float(diffTime5.microseconds)/float(1000000)
    time6 = float(diffTime6.seconds) + float(diffTime6.microseconds)/float(1000000)
    
    # Display information to the user.
    print time
    print ''
    
    print time1
    print "\nOriginal Board 1\n"
    IO.printBoard(solver1.board.board)
    print "\nSolved Board 1\n"
    IO.printBoard(solvedBoard1)

    print time2
    print "\nOriginal Board 2\n"
    IO.printBoard(solver2.board.board)
    print "\nSolved Board 2\n"
    IO.printBoard(solvedBoard2)

    print time3
    print "\nOriginal Board 3\n"
    IO.printBoard(solver3.board.board)
    print "\nSolved Board 3\n"
    IO.printBoard(solvedBoard3)

    print time4
    print "\nOriginal Board 4\n"
    IO.printBoard(solver4.board.board)
    print "\nSolved Board 4\n"
    IO.printBoard(solvedBoard4)

    print time5
    print "\nOriginal Board 5\n"
    IO.printBoard(solver5.board.board)
    print "\nSolved Board 5\n"
    IO.printBoard(solvedBoard5)

    print time6
    print "\nOriginal Board 6\n"
    IO.printBoard(solver6.board.board)
    print "\nSolved Board 6\n"
    IO.printBoard(solvedBoard6)

    print 'Board 1'
    smartSolveBoard('Sudoku/Board 1.txt')
    print 'Board 2'
    smartSolveBoard('Sudoku/Board 2.txt')
    print 'Board 3'
    smartSolveBoard('Sudoku/Board 3.txt')
    print 'Board 4'
    smartSolveBoard('Sudoku/Board 4.txt')
    print 'Board 5'
    smartSolveBoard('Sudoku/Board 5.txt')
    print 'Board 6'
    smartSolveBoard('Sudoku/Board 6.txt')

    # Test with single, hidden single
    # Board 1: 0.082, 0.413
    # Board 2: 0.001, 0.000
    # Board 3: 4.632, 4.669
    # Board 4: 0.002, 9.183
    # Board 5: 0.001, 0.424
    # Board 6: 0.003, 0.019
    # Total: 4.72, 14.708

    # Test with single, hidden single, double
    # Board 1: 0.002, 0.409
    # Board 2: 0.000, 0.000
    # Board 3: 4.626, 4.637
    # Board 4: 0.002, 9.137
    # Board 5: 0.002, 0.419
    # Board 6: 0.003, 0.019
    # Total: 4.635
    
    # Test with single, hiddlen single, double, hidden double
    # Board 1: 0.003, 0.408
    # Board 2: 0.001, 0.000
    # Board 3: 3.789, 4.626
    # Board 4: 0.003, 9.107
    # Board 5: 0.002, 0.418
    # Board 6: 0.005, 0.019
    # Total: 3.803


def smartSolveBoard(filePath):
    
    # Load in board, and time how long it takes to solve.
    board = Engine.Board(filePath)
    startTime = datetime.datetime.now()
    solvedBoard, result = Engine.SmartBruteForce(board)
    endTime = datetime.datetime.now()

    # Calculate the difference between the start and end time
    diffTime = endTime - startTime

    # Get the time in seconds
    time = float(diffTime.seconds) + float(diffTime.microseconds)/float(1000000)

    # Display information to the user.
    print time
    print "\nOriginal Board\n"
    IO.printBoard(board.board)
    print "\nSolved Board\n"
    IO.printBoard(solvedBoard)

    return solvedBoard, result


def solveBoard(filePath):

    # Load in board, and time how long it takes to solve.
    board = IO.loadBoard(filePath)
    startTime = datetime.datetime.now()
    solvedBoard, result = EnginebruteForce(board)
    endTime = datetime.datetime.now()

    # Calculate the difference between the start and end time
    diffTime = endTime - startTime

    # Get the time in seconds
    time = float(diffTime.seconds) + float(diffTime.microseconds)/float(1000000)

    # Display information to the user.
    print time
    print "\nOriginal Board\n"
    IO.printBoard(board)
    print "\nSolved Board\n"
    IO.printBoard(solvedBoard)

    return solvedBoard, result


'''
Board 1

5 2 8|4 7 3|1 9 6
9 3 1|6 2 5|4 7 8
7 6 4|9 1 8|2 3 5
-----+-----+-----
3 7 9|2 8 4|5 6 1
8 5 2|7 6 1|9 4 3
4 1 6|5 3 9|7 8 2
-----+-----+-----
1 9 5|3 4 6|8 2 7
2 4 3|8 5 7|6 1 9
6 8 7|1 9 2|3 5 4

Board 2

1 4 5|3 2 7|6 9 8
8 3 9|6 5 4|1 2 7
6 7 2|9 1 8|5 4 3
-----+-----+-----
4 9 6|1 8 5|3 7 2
2 1 8|4 7 3|9 5 6
7 5 3|2 9 6|4 8 1
-----+-----+-----
3 6 7|5 4 2|8 1 9
9 8 4|7 6 1|2 3 5
5 2 1|8 3 9|7 6 4

Board 3

2 5 3|7 6 9|1 4 8
1 8 4|3 5 2|6 9 7
7 6 9|8 4 1|5 2 3
-----+-----+-----
5 4 2|9 3 6|8 7 1
6 7 8|1 2 5|4 3 9
9 3 1|4 8 7|2 5 6
-----+-----+-----
8 9 7|2 1 4|3 6 5
3 2 6|5 9 8|7 1 4
4 1 5|6 7 3|9 8 2

Board 4

9 3 1|2 7 8|6 5 4
5 8 4|9 1 6|7 3 2
7 2 6|5 4 3|1 9 8
-----+-----+-----
1 5 3|8 2 4|9 7 6
6 9 8|1 5 7|4 2 3
4 7 2|6 3 9|5 8 1
-----+-----+-----
8 6 7|4 9 2|3 1 5
3 4 5|7 8 1|2 6 9
2 1 9|3 6 5|8 4 7

Board 5

4 5 2|6 1 8|3 7 9
3 7 1|4 2 9|8 6 5
9 8 6|5 7 3|2 4 1
-----+-----+-----
7 3 4|1 6 2|5 9 8
6 2 9|8 4 5|7 1 3
8 1 5|3 9 7|6 2 4
-----+-----+-----
2 9 3|7 5 4|1 8 6
1 4 8|2 3 6|9 5 7
5 6 7|9 8 1|4 3 2

Board 6

5 3 9|2 7 6|4 1 8
7 2 8|3 1 4|9 6 5
6 4 1|8 9 5|7 3 2
-----+-----+-----
4 6 2|5 3 9|8 7 1
3 8 5|7 2 1|6 4 9
1 9 7|4 6 8|2 5 3
-----+-----+-----
2 5 6|1 8 7|3 9 4
9 1 3|6 4 2|5 8 7
8 7 4|9 5 3|1 2 6
'''
