#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    numbers = [int(i) for i in text.split("\n")]
    return numbers


def possib_dict(numbers):
    numbers.sort()
    possib = {0: [i for i in range(1, 4) if i in numbers]}

    for i, number in enumerate(numbers[:-3]):
        possib[number] = {number + 1, number + 2, number +
                          3}. intersection({numbers[i + 1], numbers[i + 2], numbers[i + 3]})
    for i, number in enumerate(numbers[-3:]):
        possib[number] = [n for n in range(
            1 + number, 4 + number) if n in numbers]
    return possib


def traverse_tree(possib, curr, target):
    if curr == target:
        return 1
    elif curr > target:
        return 0
    else:
        return sum([traverse_tree(possib, a, target) for a in possib[curr]])


def get_diff3(numbers):
    diff3 = [0]

    for i, number in enumerate(numbers[:-1]):
        if i > 0 and numbers[i+1] - number == 3:
            diff3.append(number)

    diff3.append(max(numbers))
    return diff3


if __name__ == "__main__":
    numbers = parse_input()
    numbers.sort()
    possib = possib_dict(numbers)
    diff3 = get_diff3(numbers)

    total = 1
    for i, n in enumerate(diff3[:-1]):
        total *= traverse_tree(possib, n, diff3[i+1])
    print(total)

