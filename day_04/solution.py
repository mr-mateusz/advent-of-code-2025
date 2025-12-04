def neighbouring_rolls(pos: tuple[int, int], diagram: list[str]) -> int:
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


def accessible_rolls_num(diagram: list[str]) -> int:
    arn = 0
    for row_num, row in enumerate(diagram):
        for col_num, value in enumerate(row):
            if value == '@' and neighbouring_rolls((row_num, col_num), diagram) < 4:
                arn += 1
    return arn


if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        data = [l.strip() for l in f.readlines()]

    # Part 1
    print(accessible_rolls_num(data))
