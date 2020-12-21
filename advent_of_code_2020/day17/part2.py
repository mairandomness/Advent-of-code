#!/usr/bin/env python3


def parse_input():
    with open("input", "r") as f:
        text = f.read().split("\n")
    map = {}
    for y, line in enumerate(text):
        for x, char in enumerate(line):
            if char == '#':
                map[(x, y, 0, 0)] = 1
            else:
                map[(x, y, 0, 0)] = 0
    return map


def neighbors(point):
    x, y, z, w = point
    diffs = [(dx, dy, dz, dw) for dx in range(-1, 2) for dy in range(-1, 2) for dz in range(-1, 2)
             for dw in range(-1, 2) if (dx != 0 or dy != 0 or dz != 0 or dw != 0)]
    neighbors = [(x + dx, y + dy, z + dz, w + dw) for dx, dy, dz, dw in diffs]
    return neighbors


def run_cycle(map):
    new_map = {}
    queue = []

    for point in map.keys():
        neighboring_points = neighbors(point)
        active = 0

        for neighbor in neighboring_points:
            if neighbor not in map.keys():
                queue.append(neighbor)
            else:
                active += map[neighbor]

        new_map[point] = get_value(map[point], active)

    for point in queue:
        active = sum([map.get(neighbor, 0) for neighbor in neighbors(point)])
        new_map[point] = get_value(0, active)

    return new_map


def get_value(map_point, active):
    if map_point and (active == 2 or active == 3):
        return 1
    elif map_point:
        return 0
    elif not map_point and active == 3:
        return 1
    else:
        return 0


if __name__ == "__main__":
    map = parse_input()
    for i in range(6):
        map = run_cycle(map)
    print(sum(map.values()))
