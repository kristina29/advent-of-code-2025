
def puzzle_2(path):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f]

    max_index = len(lines[0])
    beam_positions = {lines[0].index('S')}

    prev_numeric = [0] * max_index
    prev_numeric[next(iter(beam_positions))] = 1

    for line in lines[1:]:
        new_numeric = [0] * max_index
        new_beams = set()

        for beam in beam_positions:
            if line[beam] == '^':
                # Split beam
                if beam > 0:
                    new_numeric[beam-1] = new_numeric[beam-1] + prev_numeric[beam]
                    new_beams.add(beam - 1)
                if beam < max_index:
                    new_numeric[beam+1] = new_numeric[beam+1] + prev_numeric[beam]
                    new_beams.add(beam + 1)
                new_numeric[beam] = 0
            else:
                new_numeric[beam] = new_numeric[beam] + prev_numeric[beam]
                new_beams.add(beam)

        beam_positions = new_beams
        prev_numeric = new_numeric

    return sum(new_numeric)


if __name__ == '__main__':
    #split_counter = puzzle_2('day7_exampleinput.txt')
    split_counter = puzzle_2('day7_input.txt')

    print('Split counter:', split_counter)