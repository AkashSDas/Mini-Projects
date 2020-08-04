import random

board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True

            # If our solution is incorrect then we reset the value back to 0
            board[row][column] = 0

    return False


def valid(board, entry, position):
    row, column = position

    # Check row
    for i in range(len(board[0])):
        if board[row][i] == entry and column != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][column] == entry and row != i:
            return False

    # Check 3x3 box
    box_x = column // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == entry and (i, j) != (row, column):
                return False

    return True


def display_board(board):
    for i in range(len(board)):
        for j in range(0, len(board[i]), 3):
            print(f"{board[i][j]} {board[i][j+1]} {board[i][j+2]}", end="")
            if (j+3) % 3 == 0 and (j+3) != 9:
                print(" | ", end="")
        print(end="\n")
        if (i+1) % 3 == 0 and i != 0 and (i+1) != 9:
            print("- - - - - - - - - - -")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


display_board(board)
solve(board)
print()
display_board(board)


def generate_random_sudoku_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve(board)
    random.shuffle(board)
    return board


board = generate_random_sudoku_board()
print()
display_board(board)


def make_random_decision(difficulty_level):
    if difficulty_level == 'Easy':
        if random.random() <= 0.6:
            return False
        else:
            return True

    if difficulty_level == 'Medium':
        if random.random() <= 0.4:
            return False
        else:
            return True

    if difficulty_level == 'Hard':
        if random.random() <= 0.2:
            return False
        else:
            return True


def set_value_to_0(board, difficulty_level):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if make_random_decision(difficulty_level):
                board[i][j] = 0
    return board


def generate_random_sudoku_board_to_play(difficulty_level):
    board = generate_random_sudoku_board()

    if difficulty_level == 'Easy':
        board = set_value_to_0(board, difficulty_level)
    if difficulty_level == 'Medium':
        board = set_value_to_0(board, difficulty_level)
    if difficulty_level == 'Hard':
        board = set_value_to_0(board, difficulty_level)

    return board


board = generate_random_sudoku_board_to_play('Medium')
print()
display_board(board)
