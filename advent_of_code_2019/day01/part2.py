import math


def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
    return [int(line) for line in lines]


def fuel_req(numbers):
    fuel_list = []

    for number in numbers:
        total_fuel = 0

        while number > 0:
            number = max(math.floor(number/3) - 2, 0)
            total_fuel += number

        fuel_list.append(total_fuel)
    return sum(fuel_list)


def main():
    numbers = parse_input()
    print(fuel_req(numbers))


if __name__ == "__main__":
    main()
