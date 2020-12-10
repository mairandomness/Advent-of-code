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


def find_contiguous(target, numbers):
    acc = 0
    # acc_list has the accumulated sum of numbers until its index non-inclusive
    # or, in other words: acc_list[n] == sum(numbers[:n])
    acc_list = [0]
    for number in numbers:
        acc += number
        acc_list.append(acc)

    # any contiguos sum(slice[n:m]) can be represented
    # by acc_list[m] - acc_list[n]
    for i in range(len(acc_list)):
        for j in range(i + 1, len(acc_list)):
            if acc_list[j] - acc_list[i] == target:
                min_n = min(numbers[i:j])
                max_n = max(numbers[i:j])
                print("min: ", min_n, ", max: ", max_n)
                print("sum: ", min_n + max_n)
                return 0


if __name__ == "__main__":
    numbers = parse_input()
    target = 0
    for i in range(25, len(numbers)):
        if not is_valid(i, numbers):
            target = numbers[i]
            break
    print("target:", target)
    find_contiguous(target, numbers)
