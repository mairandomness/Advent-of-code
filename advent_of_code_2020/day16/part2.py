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


def discard_errors(rules, nearby_tickets):
    intervals = get_intervals(rules)
    new_tickets = []
    is_error = True

    for ticket in nearby_tickets:
        for number in ticket:
            is_error = True
            for (mini, maxi) in intervals:
                if number >= mini and number <= maxi:
                    is_error = False
                    break
            if is_error:
                break
        if not is_error:
            new_tickets.append(ticket)
    return new_tickets


def find_possible_order(rules, nearby_tickets):
    possible_order = {rule[0]: [] for rule in rules}
    for rule in rules:
        key = rule[0]
        (min1, max1) = rule[1]
        (min2, max2) = rule[2]
        for i in range(len(rules)):
            fits = True
            for ticket in nearby_tickets:
                if (ticket[i] < min1 or ticket[i] > max1) and (ticket[i] < min2 or ticket[i] > max2):
                    fits = False
                    break
            if fits:
                possible_order[key].append(i)
    return possible_order


def get_ordering(possible_order):
    done = False
    removed = []
    while not done:
        done = True
        for key in possible_order.keys():
            if len(possible_order[key]) == 1 and possible_order[key][0] not in removed:
                to_remove = possible_order[key][0]
                done = False

                for key in possible_order.keys():
                    if len(possible_order[key]) != 1:
                        possible_order[key].remove(to_remove)
                removed.append(to_remove)
    return possible_order


def get_answer(my_ticket, order):
    answer = 1
    for key in order.keys():
        if "departure" in key:
            answer *= my_ticket[order[key][0]]
    return answer


if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    rules, my_ticket, nearby_tickets = parse_input()
    nearby_tickets = discard_errors(rules, nearby_tickets)
    possible_order = find_possible_order(rules, nearby_tickets)
    order = get_ordering(possible_order)
    print(get_answer(my_ticket, order))
