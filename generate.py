from pprint import pprint as print
from random import randint
import os


def clear(): return os.system('clear')


def applies_to_rules(grid):
    for i in range(9):
        row = grid[i]
        non_zero = list(filter(lambda x: x != 0, row))
        if len(non_zero) != len(set(non_zero)):
            print('row incorrect')
            return False

    for i in range(9):
        col = [grid[j][i] for j in range(9)]
        non_zero = list(filter(lambda x: x != 0, col))
        if len(non_zero) != len(set(non_zero)):
            print('col incorrect')
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            quarter = [grid[i1][j1] for j1 in range(
                i, i + 3) for i1 in range(j, j + 3) if grid[i1][j1] != 0]
            if len(quarter) != len(set(quarter)):
                print('quarter incorrect')
                return False

    return True


def create_puzzle():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        j = 0
        while j < 9:
            grid[i][j] = randint(1, 9)
            n = 0
            while not applies_to_rules(grid) and n < 20:
                grid[i][j] = randint(1, 9)
                clear()
                print(grid)
                n += 1
            else:
                if n >= 20:
                    grid[i][j] = 0
                    for p in range(9):
                        grid[i][p] = 0
                    j = -1
            j += 1
    return grid, make_it_a_puzzle(grid)


def make_it_a_puzzle(grid):
    puzzle_size = 81
    remaining = 20

    while puzzle_size > remaining:
        i = randint(0, 8)
        j = randint(0, 8)
        grid[i][j] = 0
        puzzle_size -= 1

    return grid


if __name__ == "__main__":
    solved_puzzle, puzzle = create_puzzle()
    print((solved_puzzle, puzzle))
