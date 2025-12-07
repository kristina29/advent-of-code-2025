import pandas as pd


def is_invalid(id, seq_length):
    n = len(id)
    if n % seq_length != 0:
        return False

    part = id[:seq_length]
    # Check if the part in id length is the id
    return part * (n // seq_length) == id


def puzzle_2(id_ranges: list) -> int:
    invalid_ids = set()
    for r in id_ranges:
        start, end = r.split('-')
        start, end = int(start), int(end)

        for i in range(start, end+1):
            s = str(i)
            n = len(s)

            for seq_length in range(1, n//2 + 1):
                if is_invalid(s, seq_length):
                    invalid_ids.add(i)
                    break
                seq_length += 1

    return sum(invalid_ids)


if __name__ == '__main__':
    #id_ranges = pd.read_csv('puzzle1_example.csv', header=None, sep=',').to_numpy()[0]
    id_ranges = pd.read_csv('puzzle1_input.csv', header=None, sep=',').to_numpy()[0]

    sum = puzzle_2(id_ranges)
    print(f'Sum of invalid IDs: {sum}')
