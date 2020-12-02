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
    for i, range in enumerate(ranges):
        letter = letters[i]
        password = passwords[i]
        count = 0
        for char in password:
            if char == letter:
                count += 1
                if count > range[1]:
                    break
        if count >= range[0] and count <= range[1]:
            valid += 1
    return valid


if __name__ == "__main__":
    (ranges, letters, passwords) = parse_input()
    print(check_amount_valid(ranges, letters, passwords))
