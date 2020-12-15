#!/usr/bin/env python3


def run_game(numbers, target):
    last_spoken = numbers[-1]
    spoken = {}
    turn = len(numbers) + 1

    for i, number in enumerate(numbers):
        spoken[number] = [i + 1]

    while True:
        if len(spoken[last_spoken]) == 1:
            last_spoken = 0

        else:
            last_spoken = - spoken[last_spoken].pop(0) + spoken[last_spoken][0]

        if turn == target:
            return last_spoken

        if last_spoken in spoken.keys():
            spoken[last_spoken].append(turn)
        else:
            spoken[last_spoken] = [turn]

        turn += 1


if __name__ == "__main__":
    numbers = [18, 8, 0, 5, 4, 1, 20]
    test1 = [0, 3, 6]
    print("part1: ", run_game(numbers, 2020))
    print("part2: ", run_game(numbers, 30000000))
