#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    numbers = [int(i) for i in text.split("\n")]
    return numbers


def is_valid(i, numbers):
    n_slice = numbers[i - 25:i]
    n_slice.sort()
    target = numbers[i]
    i = 0
    j = 24
    while i < j:
        if n_slice[i] + n_slice[j] == target:
            return True
        elif n_slice[i] + n_slice[j] > target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == "__main__":
    numbers = parse_input()
    for i in range(25, len(numbers)):
        if not is_valid(i, numbers):
            print(numbers[i])
