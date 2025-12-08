import numpy as np
import re


def parse_problems(path):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f]

    numbers_complete = []
    for line in lines[:-1]:
        numbers = re.findall(r'\d+', line)
        numbers_complete.append([int(n) for n in numbers])
    np_numbers = np.array(numbers_complete)

    operators = []
    for op in re.findall(r'\+|\*', lines[-1]):
        operators.append(op)

    return np_numbers, operators


def puzzle_1(problems, operators) -> int:
    sum = 0
    n_problems = len(operators)

    for i in range(n_problems):
        if operators[i] == '+':
            sum += np.sum(problems[:,i])
        elif operators[i] == '*':
            sum += np.prod(problems[:,i])

    return sum


if __name__ == '__main__':
    #problems, operators = parse_problems('day6_exampleinput.txt')
    problems, operators = parse_problems('day6_input.txt')

    sum = puzzle_1(problems, operators)
    print(f'Grand total: {sum}')
