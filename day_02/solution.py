# Should be better than brute force
def find_invalid_ids(lb: int, ub: int) -> list[int]:
    l_str = str(lb)
    mid = len(l_str) // 2
    if len(l_str) % 2:
        first_part = '1' + '0' * mid
    else:
        first_part = l_str[:mid]

    invalid_ids = []
    while True:
        id_to_check = int(first_part + first_part)
        if id_to_check <= ub:
            if lb <= id_to_check:
                invalid_ids.append(id_to_check)
        else:
            break
        first_part = str(int(first_part) + 1)
    return invalid_ids


if __name__ == '__main__':
    path = 'input.txt'

    with open(path, 'r') as f:
        data = f.read().strip()

    id_ranges = [r.split('-') for r in data.split(',')]
    id_ranges = [[int(lb), int(ub)] for lb, ub in id_ranges]

    invalid_ids_sum = 0
    for id_range in id_ranges:
        invalid_ids_sum += sum(find_invalid_ids(*id_range))

    # Part 1
    print(invalid_ids_sum)
