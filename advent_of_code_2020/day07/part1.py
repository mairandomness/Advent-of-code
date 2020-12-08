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


def count_bag_possib(bags):
    contained_in = []
    queue = ['shiny gold']
    while queue:
        color = queue.pop()
        for bag in bags.keys():
            for (_, color2) in bags[bag]:
                if color2 == color:
                    if bag not in contained_in:
                        contained_in.append(bag)
                        queue.append(bag)
                    break
    return len(contained_in)


if __name__ == "__main__":
    bags = parse_input()
    print(count_bag_possib(bags))
