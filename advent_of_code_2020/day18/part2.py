#!/usr/bin/env python3


def parse_input():
    with open("input", "r") as f:
        text = f.read().split("\n")
    return [[int(char) if char.isnumeric() else char for char in line.replace(" ", "")] for line in text]


def solve(expressions):
    for j, line in enumerate(expressions):
        if isinstance(line, int):
            pass
        else:
            new_line = line[:]
            while len(new_line) != 1:
                new_line = do_sums_and_parens(new_line)
                new_line = do_products(new_line)

            expressions[j] = new_line[0]

    return expressions


def do_sums_and_parens(line):
    new_line = []
    i = 0
    while i < len(line):
        if isinstance(line[i], int) and i != len(line) - 1 and line[i+1] == '+' and isinstance(line[i+2], int):
            new_line.append(calculate(line[i:i+3]))
            i += 3
        else:
            new_line.append(line[i])
            i += 1
    new_line = get_rid_of_parens(new_line)
    new_line = parens_product(new_line)
    if new_line != line:
        new_line = do_sums_and_parens(new_line)
    return new_line


def get_rid_of_parens(line):
    new_line = []
    i = 0
    while i < len(line):
        if line[i] == '(' and line[i+2] == ')':
            new_line.append(line[i+1])
            i += 3
        else:
            new_line.append(line[i])
            i += 1
    return new_line


def do_products(line):
    new_line = []
    i = 0

    if '(' in line:
        while i < len(line):
            if is_innermost(i, line) and line[i] == '(' and isinstance(line[i+1], int) and i != len(line) - 1 and line[i+2] == '*' and isinstance(line[i+3], int):
                new_line.append('(')
                new_line.append(calculate(line[i+1:i+4]))
                i += 4
            else:
                new_line.append(line[i])
                i += 1

    else:
        while i < len(line):
            if isinstance(line[i], int) and i != len(line) - 1 and line[i+1] == '*' and isinstance(line[i+2], int):
                new_line.append(calculate(line[i:i+3]))
                i += 3
            else:
                new_line.append(line[i])
                i += 1
    return new_line

def is_innermost(i, line):
    for j in range(i + 1, len(line)):
        if line[j] == '(':
            return False
        if line[j] == ')':
            return True

def parens_product(line):
    new_line = []
    i = 0
    while i < len(line):
        if line[i] == '(' and isinstance(line[i+1], int) and i != len(line) - 1 and line[i+2] == '*' and isinstance(line[i+3], int) and line[i+4] == ')':
            new_line.append(calculate(line[i+1:i+4]))
            i += 5
        else:
            new_line.append(line[i])
            i += 1
    print(new_line)
    return new_line


def calculate(piece):
    int1, op, int2 = piece
    if op == '*':
        return int1 * int2
    elif op == '+':
        return int1 + int2


if __name__ == "__main__":
    expressions = parse_input()
    print(solve(expressions))
    print(sum(solve(expressions)))

