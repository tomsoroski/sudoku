# Brute force Sudoku solver

import time
start_time = time.time()

B = " "
# Represents a blank square

BD1 = [B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B]

BD2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B,
       B, B, B, B, B, B, B, B, B]

BD3 = [1, B, B, B, B, B, B, B, B,
       2, B, B, B, B, B, B, B, B,
       3, B, B, B, B, B, B, B, B,
       4, B, B, B, B, B, B, B, B,
       5, B, B, B, B, B, B, B, B,
       6, B, B, B, B, B, B, B, B,
       7, B, B, B, B, B, B, B, B,
       8, B, B, B, B, B, B, B, B,
       9, B, B, B, B, B, B, B, B]

# Easy Board
BD4 = [2, 7, 4, B, 9, 1, B, B, 5,
       1, B, B, 5, B, B, B, 9, B,
       6, B, B, B, B, 3, 2, 8, B,
       B, B, 1, 9, B, B, B, B, 8,
       B, B, 5, 1, B, B, 6, B, B,
       7, B, B, B, 8, B, B, B, 3,
       4, B, 2, B, B, B, B, B, 9,
       B, B, B, B, B, B, B, 7, B,
       8, B, B, 3, 4, 9, B, B, B]

# Solution to BD4
BD4s = [2, 7, 4, 8, 9, 1, 3, 6, 5,
        1, 3, 8, 5, 2, 6, 4, 9, 7,
        6, 5, 9, 4, 7, 3, 2, 8, 1,
        3, 2, 1, 9, 6, 4, 7, 5, 8,
        9, 8, 5, 1, 3, 7, 6, 4, 2,
        7, 4, 6, 2, 8, 5, 9, 1, 3,
        4, 6, 2, 7, 5, 8, 1, 3, 9,
        5, 9, 3, 6, 1, 2, 8, 7, 4,
        8, 1, 7, 3, 4, 9, 5, 2, 6]

# Hard Board
BD5 = [5, B, B, B, B, 4, B, 7, B,
       B, 1, B, B, 5, B, 6, B, B,
       B, B, 4, 9, B, B, B, B, B,
       B, 9, B, B, B, 7, 5, B, B,
       1, 8, B, 2, B, B, B, B, B,
       B, B, B, B, B, 6, B, B, B,
       B, B, 3, B, B, B, B, B, 8,
       B, 6, B, B, 8, B, B, B, 9,
       B, B, 8, B, 7, B, B, 3, 1]

# Solution to BD5
BD5s = [5, 3, 9, 1, 6, 4, 8, 7, 2,
        8, 1, 2, 7, 5, 3, 6, 9, 4,
        6, 7, 4, 9, 2, 8, 3, 1, 5,
        2, 9, 6, 4, 1, 7, 5, 8, 3,
        1, 8, 7, 2, 3, 5, 9, 4, 6,
        3, 4, 5, 8, 9, 6, 1, 2, 7,
        9, 2, 3, 5, 4, 1, 7, 6, 8,
        7, 6, 1, 3, 8, 2, 4, 5, 9,
        4, 5, 8, 6, 7, 9, 2, 3, 1]

# Hardest Board Ever
BD6 = [B, B, 5, 3, B, B, B, B, B,
       8, B, B, B, B, B, B, 2, B,
       B, 7, B, B, 1, B, 5, B, B,
       4, B, B, B, B, 5, 3, B, B,
       B, 1, B, B, 7, B, B, B, 6,
       B, B, 3, 2, B, B, B, 8, B,
       B, 6, B, 5, B, B, B, B, 9,
       B, B, 4, B, B, B, B, 3, B,
       B, B, B, B, B, 9, 7, B, B]

# Solution to BD6
BD6s = [1, 4, 5, 3, 2, 7, 6, 9, 8,
        8, 3, 9, 6, 5, 4, 1, 2, 7,
        6, 7, 2, 9, 1, 8, 5, 4, 3,
        4, 9, 6, 1, 8, 5, 3, 7, 2,
        2, 1, 8, 4, 7, 3, 9, 5, 6,
        7, 5, 3, 2, 9, 6, 4, 8, 1,
        3, 6, 7, 5, 4, 2, 8, 1, 9,
        9, 8, 4, 7, 6, 1, 2, 3, 5,
        5, 2, 1, 8, 3, 9, 7, 6, 4]

# No Solution
BD7 = [1, 2, 3, 4, 5, 6, 7, 8, B,
       B, B, B, B, B, B, B, B, 2,
       B, B, B, B, B, B, B, B, 3,
       B, B, B, B, B, B, B, B, 4,
       B, B, B, B, B, B, B, B, 5,
       B, B, B, B, B, B, B, B, 6,
       B, B, B, B, B, B, B, B, 7,
       B, B, B, B, B, B, B, B, 8,
       B, B, B, B, B, B, B, B, 9]

