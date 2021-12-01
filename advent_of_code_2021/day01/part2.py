#!/usr/bin/env python3

def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
        lines = text.split("\n")
    return [int(i) for i in lines]


def count_increases(numbers):
    increases = 0
    for i, num in enumerate(numbers[:-3]):
        next = numbers[i+3]
        if next > num:
            increases += 1
    return increases


if __name__ == "__main__":
    numbers = parse_input("input")
    count = count_increases(numbers)

    test = parse_input("test")
    assert(count_increases(test) == 5)

    print(count)
