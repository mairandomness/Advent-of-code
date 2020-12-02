#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
        lines = text.split("\n")
    return [int(i) for i in lines]


def make_pairs(numbers):
    return [(a, b) for a in numbers for b in numbers if a + b + min(numbers) <= 2020 and a < b]


def find_trio(numbers, pairs):
    numbers.sort()
    print(numbers)
    pairs.sort(key=lambda x: sum(x))

    for number in numbers:
        for pair in pairs:
            if number < pair[0] and number + sum(pair) == 2020:
                print("First number:", number)
                print("Second number:", pair[0])
                print("Third number:", pair[1])
                print("Product:", number * pair[0] * pair[1])


if __name__ == "__main__":
    numbers = parse_input()
    find_trio(numbers, make_pairs(numbers))
