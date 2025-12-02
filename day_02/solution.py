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


def find_invalid_ids_p2(lb: int, ub: int) -> list[int]:
    # lengths of repeated sequences we will be looking for
    min_seq_len = 1
    max_seq_len = len(str(ub)) // 2

    # min and max number of digits in an id
    min_n_digits = len(str(lb))
    max_n_digits = len(str(ub))

    # Now it needs to be a set, because 1111 can be derived from 1 1 1 1 and 11 11
    invalid_ids = set()
    for seq_len in range(min_seq_len, max_seq_len + 1):
        for seq in range(10 ** (seq_len - 1), 10 ** seq_len):
            id_to_check = str(seq) + str(seq)
            while len(id_to_check) < min_n_digits:
                id_to_check += str(seq)
            while len(id_to_check) <= max_n_digits:
                if lb <= int(id_to_check) <= ub:
                    invalid_ids.add(int(id_to_check))
                id_to_check += str(seq)
    return list(invalid_ids)


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

    invalid_ids_sum = 0
    for id_range in id_ranges:
        invalid_ids_sum += sum(find_invalid_ids_p2(*id_range))

    # Part 2
    print(invalid_ids_sum)
