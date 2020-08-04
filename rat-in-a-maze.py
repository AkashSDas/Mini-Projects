import random

steps = 0


def get_path_or_block():
    if random.random() <= 0.8:
        return 1
    else:
        return 0


def creat_maze(N):
    maze = [[get_path_or_block() for _ in range(N)] for _ in range(N)]
    return maze


def display_maze(maze):
    for row in maze:
        print(row)
    print()


def valid(maze, x, y):
    N = len(maze)
    if x < N and y < N and x >= 0 and y >= 0 and maze[x][y] == 1:
        return True
    return False


def result_maze(N):
    maze = [[0 for _ in range(N)] for _ in range(N)]
    return maze


def find_path(maze, x, y, solution_maze):
    global steps
    N = len(maze)

    if (x == N-1) and (y == N-1):
        if valid(maze, x, y):
            solution_maze[x][y] = 1
            steps += 1
            return True
        steps -= 1
        return False

    if valid(maze, x, y):
        solution_maze[x][y] = 1
        steps += 1

        # Moving in x direction
        if find_path(maze, x, y+1, solution_maze):
            steps += 1
            return True

        # Moving in y direction
        if find_path(maze, x+1, y, solution_maze):
            steps += 1
            return True

        steps -= 1
        solution_maze[x][y] = 0
        return False


maze = creat_maze(10)
display_maze(maze)

result = result_maze(10)
display_maze(result)

find_path(maze, 0, 0, result)
display_maze(result)

print(f'It took {steps} steps to reach the end')
