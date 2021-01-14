#!/usr/bin/env python3

def crab_game(cups):
    cups_copy = cups[:]
    cur_cup = cups[0]
    three_cups = cups[1:4]
    cups = cups[:1] + cups[4:]
    dest_cup = cur_cup

    while dest_cup in three_cups or dest_cup == cur_cup:
        dest_cup -= 1
        if dest_cup == 0:
            dest_cup = max(cups_copy)
    
    i = cups.index(dest_cup) + 1
    cups = cups[:i] + three_cups + cups[i:]
    cups = cups[1:] + cups[:1]
    return cups

if __name__ == "__main__":
    input = "523764819"
    test = "389125467"
    cups = [int(num) for num in input]
    #cups = [int(num) for num in test]
    for i in range(100):
        cups = crab_game(cups)
    i = cups.index(1)
    cups = cups[i:] + cups[:i]
    print("".join(str(cup) for cup in cups[1:]))

    cups = [i for i in range(1, 1000001)]
    for i, char in enumerate(test):
        cups[i] = int(char)
    for i in range(50):
        cups = crab_game(cups)
        print(cups[:20])
        print("tail", cups[-20:])