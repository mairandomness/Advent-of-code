#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    directions = [(line[0], int(line[1:])) for line in text.split("\n")]
    return directions


def navigate(directions):
    cardinals = ["N", "E", "S", "W"]
    facing = "E"
    ns = 0
    we = 0

    for d, value in directions:
        if d == "N":
            ns += value
        elif d == "S":
            ns -= value
        elif d == "E":
            we += value
        elif d == "W":
            we -= value
        elif d == "F":
            d = facing
            if d == "N":
                ns += value
            elif d == "S":
                ns -= value
            elif d == "E":
                we += value
            elif d == "W":
                we -= value
        elif d == "R":
            facing = cardinals[(cardinals.index(facing) + value//90) % 4]
        elif d == "L":
            facing = cardinals[(cardinals.index(facing) - value//90) % 4]

    print("ns: ", ns, " we: ", we)
    return (abs(ns) + abs(we))


if __name__ == "__main__":
    directions = parse_input()
    print(navigate(directions))
