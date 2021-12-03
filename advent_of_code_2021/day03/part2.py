#!/usr/bin/env python3

def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
        lines = text.split("\n")
    return lines


def life_support(numbers):
    oxi_rating = find_rating('oxi', numbers)
    co2_rating = find_rating('co2', numbers)
    return (oxi_rating * co2_rating)


def find_rating(type, numbers):
    numbers_copy = numbers[:]
    for i in range(len(numbers_copy[0])):
        position = sum([int(line[i]) for line in numbers_copy])
        if (2 * position >= len(numbers_copy) and type == 'oxi') or (2 * position < len(numbers_copy) and type == 'co2'):
            key = '0'
        else:
            key = '1'

        numbers_copy = [line for line in numbers_copy if line[i] == key]
        if len(numbers_copy) == 1:
            rating = int(int(numbers_copy[0], 2))
            break

    return int(int(numbers_copy[0], 2))


if __name__ == "__main__":
    numbers = parse_input("input")
    vars = life_support(numbers)
    print(vars)

    test = parse_input("test")
    vars = life_support(test)
    assert(vars == 230)
