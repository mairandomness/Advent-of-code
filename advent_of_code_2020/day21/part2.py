#!/usr/bin/env python3

from functools import reduce


def parse_input():
    with open("input", "r") as f:
        text = f.read()
    recipes = text.split('\n')
    recipes = [line[:-1].split(" (contains ") for line in recipes]
    recipes = [[a.split(" "), b.split(", ")] for a, b in recipes]
    return recipes


def find_allergenics(recipes):
    recipes = [[set(a), set(b)] for a, b in recipes]
    aller_keys = set([item for recipe in recipes for item in recipe[1]])
    allergenics = {key: [] for key in aller_keys}

    for recipe in recipes:
        for key in recipe[1]:
            allergenics[key].append(recipe[0])

    for key in allergenics.keys():
        allergenics[key] = reduce(
            (lambda x, y: x.intersection(y)), allergenics[key])

    final_allergenics = {}
    while allergenics.values():
        for key in allergenics.keys():
            if len(allergenics[key]) == 1:
                final_allergenics[key] = list(allergenics[key])[0]
                for key1 in allergenics.keys():
                    allergenics[key1].discard(final_allergenics[key])
                allergenics.pop(key)
                break

    return final_allergenics


if __name__ == "__main__":
    recipes = parse_input()
    allergenics = find_allergenics(recipes)
    allerg = sorted(allergenics.items(), key = lambda kv:(kv[0], kv[1]))
    print(",".join([item[1] for item in allerg]))