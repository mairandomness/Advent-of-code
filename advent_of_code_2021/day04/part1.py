#!/usr/bin/env python3

import functools


class Board:
    def __init__(self, lines, rows):
        self.lines = lines
        self.rows = rows
        # self.diagonals = diagonals


def make_set_board(board):
    # make lines
    lines = [set(line) for line in board]

    # make rows
    rows = []
    for i in range(len(board[0])):
        rows.append({board[j][i] for j in range(len(board))})

    # # make diagonals
    # diagonals = [{board[i][i] for i in range(len(board))},
    #              {board[i][len(board) - i - 1] for i in range(len(board))}]
    # print(diagonals)
    return Board(lines, rows)


def parse_input(file):
    with open(file, "r") as f:
        text = f.read()
        lines = text.split("\n\n")
        number_calls = lines[0].split(",")
        number_calls = [int(i) for i in number_calls]
        boards = [board.split("\n") for board in lines[1:]]
        boards = [[[int(num) for num in line.split(" ") if num != ""]
                   for line in board] for board in boards]
        boards = [make_set_board(board) for board in boards]
        print(boards[0].rows)
    return (number_calls, boards)


def update_board(board, number):
    for i, line in enumerate(board.lines):
        board.lines[i].discard(number)
        if not board.lines[i]:
            print("line win")
            return True
    for i, row in enumerate(board.rows):
        board.rows[i].discard(number)
        if not board.rows[i]:
            print("row win")
            return True
    # for i, diagonal in enumerate(board.diagonals):
    #     board.diagonals[i].discard(number)
    #     if not board.diagonals[i]:
    #         print("diagonal win")
    #         return True


def play_bingo(number_calls, boards):
    for number in number_calls:
        for i, board in enumerate(boards):
            if update_board(boards[i], number):
                numbers_left = functools.reduce(
                    lambda acc, line: acc.union(line), board.lines)
                sum = functools.reduce(lambda a, b: a + b, numbers_left)
                print(sum)
                return sum * number


if __name__ == "__main__":
    numbers = parse_input("input")
    calls, boards = numbers
    print(play_bingo(calls, boards))

    test = parse_input("test")
    test_calls, test_boards = test
    test_product = play_bingo(test_calls, test_boards)
    assert(test_product == 4512)
