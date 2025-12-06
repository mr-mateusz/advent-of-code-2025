from math import prod

if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = lines[:-1]
    operations = lines[-1].split()

    numbers = [list(map(int, line.split())) for line in numbers]

    numbers = list(zip(*numbers))

    total_sum = 0
    for operation, col in zip(operations, numbers):
        if operation == '+':
            res = sum(col)
        else:  # *
            res = prod(col)
        total_sum += res

    print(total_sum)
