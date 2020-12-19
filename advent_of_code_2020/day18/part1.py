#!/usr/bin/env python3

import pprint


def parse_input():
    with open("input", "r") as f:
        text = f.read().split("\n")
    return [[int(char) if char.isnumeric() else char for char in line.replace(" ", "")] for line in text]


def solve(expressions):
    done = False
    while not done:
        done = True
        for j, line in enumerate(expressions):
            if isinstance(line, int):
                pass
            elif isinstance(line, list) and len(line) == 1:
                expressions[j] = line[0]
            else:
                done = False
                new_line = []
                i = 0
                while i  < len(line):
                    if i == 0 and isinstance(line[i], int) and isinstance(line[i+2], int):
                        new_line.append(calculate(line[i:i+3]))
                        i += 3
                    elif line[i] == '(' and line[i+2] == ')':
                        new_line.append(line[i+1])
                        i += 3
                    elif line[i] == '(' and isinstance(line[i + 1], int) and isinstance(line[i+3], int):
                        new_line.append('(')
                        new_line.append(calculate(line[i+1:i+4]))
                        i += 4
                    else:
                        new_line.append(line[i])
                        i += 1
                expressions[j] = new_line
    return expressions


def calculate(piece):
    int1, op, int2 = piece
    if op == '*':
        return int1 * int2
    elif op == '+':
        return int1 + int2


if __name__ == "__main__":
    expressions = parse_input()
    print(sum(solve(expressions)))
