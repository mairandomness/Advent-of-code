#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
        lines = text.split("\n")
    return lines


def go_through_forest(map, r, d):
    count = 0
    x = 0
    y = 0
    while y + d < len(map):
        x += r
        y += d
        x %= len(map[y])
        if map[y][x] == '#':
            count += 1
    return count


if __name__ == "__main__":
    map = parse_input()
    print(go_through_forest(map, 1, 1) * go_through_forest(map, 3, 1) *
          go_through_forest(map, 5, 1) * go_through_forest(map, 7, 1) * go_through_forest(map, 1, 2))
