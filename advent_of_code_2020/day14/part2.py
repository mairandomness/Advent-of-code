#!/usr/bin/env python3

import numpy as np


def parse_input():
    with open("input", "r") as f:
        text = f.read().split("\n")
    directions = [line.split(" = ") for line in text]
    return directions


def parse_directions(directions):
    # just writing directions as a list of key (post mask)  and value
    new_directions = []
    mask = ""

    for dir in directions:
        if dir[0] == "mask":
            mask = dir[1]
        else:
            value = int(dir[1])
            key = np.base_repr(int(dir[0][4:-1]), base=2, padding=36)
            key = key[len(key)-36:len(key)]
            key = "".join([mask[i] if mask[i] != '0' else key[i]
                           for i in range(36)])

            new_directions.append((key, value))
    return new_directions


def gimme_the_sum(directions):
    # let's start from the end, since if we do, the first time we
    # encounter a key, that will be the its final value

    directions.reverse()
    visited = []
    acc = 0

    for key, value in directions:
        # for each new masked key, we check how many new keys it adds to our mem
        # and we increment the acc accordingly
        n_new_keys = number_of_new_keys(visited, key)
        visited.append(key)
        acc += value * n_new_keys

    return(acc)


def number_of_new_keys(visited_keys, new_key):
    colisions = check_colisions(visited_keys, new_key)
    if not colisions:
        # if there are no colisions with old masked keys, the number of
        # new keys is 2**(number of 'X's in the new masked key)
        return (2 ** sum([1 for char in new_key if char == 'X']))
    else:
        # if there are colisions we go and actually break down the masked keys into
        # all the values they can represent
        # and check how many new ones are left
        new_keys = set(gimme_all_keys(new_key))
        colisions = [set(gimme_all_keys(key)) for key in colisions]
        for keys in colisions:
            new_keys -= keys
        return len(new_keys)


def check_colisions(visited_keys, new_key):
    # returns a list of all masked keys that have a colision with a new masked key
    colisions = []
    for visited_key in visited_keys:
        colides = True
        for i in range(len(new_key)):
            if new_key[i] != 'X' and visited_key[i] != 'X' and new_key[i] != visited_key[i]:
                colides = False
                break
        if colides:
            colisions.append(visited_key)
    return colisions


def gimme_all_keys(key):
    roots = [""]
    for c in key:
        if c != 'X':
            for i, root in enumerate(roots):
                roots[i] = root + c

        else:
            new_roots = []
            for root in roots:
                new_roots.append(root + '1')
                new_roots.append(root + '0')
            roots = new_roots
    return roots


if __name__ == "__main__":
    directions = parse_input()
    directions = parse_directions(directions)
    print(gimme_the_sum(directions))
