import pandas as pd
import numpy as np
import csv


def convert_input(path):
    files = open(path).read().split('\n\n')
    fresh_id_ranges = files[0].strip().splitlines()
    available_ids = list(map(int, files[1].strip().splitlines()))

    return fresh_id_ranges, available_ids


def puzzle_2(fresh_id_ranges) -> int:
    id_ranges = []
    for id_range in fresh_id_ranges:
        start, stop = map(int, id_range.split('-'))
        id_ranges.append((start, stop))
    id_ranges = sorted(id_ranges)

    counter = 0
    current_min, current_max = id_ranges[0]

    for start, stop in id_ranges[1:]:
        # Check if within previous range
        if start <= current_max:
            current_max = max(current_max, stop)
        else:
            count_ids = current_max - current_min + 1
            counter += count_ids
            current_min, current_max = start, stop

    # Final range
    count_ids = current_max - current_min + 1
    counter += count_ids

    return counter


if __name__ == '__main__':
    #fresh_id_ranges, _ = convert_input('day5_exampleinput.csv')
    fresh_id_ranges, _ = convert_input('day5_input.csv')

    counter = puzzle_2(fresh_id_ranges)
    print(f'Fresh ids: {counter}')
