#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.split("\n")
    instructions = [(line.split(" ")[0], int(line.split(" ")[1]))
                    for line in data]
    return instructions


def int_code(instructions, ACC):
    i_list = []
    i = 0
    while True:
        if i not in i_list:
            i_list.append(i)
        else:
            break

        instruct, n = instructions[i]
        if instruct == 'nop':
            i += 1
        elif instruct == 'acc':
            i += 1
            ACC += n
        elif instruct == 'jmp':
            i += n

    return ACC


if __name__ == "__main__":
    instructions = parse_input()
    ACC = 0
    print(int_code(instructions, ACC))
