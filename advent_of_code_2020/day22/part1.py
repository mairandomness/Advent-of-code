#!/usr/bin/env python3


def parse_input():
    with open("input", "r") as f:
        text = f.read()
    player1, player2 = text.split('\n\n')
    player1 = [int(n) for n in player1.split("\n")[1:]]
    player2 = [int(n) for n in player2.split("\n")[1:]]
    return player1, player2


def run_game(player1, player2):
    while len(player1) > 0 and len(player2) > 0:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1 += [p1, p2]
        else:
            player2 += [p2,p1]
    return player2 + player1


if __name__ == "__main__":
    player1, player2 = parse_input()
    print(sum([(i + 1 )* num for i, num in enumerate(reversed(run_game(player1, player2)))]))
