#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    numbers = [int(i) for i in text.split("\n")]
    return numbers


def count_jolts(numbers):
    numbers.sort()
    diff1 = 0
    diff3 = 1
    start = 0
    end = max(numbers) + 3
    if numbers[0] == 1:
        diff1 += 1
    elif numbers[0] == 3:
        diff3 += 1

    for i, number in enumerate(numbers[:-1]):
        if numbers[i+1] - number == 1:
           diff1 += 1
        elif numbers[i+1] - number == 3:
            diff3 += 1
        else:
            print("something went terribly wrong")
    return (diff1, diff3)


if __name__ == "__main__":
    numbers = parse_input()
    a, b = count_jolts(numbers)
    print("diff1: ", a, " diff2: ", b)
    print("product: ", a * b)
