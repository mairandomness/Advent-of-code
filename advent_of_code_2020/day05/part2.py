#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.split("\n")
    board_passes = [(int(line[:7].replace('F', '0').replace('B', '1'), 2), int(
        line[7:].replace('L', '0').replace('R', '1'), 2)) for line in data]
    seat_IDs = [8 * row + col for row, col in board_passes]
    return seat_IDs


def find_my_seat(seat_IDs):
    seat_IDs.sort()
    for i, ID in enumerate(seat_IDs[:-1]):
        if seat_IDs[i + 1] - ID == 2:
            return ID + 1


if __name__ == "__main__":
    seat_IDs = parse_input()
    print(find_my_seat(seat_IDs))
