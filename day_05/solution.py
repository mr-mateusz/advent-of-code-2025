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


def compact_ranges(ranges: Sequence[tuple[int, int]]) -> list[tuple]:
    ranges_to_compact = list(ranges)
    compacted_ranges = []

    while ranges_to_compact:
        candidate_1 = ranges_to_compact.pop()
        for candidate_2 in compacted_ranges:
            if candidate_1[0] <= candidate_2[0] <= candidate_1[1]:
                merged_candidate = (candidate_1[0], max(candidate_1[1], candidate_2[1]))
                compacted_ranges.remove(candidate_2)
                ranges_to_compact.append(merged_candidate)
                break
            if candidate_2[0] <= candidate_1[0] <= candidate_2[1]:
                merged_candidate = (candidate_2[0], max(candidate_1[1], candidate_2[1]))
                compacted_ranges.remove(candidate_2)
                ranges_to_compact.append(merged_candidate)
                break
        else:
            compacted_ranges.append(candidate_1)
    return compacted_ranges


def fresh_ids_count(ranges: Sequence[tuple[int, int]]) -> int:
    compacted_ranges = compact_ranges(ranges)

    total = 0
    for lb, ub in compacted_ranges:
        total += ub - lb + 1
    return total


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

    # part 2
    print(fresh_ids_count(id_ranges))
