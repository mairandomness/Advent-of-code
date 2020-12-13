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
    w_ns = 1
    w_we = 10

    for d, value in directions:
        if d == "N":
            w_ns += value
        elif d == "S":
            w_ns -= value
        elif d == "E":
            w_we += value
        elif d == "W":
            w_we -= value
        elif d == "F":
            ns += value * w_ns
            we += value * w_we
        elif d == "R":
            turns = (value//90) % 4
            for i in range(turns):
                (w_we, w_ns) = (w_ns, - w_we)
        elif d == "L":
            turns = (-value//90) % 4
            for i in range(turns):
                (w_we, w_ns) = (w_ns, - w_we)

    print("ns: ", ns, " we: ", we)
    return (abs(ns) + abs(we))


if __name__ == "__main__":
    directions = parse_input()
    print(navigate(directions))
