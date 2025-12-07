import pandas as pd


def puzzle_1(id_ranges: list) -> int:
    invalid_sum = 0
    for r in id_ranges:
        start, end = r.split('-')
        start, end = int(start), int(end)
        for i in range(start, end+1):
            s = str(i)
            n = len(s)

            # Uneven length, cannot be repeated twice
            if n % 2 != 0:
                continue

            split = int(n/2)
            # Split in half
            first = s[:split]
            second = s[split:]

            if first == second:
                invalid_sum += i

    return invalid_sum


if __name__ == '__main__':
    #id_ranges = pd.read_csv('puzzle1_example.csv', header=None, sep=',').to_numpy()[0]
    id_ranges = pd.read_csv('puzzle1_input.csv', header=None, sep=',').to_numpy()[0]

    sum = puzzle_1(id_ranges)
    print(f'Sum of invalid IDs: {sum}')
