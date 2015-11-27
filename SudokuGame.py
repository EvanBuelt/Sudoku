import Sudoku.Engine as Engine
import Sudoku.IO as IO
import datetime


def elegant_solver_test():
    # Load in all boards
    solver1 = Engine.ElegantSolver('Sudoku/Board 1.txt')
    solver2 = Engine.ElegantSolver('Sudoku/Board 2.txt')
    solver3 = Engine.ElegantSolver('Sudoku/Board 3.txt')
    solver4 = Engine.ElegantSolver('Sudoku/Board 4.txt')
    solver5 = Engine.ElegantSolver('Sudoku/Board 5.txt')
    solver6 = Engine.ElegantSolver('Sudoku/Board 6.txt')

    print "\nOriginal Board 1\n"
    IO.print_board(solver1.board.raw_board)

    print "\nOriginal Board 2\n"
    IO.print_board(solver2.board.raw_board)

    print "\nOriginal Board 3\n"
    IO.print_board(solver3.board.raw_board)

    print "\nOriginal Board 4\n"
    IO.print_board(solver4.board.raw_board)

    print "\nOriginal Board 5\n"
    IO.print_board(solver5.board.raw_board)

    print "\nOriginal Board 6\n"
    IO.print_board(solver6.board.raw_board)

    # Get time for all boards
    start_time = datetime.datetime.now()

    print "\nBoard 1\n"
    # Get time for first board
    start_time_1 = datetime.datetime.now()
    solved_board_1, result = solver1.solve()
    end_time_1 = datetime.datetime.now()

    print "\nBoard 2\n"
    # Get time for second board
    start_time_2 = datetime.datetime.now()
    solved_board_2, result = solver2.solve()
    end_time_2 = datetime.datetime.now()

    print "\nBoard 3\n"
    # Get time for third board
    start_time_3 = datetime.datetime.now()
    solved_board_3, result = solver3.solve()
    end_time_3 = datetime.datetime.now()

    print "\nBoard 4\n"
    # Get time for fourth board
    start_time_4 = datetime.datetime.now()
    solved_board_4, result = solver4.solve()
    end_time_4 = datetime.datetime.now()

    print "\nBoard 5\n"
    # Get time for fifth board
    start_time_5 = datetime.datetime.now()
    solved_board_5, result = solver5.solve()
    end_time_5 = datetime.datetime.now()

    print "\nBoard 6\n"
    # Get time for sixth board
    start_time_6 = datetime.datetime.now()
    solved_board_6, result = solver6.solve()
    end_time_6 = datetime.datetime.now()

    # Get time for all boards
    end_time = datetime.datetime.now()

    # Calculate the difference between the start and end time for all boards
    diff_time = end_time - start_time
    diff_time_1 = end_time_1 - start_time_1
    diff_time_2 = end_time_2 - start_time_2
    diff_time_3 = end_time_3 - start_time_3
    diff_time_4 = end_time_4 - start_time_4
    diff_time_5 = end_time_5 - start_time_5
    diff_time_6 = end_time_6 - start_time_6

    # Get the time in seconds
    time = float(diff_time.seconds) + float(diff_time.microseconds) / float(1000000)
    time1 = float(diff_time_1.seconds) + float(diff_time_1.microseconds) / float(1000000)
    time2 = float(diff_time_2.seconds) + float(diff_time_2.microseconds) / float(1000000)
    time3 = float(diff_time_3.seconds) + float(diff_time_3.microseconds) / float(1000000)
    time4 = float(diff_time_4.seconds) + float(diff_time_4.microseconds) / float(1000000)
    time5 = float(diff_time_5.seconds) + float(diff_time_5.microseconds) / float(1000000)
    time6 = float(diff_time_6.seconds) + float(diff_time_6.microseconds) / float(1000000)

    # Display information to the user.
    print time
    print ''

    print time1
    print "\nSolved Board 1\n"
    IO.print_board(solved_board_1)

    print time2
    print "\nSolved Board 2\n"
    IO.print_board(solved_board_2)

    print time3
    print "\nSolved Board 3\n"
    IO.print_board(solved_board_3)

    print time4
    print "\nSolved Board 4\n"
    IO.print_board(solved_board_4)

    print time5
    print "\nSolved Board 5\n"
    IO.print_board(solved_board_5)

    print time6
    print "\nSolved Board 6\n"
    IO.print_board(solved_board_6)

    # Print information using Brute Force, to compare to the elegant solution
    print 'Brute Force Method\n'
    print 'Board 1'
    smart_solve_board('Sudoku/Board 1.txt')
    print 'Board 2'
    smart_solve_board('Sudoku/Board 2.txt')
    print 'Board 3'
    smart_solve_board('Sudoku/Board 3.txt')
    print 'Board 4'
    smart_solve_board('Sudoku/Board 4.txt')
    print 'Board 5'
    smart_solve_board('Sudoku/Board 5.txt')
    print 'Board 6'
    smart_solve_board('Sudoku/Board 6.txt')

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


def smart_solve_board(file_path):
    # Load in board, and time how long it takes to solve.
    board = Engine.Board(file_path)
    start_time = datetime.datetime.now()
    solved_board, result = Engine.smart_brute_force(board)
    end_time = datetime.datetime.now()

    # Calculate the difference between the start and end time
    diff_time = end_time - start_time

    # Get the time in seconds
    time = float(diff_time.seconds) + float(diff_time.microseconds) / float(1000000)

    # Display information to the user.
    print time
    print "\nOriginal Board\n"
    IO.print_board(board.raw_board)
    print "\nSolved Board\n"
    IO.print_board(solved_board)

    return solved_board, result


def solve_board(file_path):
    # Load in board, and time how long it takes to solve.
    board = IO.load_board(file_path)
    start_time = datetime.datetime.now()
    solved_board, result = Engine.brute_force(board)
    end_time = datetime.datetime.now()

    # Calculate the difference between the start and end time
    diff_time = end_time - start_time

    # Get the time in seconds
    time = float(diff_time.seconds) + float(diff_time.microseconds) / float(1000000)

    # Display information to the user.
    print time
    print "\nOriginal Board\n"
    IO.print_board(board)
    print "\nSolved Board\n"
    IO.print_board(solved_board)

    return solved_board, result


elegant_solver_test()

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
