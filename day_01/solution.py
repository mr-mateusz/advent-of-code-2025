def turn_dial(initial_state: int, rotation: str) -> tuple[int, int]:
    lb = 0
    ub = 99
    if not lb <= initial_state <= ub:
        raise ValueError()

    if len(rotation) < 2:
        raise ValueError()

    direction = rotation[0]
    if direction not in ['L', 'R']:
        raise ValueError()

    distance = int(rotation[1:])

    zero_clicks = 0
    state = initial_state

    if direction == 'L':
        state -= distance
        while state < lb:
            state += ub + 1
            zero_clicks += 1
        if state == 0:
            zero_clicks += 1
        if initial_state == 0:
            zero_clicks -= 1
        return state, zero_clicks

    state += distance
    while state > ub:
        state -= ub + 1
        zero_clicks += 1
    return state, zero_clicks


if __name__ == '__main__':
    path = 'input.txt'

    state = 50
    zero_cnt = 0
    total_zero_clicks = 0

    with open(path, 'r') as f:
        for line in f:
            state, zero_clicks = turn_dial(state, line.strip())
            if state == 0:
                zero_cnt += 1
            total_zero_clicks += zero_clicks

    # Part 1
    print(zero_cnt)

    # Part 2
    print(total_zero_clicks)
