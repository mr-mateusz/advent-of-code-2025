from math import prod

if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]

    numbers = lines[:-1]
    operations = lines[-1].split()

    numbers = [list(map(int, line.split())) for line in numbers]

    numbers = list(zip(*numbers))

    operation_map = {
        '+': sum,
        '*': prod
    }

    total_sum = 0
    for operation, col in zip(operations, numbers):
        total_sum += operation_map[operation](col)

    # Part 1
    print(total_sum)

    # The input is not padded to the right with spaces, so we need to add this padding
    longest_row = max(len(l) for l in lines)

    for i in range(len(lines)):
        lines[i] = lines[i] + ' ' * (longest_row - len(lines[i]))

    # Transpose input (we still work on the individual characters, not "numbers")
    # We will actually go from left to right, but it does not matter. Digit significance will be preserved and
    # it will be easier to take operation sign
    transposed = [''.join(l) for l in zip(*lines)]

    operation = None
    total_sum = 0
    operation_res = None
    for row in transposed:
        row = row.strip()
        if not row:
            # Empty line (column) - new set of numbers
            total_sum += operation_res
            operation = None
            operation_res = None
            continue
        if not operation:
            # Operation not initialized - first number in this set of numbers - contains operation sign at the end
            value, operation = row[:-1], row[-1]
            value = int(value)
            operation_res = 0 if operation == '+' else 1
            operation = operation_map[operation]
        else:
            # Just a number
            value = int(row)
        operation_res = operation([operation_res, value])
    if operation_res is not None:
        total_sum += operation_res

    # Part 2
    print(total_sum)
