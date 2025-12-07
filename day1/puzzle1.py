import pandas as pd


def puzzle_1(rotations: list) -> int:
    zero_counter = 0
    position = 50

    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])

        if direction == 'R':
            position += steps
            while position > 99:
                position -= 100
        else:
            position -= steps
            while position < 0:
                position += 100

        if position == 0:
            zero_counter += 1

    return zero_counter


if __name__ == '__main__':
    rotations = pd.read_csv('puzzle1_input.csv', header=None).to_numpy()[:, 0]
    # rotations = pd.read_csv('puzzle1_example.csv', header=None).to_numpy()[:, 0]

    password = puzzle_1(rotations)
    print(f'Password: {password}')
