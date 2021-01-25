#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    return text.split("\n")


def flip(instructions):
    map = {}

    for inst in instructions:
        line = 0
        col = 0
        i = 0
        while i < len(inst):
            if col % 2 == 0:
                if inst[i] == 'e':
                    line += 1
                elif inst[i] == 'w':
                    line -= 1
                elif inst[i:i+2] == "ne":
                    col += 1
                    i += 1
                elif inst[i:i+2] == "nw":
                    line -= 1
                    col += 1
                    i += 1
                elif inst[i:i+2] == "se":
                    col -= 1
                    i += 1
                elif inst[i:i+2] == "sw":
                    line -= 1
                    col -= 1
                    i += 1
            else:
                if inst[i] == 'e':
                    line += 1
                elif inst[i] == 'w':
                    line -= 1
                elif inst[i:i+2] == "ne":
                    col += 1
                    line += 1
                    i += 1
                elif inst[i:i+2] == "nw":
                    col += 1
                    i += 1
                elif inst[i:i+2] == "se":
                    col -= 1
                    line += 1
                    i += 1
                elif inst[i:i+2] == "sw":
                    col -= 1
                    i += 1
            i += 1

        if (line, col) in map.keys():
            map[(line, col)] = not map[(line, col)]
        else:
            map[(line, col)] = False
    return map


if __name__ == "__main__":
    instructions = parse_input()
    map = flip(instructions)
    print(map.values())
    print(sum([1 for i in map.values() if not i]))
