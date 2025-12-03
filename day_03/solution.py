from typing import Sequence


def find_largest_joltage(line: Sequence[int], num_batteries: int) -> int:
    if len(line) < num_batteries:
        raise ValueError

    start = 0
    remaining_batteries = num_batteries

    digits = []
    while remaining_batteries:
        end = remaining_batteries - 1
        digit = max(line[start:len(line) - end])
        digit_pos = start + line[start:].index(digit)

        digits.append(digit)

        start = digit_pos + 1
        remaining_batteries -= 1

    return int(''.join(map(str, digits)))


if __name__ == '__main__':
    path = 'input.txt'

    total_joltage_2 = 0
    total_joltage_12 = 0
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            line = list(map(int, line))

            total_joltage_2 += find_largest_joltage(line, 2)
            total_joltage_12 += find_largest_joltage(line, 12)

    # Part 1
    print(total_joltage_2)

    # Part 2
    print(total_joltage_12)
