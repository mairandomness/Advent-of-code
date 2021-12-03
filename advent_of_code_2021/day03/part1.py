#!/usr/bin/env python3

def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
        lines = text.split("\n")
    return [[int(bit) for bit in line] for line in lines]


def power_consumption(numbers):
    gamma = ''
    epsilon = ''
    for i in range(len(numbers[0])):
        in_position = sum([line[i] for line in numbers])
        if in_position > len(numbers) // 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma = int(int(gamma, 2))
    epsilon = int(int(epsilon, 2))
    return (gamma, epsilon)


if __name__ == "__main__":
    numbers = parse_input("input")
    vars = power_consumption(numbers)
    print(vars[0] * vars[1])

    test = parse_input("test")
    vars = power_consumption(test)
    assert(vars[0] * vars[1] == 198)
