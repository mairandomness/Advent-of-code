#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.split("\n\n")
    passports = []
    for entry in data:
        entry.replace("\n", " ")
        entry = entry.split()
        fields = [field.split(":")[0]
                  for field in entry if field.split(":")[0] != "cid"]
        passports.append(fields)
    return passports


def check_valids(passports):
    count = 0
    for passport in passports:
        if len(passport) == 7:
            count += 1
    return count


if __name__ == "__main__":
    passports = parse_input()
    print(check_valids(passports))
