#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.split("\n")
    board_passes = [(int(line[:7].replace('F', '0').replace('B', '1'), 2), int(
        line[7:].replace('L', '0').replace('R', '1'), 2)) for line in data]
    seat_IDs = [8 * row + col for row, col in board_passes]
    return seat_IDs


if __name__ == "__main__":
    seat_IDs = parse_input()
    print(max(seat_IDs))
