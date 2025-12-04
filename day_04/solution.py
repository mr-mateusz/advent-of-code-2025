def neighbouring_rolls(pos: tuple[int, int], diagram: list[list[str]]) -> int:
    row_num, col_num = pos

    max_row = len(diagram)
    max_col = len(diagram[0])

    n_rolls = 0
    for row_diff in [-1, 0, 1]:
        for col_diff in [-1, 0, 1]:
            if row_diff == 0 and col_diff == 0:
                continue
            nghb_row = row_num + row_diff
            nghb_col = col_num + col_diff

            if not 0 <= nghb_row < max_row or not 0 <= nghb_col < max_col:
                continue

            if diagram[nghb_row][nghb_col] == '@':
                n_rolls += 1
    return n_rolls


def accessible_rolls_iteration(diagram: list[list[str]]) -> list[tuple[int, int]]:
    ars = []
    for row_num, row in enumerate(diagram):
        for col_num, value in enumerate(row):
            if value == '@' and neighbouring_rolls((row_num, col_num), diagram) < 4:
                ars.append((row_num, col_num))
    return ars


def accessible_rolls_total_num(diagram: list[list[str]]) -> int:
    diagram = [r[:] for r in diagram]

    arn = 0
    while True:
        ars = accessible_rolls_iteration(diagram)
        if not ars:
            return arn

        arn += len(ars)
        for ar in ars:
            diagram[ar[0]][ar[1]] = '.'


if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        data = [list(l.strip()) for l in f.readlines()]

    # Part 1
    print(len(accessible_rolls_iteration(data)))

    # Part 2
    print(accessible_rolls_total_num(data))
