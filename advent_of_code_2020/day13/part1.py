#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    target, busses = text.split("\n")
    target = int(target)
    busses = [int(bus) for bus in busses.split(",") if bus != "x"]
    return (target, busses)


def next_bus(target, busses):
    wait_time = target + 1
    early_bus = 0
    for bus in busses:

        if bus - target % bus < wait_time:
            early_bus = bus
            wait_time = bus - target % bus

    print("early_bus: ", early_bus, " wait time: ", wait_time)
    print("target: ", target)
    print("departure_time: ", target + wait_time)
    print("product: ", early_bus*wait_time)


if __name__ == "__main__":
    (target, busses) = parse_input()
    next_bus(target, busses)
