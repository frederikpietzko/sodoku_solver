from pprint import pprint as print
from generate import create_puzzle
import os


def clear(): return os.system('clear')


def contains_zero(grid):
    for i in range(9):
        for j in range(9):
            cell = grid[i][j]
            if cell == 0:
                return True, i, j
    return False, None, None


def num_in_row(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
            return True
    return False


def num_in_col(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return True
    return False


def num_in_block(grid, row, col, num):
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return True
    return False


def is_safe(grid, row, col, num):
    num_used = num_in_row(grid, row, num) or num_in_col(
        grid, col, num) or num_in_block(grid, row, col, num)
    return not num_used


def solve(grid):
    found_something, row, col = contains_zero(grid)

    if not found_something:
        return True, grid

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            solved, new_grid = solve(grid.copy())
            if solved:

                return True, new_grid

            grid[row][col] = 0

    return False, None


def check_if_correct(solved1, solved2):
    for i in range(9):
        for j in range(9):
            if solved1[i][j] != solved2[i][j]:
                return False
    return True


if __name__ == "__main__":
    solved_puzzle, puzzle = create_puzzle()
    solved, backtracked_puzzle = solve(puzzle)
    print(backtracked_puzzle) if solved else print('Impossible')
    print('the solutions match') if check_if_correct(backtracked_puzzle,
                                                     solved_puzzle) else print('They dont match! Multiple soltions!???')
