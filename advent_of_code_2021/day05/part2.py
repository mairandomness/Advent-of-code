#!/usr/bin/env python3

def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
        lines = text.split("\n")
    return [[[int(n) for n in piece.split(",") if n != ''] for piece in line.split(" -> ")] for line in lines]


def make_grid(max_x, max_y):
    board = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]
    return board


def mark_line_on_board(line, board):
    curr_x, curr_y = line[0]
    x, y = line[1]

    if curr_y == y:
        while curr_x != x:
            board[curr_y][curr_x] += 1
            if curr_x > x:
                curr_x -= 1
            else:
                curr_x += 1

    elif curr_x == x:
        while curr_y != y:
            board[curr_y][curr_x] += 1
            if curr_y > y:
                curr_y -= 1
            else:
                curr_y += 1
    else:
        while curr_y != y:
            board[curr_y][curr_x] += 1
            if curr_y > y and (curr_x - x) // (curr_y - y) == 1:
                curr_y -= 1
                curr_x -= 1
            elif curr_y < y and (curr_x - x) // (curr_y - y) == 1:
                curr_y += 1
                curr_x += 1
            elif curr_y > y:
                curr_y -= 1
                curr_x += 1
            elif curr_y < y:
                curr_y += 1
                curr_x -= 1

    board[y][x] += 1
    return board


def check_lines(lines):
    max_x = max([max(line[0][0], line[1][0]) for line in lines])
    max_y = max([max(line[0][1], line[1][1]) for line in lines])
    board = make_grid(max_x, max_y)
    for line in lines:
        board = mark_line_on_board(line, board)
    board = [point for line in board for point in line if point > 1]
    return len(board)


if __name__ == "__main__":
    numbers = parse_input("input")
    print(check_lines(numbers))

    test = parse_input("test")
    test = check_lines(test)
    assert(test == 12)
