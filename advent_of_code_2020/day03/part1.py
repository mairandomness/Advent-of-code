#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
        lines = text.split("\n")
    return lines


def go_through_forest(map):
    x = 0
    count = 0
    for line in map[1:]:
        x += 3
        x %= len(line)
        if line[x] == '#':
            count += 1
    return count


if __name__ == "__main__":
    map = parse_input()
    print(go_through_forest(map))
