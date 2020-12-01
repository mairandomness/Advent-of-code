#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
        lines = text.split("\n")
    return [int(i) for i in lines]


def find_pair(numbers):
    numbers.sort()
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == 2020:
            print("First number:", numbers[i])
            print("Second number:", numbers[j])
            print("Product:", numbers[i] * numbers[j])
            break
        elif numbers[i] + numbers[j] < 2020:
            i += 1
        else:
            j -= 1


if __name__ == "__main__":
    numbers = parse_input()
    find_pair(numbers)
    # just making sure it's unique
    print([[a, b] for a in numbers for b in numbers if a + b == 2020 and a <= b])