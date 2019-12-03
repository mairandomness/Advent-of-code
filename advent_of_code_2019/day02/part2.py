def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [int(line) for line in lines]


def test_result(numbers):
    numbers_copy = numbers[:]
    for numbers[1] in range(100):
        for numbers[2] in range(100):
            noun = numbers[1]
            verb = numbers[2]
            numbers = numbers_copy[:]
            numbers[1] = noun
            numbers[2] = verb
            i = 0

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

            if numbers[0] == 19690720:
                return 100 * noun + verb


def main():
    numbers = parse_input()

    print(test_result(numbers))


if __name__ == "__main__":
    main()
