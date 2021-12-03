#!/usr/bin/env python3

def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
        lines = text.split("\n")
        split_lines = [line.split(" ") for line in lines]
    return [(direct, int(i)) for direct, i in split_lines]


def find_location(moves):
    depth = 0
    horiz = 0
    for move in moves:
        if move[0] == 'forward':
            horiz += move[1]
        elif move[0] == 'down':
            depth += move[1]
        elif move[0] == 'up':
            depth -= move[1]

    return (depth, horiz)


if __name__ == "__main__":
    instructions = parse_input("input")
    pair = find_location(instructions)
    print(pair[0] * pair[1])

    test = parse_input("test")
    pair = find_location(test)
    assert(pair[0]*pair[1] == 150)
