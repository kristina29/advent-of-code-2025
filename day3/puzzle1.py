import pandas as pd
import numpy as np


def puzzle_1(banks: list) -> int:
    volt_sum = 0
    for bank in banks:
        batteries = np.fromiter(bank, dtype=np.int64)
        first_index = np.argmax(batteries)
        next_batteries = batteries[first_index+1:]

        if len(next_batteries) == 0:
            second_index = first_index
            second_value = batteries[second_index]
            temp_batteries = batteries
            temp_batteries[first_index] = 0
            first_index = np.argmax(temp_batteries)
        else:
            second_index = np.argmax(next_batteries) + first_index + 1
            second_value = batteries[second_index]

        first_value = batteries[first_index]
        max_volt = int(f'{first_value}{second_value}')
        volt_sum += max_volt

    return volt_sum


if __name__ == '__main__':
    #banks = pd.read_csv('day3_exampleinput.csv', header=None, dtype=str).to_numpy()[:,0]
    banks = pd.read_csv('day3_input.csv', header=None, dtype=str).to_numpy()[:, 0]

    sum = puzzle_1(banks)
    print(f'Sum: {sum}')
