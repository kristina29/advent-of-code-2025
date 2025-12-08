import pandas as pd
import numpy as np


def puzzle_2(banks: list) -> int:
    volt_sum = 0
    for bank in banks:
        batteries = np.fromiter(bank, dtype=np.int64)

        volt = ''
        for i in range(12, 0, -1):
            if i == 1:
                # Final battery
                max_index = np.argmax(batteries)
                volt += str(batteries[max_index])
            else:
                max_index = np.argmax(batteries[:-(i-1)])
                volt += str(batteries[max_index])
                batteries = batteries[max_index+1:]

        volt_sum += int(volt)

    return volt_sum


if __name__ == '__main__':
    #banks = pd.read_csv('day3_exampleinput.csv', header=None, dtype=str).to_numpy()[:,0]
    banks = pd.read_csv('day3_input.csv', header=None, dtype=str).to_numpy()[:, 0]

    sum = puzzle_2(banks)
    print(f'Sum: {sum}')
