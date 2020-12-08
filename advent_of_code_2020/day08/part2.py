#!/usr/bin/env python3

# I'd rather have some repetition and more readability u.u
# though original_loop and finite are pretty close to being the same function

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.split("\n")
    instructions = [(line.split(" ")[0], int(
        line.split(" ")[1])) for line in data]
    return instructions


def original_loop(instructions):
    i_list = []
    i = 0
    while True:
        if i in i_list:
            break
        else:
            i_list.append(i)

        instruct, n = instructions[i]
        if instruct == 'nop':
            i += 1
        elif instruct == 'acc':
            i += 1
        elif instruct == 'jmp':
            i += n
    return i_list


def finite(instructions):
    i_list = []
    i = 0
    ACC = 0
    while True:
        if i in i_list:
            return False
        elif i == len(instructions):
            return ACC
        else:
            i_list.append(i)

        instruct, n = instructions[i]

        if instruct == 'nop':
            i += 1
        elif instruct == 'acc':
            i += 1
            ACC += n
        elif instruct == 'jmp':
            i += n


def fix_it(instructions, i_list):
    is_finite = False
    for i in i_list:
        if instructions[i][0] == 'nop':
            instructions_copy = instructions[:]
            instructions_copy[i] = ('jmp', instructions[i][1])
            is_finite = finite(instructions_copy)
        elif instructions[i][0] == 'jmp':
            instructions_copy = instructions[:]
            instructions_copy[i] = ('nop', instructions[i][1])
            is_finite = finite(instructions_copy)
        if is_finite:
            return is_finite


if __name__ == "__main__":
    instructions = parse_input()
    i_list = [i for i in original_loop(
        instructions) if instructions[i][0] != 'acc']
    print(fix_it(instructions, i_list))
