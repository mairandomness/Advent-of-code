#this is just baaaad, but i really wanted to do a recursive version of the solution

import sys
TOTAL_D = 10000

sys.setrecursionlimit(1500000)


def parse_input():
    with open("input", "r") as f:
        text = f.read()
    lines = text.split("\n")
    lines = [line.split(", ") for line in lines]
    coords = [(int(a), int(b)) for [a, b] in lines]
    return coords


def get_coord_to_check(coords):
    for coord in coords:
        if within_bounds(coord, coords):
            return coord
    return None


def count_points(coords):
    coord_to_check = get_coord_to_check(coords)
    grid = [coord_to_check]

    return sum(populate_neighbors(coord_to_check, grid, coords, [1]))


def neighbors(point):
    (x, y) = point
    neighbors = [(x + a, y + b) for a in [0, 1, -1]
                 for b in [0, 1, -1] if (a, b) != (0, 0)]
    return neighbors


def populate_neighbors(point, grid, coords, count):
    #print(sum(count))
    possible_n = neighbors(point)

    for n in possible_n:
        new_neighbor = False
        if n not in grid:
            count.append(within_bounds(n, coords))
            grid.append(n)
            new_neighbor = True
            if within_bounds(n, coords) and new_neighbor:
                populate_neighbors(n, grid, coords, count)
    return count


def distance(point_A, point_B):
    (a, b) = point_A
    (c, d) = point_B
    return abs(a - c) + abs(b - d)


def within_bounds(point, coords):
    dist = 0
    for coord in coords:
        dist += distance(coord, point)
        if dist >= TOTAL_D:
            break
    if dist < TOTAL_D:
        return 1
    else:
        return 0


def main():
    coords = parse_input()
    #print(count_points(coords))


if __name__ == "__main__":
    main()
