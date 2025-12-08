import pandas as pd
import numpy as np


def load_grid(path):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    return np.array([list(line) for line in lines], dtype='str')


def get_adjacent_values(position, grid):
    row, col = position
    n_rows, n_cols = np.shape(grid)

    adjacent_values = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i <= (n_rows-1) and 0 <= j <= (n_cols-1) and not (i == row and j == col):
                adjacent_values.append(grid[i,j])

    return adjacent_values

def puzzle_1(grid) -> int:
    counter = 0

    # Convert grid into boolean grid
    grid = (grid == '@')

    for position, value in np.ndenumerate(grid):
        if value:
            adjacent_values = get_adjacent_values(position, grid)
            if sum(adjacent_values) < 4:
                counter += 1

    return counter


if __name__ == '__main__':
    #grid = load_grid('day4_exampleinput.txt')
    grid = load_grid('day4_input.txt')

    counter = puzzle_1(grid)
    print(f'Accessible rolls: {counter}')
