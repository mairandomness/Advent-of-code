def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [int(line) for line in lines]


def run_code(numbers):
    numbers[1] = 12
    numbers[2] = 2
    i = 0
    print(numbers)
    while True:
        if numbers[i] == 99:
            break

        elif numbers[i] == 1:
            numbers[numbers[i+3]] = numbers[numbers[i+1]] + \
                numbers[numbers[i+2]]
            i += 4

        elif numbers[i] == 2:
            numbers[numbers[i+3]] = numbers[numbers[i+1]] * \
                numbers[numbers[i+2]]
            i += 4
        if i == 4:
            print(numbers)
    return numbers[0]


def main():
    numbers = parse_input()

    print(run_code(numbers))


if __name__ == "__main__":
    main()
