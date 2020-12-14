#!/usr/bin/env python3

import numpy as np


def parse_input():
    with open("input", "r") as f:
        text = f.read().split("\n")
    directions = [line.split(" = ") for line in text]
    return directions


def run_directions(directions):
    mem = {}
    mask = ""

    for dir in directions:
        if dir[0] == "mask":
            mask = dir[1]
        else:
            key = int(dir[0][4:-1])
            value = np.base_repr(int(dir[1]), base=2, padding=36)
            value = value[len(value)-36:len(value)]
            value = "".join([mask[i] if mask[i] != 'X' else value[i]
                             for i in range(36)])
            mem[key] = value

    return sum([int(val, 2) for val in mem.values()])


if __name__ == "__main__":
    directions = parse_input()
    print(run_directions(directions))