# List indices of one unit
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Values permissible in a given Sudoku cell
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List indices of each row
rows = [[0,  1,  2,  3,  4,  5,  6,  7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23, 24, 25, 26],
        [27, 28, 29, 30, 31, 32, 33, 34, 35],
        [36, 37, 38, 39, 40, 41, 42, 43, 44],
        [45, 46, 47, 48, 49, 50, 51, 52, 53],
        [54, 55, 56, 57, 58, 59, 60, 61, 62],
        [63, 64, 65, 66, 67, 68, 69, 70, 71],
        [72, 73, 74, 75, 76, 77, 78, 79, 80]]

# List indices of each column
cols = [[0,  9, 18, 27, 36, 45, 54, 63, 72],
        [1, 10, 19, 28, 37, 46, 55, 64, 73],
        [2, 11, 20, 29, 38, 47, 56, 65, 74],
        [3, 12, 21, 30, 39, 48, 57, 66, 75],
        [4, 13, 22, 31, 40, 49, 58, 67, 76],
        [5, 14, 23, 32, 41, 50, 59, 68, 77],
        [6, 15, 24, 33, 42, 51, 60, 69, 78],
        [7, 16, 25, 34, 43, 52, 61, 70, 79],
        [8, 17, 26, 35, 44, 53, 62, 71, 80]]

# List indices of each square (3x3)
sqrs = [[0,  1,  2,  9,  10, 11, 18, 19, 20],
        [3,  4,  5,  12, 13, 14, 21, 22, 23],
        [6,  7,  8,  15, 16, 17, 24, 25, 26],
        [27, 28, 29, 36, 37, 38, 45, 46, 47],
        [30, 31, 32, 39, 40, 41, 48, 49, 50],
        [33, 34, 35, 42, 43, 44, 51, 52, 53],
        [54, 55, 56, 63, 64, 65, 72, 73, 74],
        [57, 58, 59, 66, 67, 68, 75, 76, 77],
        [60, 61, 62, 69, 70, 71, 78, 79, 80]]

def print_board(bd):
    """Prints a Sudoku board in a 9x9 grid, with 1 space between each value"""
    print("-----------------")
    for row in rows:
        to_print = ""
        for num in nums:
            to_print += str(bd[row[num]]) + " "
        print(to_print)
    print("-----------------")


def solve_board(bd):
    """Given initial board, produces the first legal result, or false if unsolvable"""
    if is_solved(bd):
        print_board(bd)
        return
    elif len(next_valid_boards(bd)) == 0:
        return False
    else:
        for board in next_valid_boards(bd):
            solve_board(board)


def next_valid_boards(bd):
    return list(filter(is_board_valid, next_boards(bd)))


def next_boards(bd):
    """Produces a list of all next boards given board"""
    lobd = []
    for value in values:
        lobd += [fill_spot(find_blank(bd), bd, value)]
    return lobd


def fill_spot(blank_spot, bd, num):
    if blank_spot == 0:
        return [num] + bd[1:81]
    elif blank_spot == 80:
        return bd[0:80] + [num]
    else:
        return bd[:blank_spot] + [num] + bd[(blank_spot + 1):81]


def find_blank(bd):
    """Returns the location of the first blank in board"""
    count = 0
    for num in bd:
        if num == " ":
            return count
        else:
            count += 1


def is_solved(bd):
    """ Returns True if the given board is solved. False otherwise"""
    """ CONSTRAINT: Assumes board is valid"""
    count = 0
    for pos in bd:
        if pos == " ":
            count += 1
        else:
            continue
    if count > 0:
        return False
    else:
        return True


def is_board_valid(bd):
    """Returns True if all rows, cols, and squares of Board are valid"""
    return is_rows_valid(bd) and is_cols_valid(bd) and is_sqrs_valid(bd)


def is_rows_valid(bd):
    """Produce True if all the rows in board are valid"""
    for row in rows:
        seen = []
        for num in nums:
            if bd[row[num]] == " ":
                continue
            elif bd[row[num]] not in seen:
                seen += [bd[row[num]]]
            else:
                return False
        else:
            continue
    return True


def is_cols_valid(bd):
    """Produce True if all the columns in board are valid"""
    for col in cols:
        seen = []
        for num in nums:
            if bd[col[num]] == " ":
                continue
            elif bd[col[num]] not in seen:
                seen += [bd[col[num]]]
            else:
                return False
        else:
            continue
    return True


def is_sqrs_valid(bd):
    """Produce True if all the squares in board are valid"""
    for sqr in sqrs:
        seen = []
        for num in nums:
            if bd[sqr[num]] == " ":
                continue
            elif bd[sqr[num]] not in seen:
                seen += [bd[sqr[num]]]
            else:
                return False
        else:
            continue
    return True

solve_board(BD6)
print("--- %s seconds ---" % (time.time() - start_time))
