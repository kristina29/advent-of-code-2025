
def puzzle_1(path):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f]

    max_index = len(lines[0])
    beam_positions = [lines[0].index('S')]
    split_counter = 0

    for line in lines[1:]:
        to_remove = []
        to_add = set()
        for beam in beam_positions:
            if line[beam] == '^':
                # Split beam
                split_counter += 1
                to_remove.append(beam)
                if beam > 0:
                    to_add.add(beam-1)
                if beam < max_index:
                    to_add.add(beam+1)

        beam_positions = list(set(beam_positions) - set(to_remove))
        beam_positions.extend(to_add)

    return split_counter


if __name__ == '__main__':
    #split_counter = puzzle_1('day7_exampleinput.txt')
    split_counter = puzzle_1('day7_input.txt')

    print('Split counter:', split_counter)