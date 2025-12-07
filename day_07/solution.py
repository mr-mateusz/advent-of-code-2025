from functools import cache


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


def find_first_splitter(data: tuple[tuple[str]], start: tuple[int, int]) -> tuple[int, int] | None:
    start_row_idx = start[0]
    start_col_idx = start[1]
    n_rows = len(data)
    for row_idx in range(start_row_idx, n_rows):
        if data[row_idx][start_col_idx] == '^':
            return row_idx, start_col_idx
    return None


@cache
def run_simulation_quantum(data: tuple[tuple[str]], start: tuple[int, int]) -> int:
    splitter_pos = find_first_splitter(data, start)

    if not splitter_pos:
        return 1
    else:
        start_1 = splitter_pos[0], splitter_pos[1] - 1
        start_2 = splitter_pos[0], splitter_pos[1] + 1
        return run_simulation_quantum(data, start_1) + run_simulation_quantum(data, start_2)


if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        data = [list(l.strip()) for l in f.readlines()]

    start = find_start(data)

    # part 1
    print(run_simulation(data, start))

    data = tuple(tuple(row) for row in data)

    # part 2
    print(run_simulation_quantum(data, start))
