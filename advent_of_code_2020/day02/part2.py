#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()

    lines = text.split("\n")
    passwords = [line.split(": ")[1] for line in lines]
    letters = [line.split(" ")[1][:1] for line in lines]
    ranges = [(int(a), int(b))
              for a, b in [line.split(" ")[0].split("-") for line in lines]]

    return (ranges, letters, passwords)


def check_amount_valid(ranges, letters, passwords):
    valid = 0
    for i, (n, m) in enumerate(ranges):
        letter = letters[i]
        password = passwords[i]
        if (password[n-1] == letter) ^ (m-1 < len(password) and password[m-1] == letter):
            valid += 1

    return valid


if __name__ == "__main__":
    (ranges, letters, passwords) = parse_input()
    print(check_amount_valid(ranges, letters, passwords))
