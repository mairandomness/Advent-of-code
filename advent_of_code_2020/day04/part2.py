#!/usr/bin/env python3

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    data = text.split("\n\n")
    passports = []
    for entry in data:
        entry.replace("\n", " ")
        entry = entry.split()
        fields = [field.split(":")
                  for field in entry if field.split(":")[0] != "cid"]
        passports.append(fields)
    return passports


def check_field_presence(passports):
    present = []
    for i, passport in enumerate(passports):
        if len(passport) == 7:
            present.append(i)
    return present


def check_valids(passports):

    present = check_field_presence(passports)
    count = len(present)
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    chars = "0123456789abcdef"
    for i in present:
        for field in passports[i]:
            if field[0] == "byr" and (not field[1].isnumeric() or int(field[1]) < 1920 or int(field[1]) > 2002):
                count -= 1
                break
            elif field[0] == "iyr" and (not field[1].isnumeric() or int(field[1]) < 2010 or int(field[1]) > 2020):
                count -= 1
                break
            elif field[0] == "eyr" and (not field[1].isnumeric() or int(field[1]) < 2020 or int(field[1]) > 2030):
                count -= 1
                break
            elif field[0] == "hgt":
                if not field[1][:-2].isnumeric():
                    count -= 1
                    break
                elif field[1][-2:] != "in" and field[1][-2:] != "cm":
                    count -= 1
                    break
                elif field[1][-2:] == "in" and (int(field[1][:-2]) < 59 or int(field[1][:-2]) > 76):
                    count -= 1
                    break
                elif field[1][-2:] == "cm" and (int(field[1][:-2]) < 150 or int(field[1][:-2]) > 193):
                    count -= 1
                    break
            elif field[0] == "hcl":
                if field[1][0] != "#" or len(field[1]) != 7:
                    count -= 1
                    break
                elif set(field[1][1:]) - set(chars):
                    count -= 1
                    break
            elif field[0] == "ecl" and field[1] not in eye_colors:
                count -= 1
                break
            elif field[0] == "pid" and (not field[1].isnumeric() or len(field[1]) != 9):
                count -= 1
                break

    return count


if __name__ == "__main__":
    passports = parse_input()
    print(check_valids(passports))
