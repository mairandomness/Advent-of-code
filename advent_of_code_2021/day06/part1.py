#!/usr/bin/env python3

def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
        lines = text.split(",")
    return [int(i) for i in lines]


def count_fish(initial_fish, days):
    fish_dict = {i: 0 for i in range(9)}

    for fish in initial_fish:
        fish_dict[fish] = fish_dict.get(fish, 0) + 1

    for day in range(days):
        fish_to_reset = fish_dict.get(0, 0)

        for count in range(8):
            fish_dict[count] = fish_dict.get(count + 1, 0)

        fish_dict[6] = fish_dict.get(6, 0) + fish_to_reset
        fish_dict[8] = fish_to_reset

    return sum(fish_dict.values())


if __name__ == "__main__":
    numbers = parse_input("input")
    count = count_fish(numbers, 80)
    print(count)

    test = parse_input("test")
    assert(count_fish(test, 18) == 26)
    assert(count_fish(test, 80) == 5934)
