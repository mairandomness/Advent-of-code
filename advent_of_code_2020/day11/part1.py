#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    seats = text.split("\n")
    return seats


def update(map):
    changes = 0
    new_map = []
    for y, line in enumerate(map):
        new_line = []
        for x, seat in enumerate(line):
            if seat == 'L':
                adjacent = [(y + a, x + b) for a in [0, 1, -1] for b in [0, 1, -1] if (a, b) != (
                    0, 0) and y + a >= 0 and y + a < len(map) and x+b >= 0 and x+b < len(line)]
                occupied = len([map[b][a]
                                for b, a in adjacent if map[b][a] == '#'])
                if occupied == 0:
                    changes += 1
                    new_line.append('#')
                else:
                    new_line.append('L')
            elif seat == '#':
                adjacent = [(y + a, x + b) for a in [0, 1, -1] for b in [0, 1, -1] if (a, b) != (
                    0, 0) and y + a >= 0 and y + a < len(map) and x+b >= 0 and x+b < len(line)]
                occupied = len([map[b][a]
                                for b, a in adjacent if map[b][a] == '#'])
                if occupied >= 4:
                    changes += 1
                    new_line.append('L')
                else:
                    new_line.append('#')
            else:
                new_line.append(".")
        new_map.append(new_line)
    return(new_map, changes)


if __name__ == "__main__":
    map = parse_input()
    changes = 1
    while changes != 0:
        map, changes = update(map)
    print(sum([sum([1 for char in line if char == '#']) for line in map]))
