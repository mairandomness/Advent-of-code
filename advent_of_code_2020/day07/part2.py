#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.replace("bags", "bag").replace(", ", "").split("\n")
    bags = {}
    groups = [line[:-1].split(" bag contain ") for line in data]
    for group in groups:
        bags[group[0]] = []
        bag_list = group[1].split(" bag")[:-1]
        for elem in bag_list:
            if elem != 'no other':
                bags[group[0]].append((int(elem[:1]), elem[2:]))
    return bags


def how_many_inside(bags):
    queue = [(1, 'shiny gold')]
    # start at -1, because the first outer shiny gold bag doesn't count
    acc = -1
    while queue:
        print(queue)
        i, color = queue.pop()
        acc += i
        print(acc)
        for n, bag in bags[color]:
            queue.append((n * i, bag))
    return acc


if __name__ == "__main__":
    bags = parse_input()
    print(how_many_inside(bags))
