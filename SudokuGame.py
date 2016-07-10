import datetime

import Sudoku.Solver.Engine as Engine
import Sudoku.Solver.ElegantSolver as ElegantSolver
import Sudoku.Solver.BruteForce as BruteForce

import Sudoku.Solver.IO as IO


def elegant_solver_test():
    board_start = 1
    board_end = 6

    boards = []
    solved_boards_and_results = []
    board_time = []

    # Load in all boards
    for board_number in range(board_start, board_end + 1):
        file_path = 'Sudoku/Boards/board ' + str(board_number) + '.txt'
        boards.append(ElegantSolver.ElegantSolver(file_path))

    # Print original board
    for board_number in range(board_start, board_end + 1):
        solver = boards[board_number - 1]
        print '\nOriginal Board ' + str(board_number) + '\n'
        IO.print_board(solver.board.raw_board)

    # Get time for all boards
    start_time = datetime.datetime.now()

    for board_number in range(board_start, board_end + 1):
        solver = boards[board_number - 1]

        start_time_board = datetime.datetime.now()
        print '\nSolved Board ' + str(board_number) + '\n'
        solved_boards_and_results.append(solver.solve())
        end_time_board = datetime.datetime.now()

        board_time.append(end_time_board - start_time_board)

    # Get time for all boards
    end_time = datetime.datetime.now()

    # Calculate the difference between the start and end time for all boards
    diff_time = end_time - start_time

    # Get the time in seconds
    time = float(diff_time.seconds) + float(diff_time.microseconds) / float(1000000)

    # for board_number in range(board_start, board_end + 1):
    #     my_time = board_time[board_number - 1]
    #     board_time[board_number] = float(my_time.seconds) + float(my_time.microseconds) / float(1000000)

    # Display information to the user.
    print '\nTotal time'
    print time
    print ''

    # for board_number in range(board_start, board_end + 1):
    #     print '\nTime for Board ' + str(board_number)
    #     print board_time[board_number - 1]

    '''
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
    '''

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
    solved_board, result = BruteForce.smart_brute_force(board)
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
    solved_board, result = BruteForce.brute_force(board)
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
