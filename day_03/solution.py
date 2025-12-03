from typing import Sequence


def find_largest_joltage(line: Sequence[int]) -> int:
    first_digit = max(line[:-1])
    first_digit_pos = line.index(first_digit)

    second_digit = max(line[first_digit_pos + 1:])

    return first_digit * 10 + second_digit


if __name__ == '__main__':
    path = 'input.txt'

    total_joltage = 0
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            line = list(map(int, line))

            total_joltage += find_largest_joltage(line)

    # Part 1
    print(total_joltage)
