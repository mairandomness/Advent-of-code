#!/usr/bin/env python3

import sys
sys.setrecursionlimit(50000000)


def parse_input():
    with open("input", "r") as f:
        text = f.read()
    player1, player2 = text.split('\n\n')
    player1 = [int(n) for n in player1.split("\n")[1:]]
    player2 = [int(n) for n in player2.split("\n")[1:]]
    return player1, player2


def run_game(player1, player2, states, all_seen):
    key = "".join(str(c) if c > 9 else '0' + str(c) for c in player1) + \
        "." + "".join(str(c) if c > 9 else '0' + str(c) for c in player2)
    if key in states:
        return (player1, [], [], {})
    else:
        states.append(key)

    if len(player1) == 0 or len(player2) == 0:
        return (player1, player2, states, all_seen)

    else:

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        if len(player1) >= p1 and len(player2) >= p2:
            key = "".join(str(c) if c > 9 else '0' + str(c) for c in player1[:p1]) + "." + "".join(
                str(c) if c > 9 else '0' + str(c) for c in player2[:p2])
            if key in all_seen.keys():
                if all_seen[key] == 0:
                    b = []
                else:
                    b = [1]

            else:
                (a, b, c, d) = run_game(
                    player1[:p1], player2[:p2], [], all_seen)
                if len(key) < 20:
                    all_seen[key] = len(b)

            if len(b) == 0:
                player1 += [p1, p2]
            else:
                player2 += [p2, p1]
        else:
            if p1 > p2:
                player1 += [p1, p2]
            else:
                player2 += [p2, p1]
        return run_game(player1, player2, states, all_seen)


if __name__ == "__main__":
    player1, player2 = parse_input()
    (a, b, c, d) = run_game(player1, player2, [], {})
    print(a)
    print(b)
    if len(b) == 0:
        print(sum([(i + 1) * num for i,
                   num in enumerate(reversed(a))]))
    else:
        print(sum([(i + 1) * num for i,
                   num in enumerate(reversed(b))]))
