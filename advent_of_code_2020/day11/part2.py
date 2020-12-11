#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    seats = text.split("\n")
    return seats


def sees_dict(map):
    sees = {}
    for y, line in enumerate(map):
        for x, seat in enumerate(line):
            if seat == 'L':
                sees[(y, x)] = []
                directions = [(a,  b) for a in [0, 1, -1]
                              for b in [0, 1, -1] if (a, b) != (0, 0)]
                for a, b in directions:
                    i = 1
                    while y + i*a >= 0 and y + i*a < len(map) and x+i*b >= 0 and x+i*b < len(line):
                        if map[y+i*a][x+i*b] == 'L':
                            sees[(y, x)].append((y+i*a, x+i*b))
                            break
                        i += 1
    return sees


def update(map, sees_dict):
    changes = 0
    new_map = []
    for y, line in enumerate(map):
        new_line = []
        for x, seat in enumerate(line):
            if seat == 'L':
                occupied = sum(
                    [1 for b, a in sees_dict[(y, x)] if map[b][a] == '#'])
                if occupied == 0:
                    changes += 1
                    new_line.append('#')
                else:
                    new_line.append('L')

            elif seat == '#':
                occupied = sum(
                    [1 for b, a in sees_dict[(y, x)] if map[b][a] == '#'])
                if occupied < 5:
                    new_line.append('#')
                else:
                    changes += 1
                    new_line.append('L')
            else:
                new_line.append(".")
        new_map.append(new_line)
    return(new_map, changes)


if __name__ == "__main__":
    map = parse_input()
    changes = 1
    sees_dict = sees_dict(map)
    while changes != 0:
        map, changes = update(map, sees_dict)
    print(sum([sum([1 for char in line if char == '#']) for line in map]))
