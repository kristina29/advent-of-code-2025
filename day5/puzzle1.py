import pandas as pd
import numpy as np
import csv


def convert_input(path):
    files = open(path).read().split('\n\n')
    fresh_id_ranges = files[0].strip().splitlines()
    available_ids = list(map(int, files[1].strip().splitlines()))

    return fresh_id_ranges, available_ids


def puzzle_1(fresh_id_ranges, available_ids) -> int:
    parsed_ranges = []
    for id_range in fresh_id_ranges:
        start, stop = map(int, id_range.split('-'))
        parsed_ranges.append((start, stop))

    counter = 0
    for available_id in available_ids:
        for start, stop in parsed_ranges:
            if start <= available_id <= stop:
                counter += 1
                break

    return counter


if __name__ == '__main__':
    #fresh_id_ranges, available_ids = convert_input('day5_exampleinput.csv')
    fresh_id_ranges, available_ids = convert_input('day5_input.csv')

    counter = puzzle_1(fresh_id_ranges, available_ids)
    print(f'Fresh and available ids: {counter}')
