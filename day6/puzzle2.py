import numpy as np
from itertools import zip_longest
import re


def parse_problems(path):
    with open(path, 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    numeric_columns = list(zip_longest(*lines[:-1], fillvalue=' '))

    problem = []
    all_problems = []
    for i, column in enumerate(numeric_columns):
        # Check if all elements in column are whitespace
        if all(char == ' ' for char in column):
            all_problems.append(problem)
            problem = []
        else:
            number = ''.join(column).strip()
            problem.append(int(number))

    all_problems.append(problem)
    np_numbers = np.array(list(zip_longest(*all_problems, fillvalue=np.nan))).T

    operators = []
    for op in re.findall(r'\+|\*', lines[-1]):
        operators.append(op)

    return np_numbers, operators


def puzzle_2(problems, operators) -> int:
    sum = 0
    n_problems = len(operators)

    for i in range(n_problems):
        if operators[i] == '+':
            sum += np.nansum(problems[i, :])
        elif operators[i] == '*':
            sum += np.nanprod(problems[i, :])

    return sum


if __name__ == '__main__':
    #problems, operators = parse_problems('day6_exampleinput.txt')
    problems, operators = parse_problems('day6_input.txt')

    sum = puzzle_2(problems, operators)
    print(f'Grand total: {sum}')
