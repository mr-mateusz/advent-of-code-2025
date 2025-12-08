import math


def euclidean_distance(box_1: tuple, box_2: tuple) -> float:
    return math.sqrt(sum((pb1 - pb2) ** 2 for pb1, pb2 in zip(box_1, box_2)))


def calculate_distances(boxes: list[tuple]) -> list[tuple[set, float]]:
    distances = []
    for box_1_index, box_1 in enumerate(boxes):
        for box_2 in boxes[box_1_index + 1:]:
            distances.append(({box_1, box_2}, euclidean_distance(box_1, box_2)))
    return distances


def find_circuit(box: tuple, circuits: list[set[tuple]]):
    for circuit in circuits:
        if box in circuit:
            return circuit
    raise ValueError(f'Circuit not found for box {box}')


def connect_boxes(circuits: list[set[tuple]], distances: list[tuple[set, float]]) -> list[set[tuple]]:
    circuits = circuits[:]
    distances = distances[:]

    for boxes, _ in distances:
        box_1, box_2 = boxes
        box_1_circuit = find_circuit(box_1, circuits)
        box_2_circuit = find_circuit(box_2, circuits)
        if box_1_circuit == box_2_circuit:
            continue
        circuits.remove(box_1_circuit)
        circuits.remove(box_2_circuit)
        circuits.append(box_1_circuit.union(box_2_circuit))

    return circuits


if __name__ == '__main__':
    path = 'input.txt'

    boxes_to_connect = 1000

    with open(path, 'r') as f:
        data = [tuple(map(int, l.strip().split(','))) for l in f.readlines()]

    circuits = [{box} for box in data]

    distances = calculate_distances(data)
    distances.sort(key=lambda x: x[1])

    circuits_connected = connect_boxes(circuits, distances[:boxes_to_connect])

    circuits_connected.sort(key=len, reverse=True)

    top_3_sizes = [len(x) for x in circuits_connected[:3]]

    result = math.prod(top_3_sizes)

    print(result)
