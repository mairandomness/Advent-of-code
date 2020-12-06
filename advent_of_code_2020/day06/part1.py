#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.split("\n\n")
    groups = [group.split("\n") for group in data]
    return groups


def find_yesses(groups):
    acc_yesses = []
    for group in groups:
        yesses = set()
        for person in group:
            yesses = yesses.union(set(person))
        acc_yesses.append(len(yesses))
    return sum(acc_yesses)


if __name__ == "__main__":
    groups = parse_input()
    print(find_yesses(groups))
