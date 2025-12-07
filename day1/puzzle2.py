import pandas as pd


def puzzle2(rotations: list) -> int:
    zero_counter = 0
    position = 50
    prev_position = position

    for rotation in rotations:
        direction = rotation[0]
        whole_turns, steps = divmod(int(rotation[1:]), 100)

        if direction == 'R':
            position += steps
        else:
            position -= steps

        if prev_position != 0 and not (0 < position <= 99):
            zero_counter += 1

        zero_counter += whole_turns
        position = position % 100
        prev_position = position

    return zero_counter


if __name__ == '__main__':
    rotations = pd.read_csv('puzzle1_input.csv', header=None).to_numpy()[:, 0]
    #rotations = pd.read_csv('puzzle1_example.csv', header=None).to_numpy()[:, 0]

    password = puzzle2(rotations)
    print(f'Password: {password}')
