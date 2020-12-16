#!/usr/bin/env python3

import pprint


def parse_input():
    with open("input", "r") as f:
        text = f.read().split("\n\n")
    rules = text[0].split("\n")
    rules = [line.split(": ") for line in rules]
    rules = [[line[0], [int(n) for n in line[1].split(" or ")[0].split(
        "-")], [int(n) for n in line[1].split(" or ")[1].split("-")]] for line in rules]
    my_ticket = [int(i) for i in text[1].split("\n")[1].split(",")]
    nearby_tickets = [[int(number) for number in ticket.split(",")]
                      for ticket in text[2].split("\n")[1:]]

    return (rules, my_ticket, nearby_tickets)


def get_intervals(rules):
    intervals = [(a, b) for line in rules for (a, b) in line[1:]]
    new_intervals = []

    for i, (a1, b1) in enumerate(intervals):
        redundant = False
        for j, (a2, b2) in enumerate(intervals):
            if i != j and a2 <= a1 and b2 >= b1:
                redundant = True
                break
        if not redundant:
            new_intervals.append((a1, b1))

    return new_intervals


def get_scanning_error(rules, nearby_tickets):
    intervals = get_intervals(rules)
    error = 0
    for ticket in nearby_tickets:
        for number in ticket:
            is_error = True
            for (mini, maxi) in intervals:
                if number >= mini and number <= maxi:
                    is_error = False
                    break
            if is_error:
                error += number
    return error


if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    rules, my_ticket, nearby_tickets = parse_input()
    print(get_scanning_error(rules, nearby_tickets))
    pp.pprint(rules)
    print(my_ticket)
    print(nearby_tickets)
    get_intervals(rules)
