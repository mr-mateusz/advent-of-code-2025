def turn_dial(state: int, rotation: str) -> int:
    lb = 0
    ub = 99
    if not lb <= state <= ub:
        raise ValueError()

    if len(rotation) < 2:
        raise ValueError()

    direction = rotation[0]
    if direction not in ['L', 'R']:
        raise ValueError()

    distance = int(rotation[1:])

    if direction == 'L':
        state -= distance
        while state < lb:
            state += ub + 1
        return state

    state += distance
    while state > ub:
        state -= ub + 1
    return state


if __name__ == '__main__':
    path = 'input.txt'

    state = 50
    zero_cnt = 0

    with open(path, 'r') as f:
        for line in f:
            state = turn_dial(state, line.strip())
            if state == 0:
                zero_cnt += 1

    # Part 1
    print(zero_cnt)
