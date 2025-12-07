def find_start(data: list[list[str]]) -> tuple[int, int]:
    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            if value == 'S':
                return row_idx, col_idx
    raise ValueError('Starting point not found')


def run_simulation(data: list[list[str]], start: tuple[int, int]) -> int:
    beam_positions = [start]

    n_splits = 0
    while beam_positions:
        next_beam_positions = set()
        for bp in beam_positions:
            next_bp = (bp[0] + 1, bp[1])
            try:
                next_location = data[next_bp[0]][next_bp[1]]
            except IndexError:
                continue
            if next_location == "^":
                n_splits += 1
                next_beam_positions.add((next_bp[0], next_bp[1] - 1))
                next_beam_positions.add((next_bp[0], next_bp[1] + 1))
            else:
                next_beam_positions.add(next_bp)
        beam_positions = list(next_beam_positions)

    return n_splits


if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        data = [list(l.strip()) for l in f.readlines()]

    start = find_start(data)

    # part 1
    print(run_simulation(data, start))
