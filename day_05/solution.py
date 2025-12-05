from typing import Sequence


def in_any_range(ranges: Sequence[tuple[int, int]], value: int) -> bool:
    for _range in ranges:
        if _range[0] <= value <= _range[1]:
            return True
    return False

def ids_in_range(ranges: Sequence[tuple[int, int]], ids: Sequence[int]) -> list[int]:
    in_range = []
    for _id in ids:
        if in_any_range(ranges, _id):
            in_range.append(_id)
    return in_range

if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        data = f.read()

    id_ranges, ids = data.split('\n\n')
    id_ranges = id_ranges.split('\n')
    id_ranges = [tuple(map(int, l.split('-'))) for l in id_ranges]

    ids = ids.strip().split('\n')
    ids = list(map(int, ids))

    # Part 1
    print(len(ids_in_range(id_ranges, ids)))