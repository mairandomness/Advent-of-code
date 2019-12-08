def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [line for line in lines]


def run_code(numbers_cp):
    i = 0
    input = "1"
    # print(numbers_cp)
    # print("len numbers_cp", len(numbers_cp))
    while True:
        if numbers_cp[i] == "99":
            break

        elif numbers_cp[i] == '3':
            print("instructions", numbers_cp[i], numbers_cp[i+1])
            numbers_cp[int(numbers_cp[i+1])] = input
            print("puts input {} at position {} so numbers_cp[{}] = {}".format(
                input, numbers_cp[i+1], numbers_cp[i+1], numbers_cp[int(numbers_cp[i+1])]))
            i += 2

        elif numbers_cp[i] == '103':
            numbers_cp[i+1] = input
            i + 2

        elif numbers_cp[i] == '4':
            print("instructions", numbers_cp[i], numbers_cp[i+1])

            output = numbers_cp[int(numbers_cp[i+1])]
            print(output)
            i += 2

        elif numbers_cp[i] == '104':
            print("instructions", numbers_cp[i], numbers_cp[i+1])
            output = numbers_cp[i+1]
            print(output)
            i += 2

        else:
            parameters = [0, 0, 0]
            mode = [int(char) for char in str(numbers_cp[i][:-2])]
            while len(mode) < 3:
                mode = [0] + mode
            # print(mode)
            mode.reverse()
            # print("i : ", i)
            print["instructions", numbers_cp[i],
                numbers_cp[i+1], numbers_cp[i+2], numbers_cp[i+3]]
            # print("modes", mode)
            for j in range(3):
                if mode[j] == 1 or j == 2:
                    parameters[j] = int(numbers_cp[i+j+1])
                else:
                    address = int(numbers_cp[i+j+1])
                    # print("ad", address, "j", j, "mode", mode[j])

                    # print(numbers_cp[address])
                    parameters[j] = int(numbers_cp[address])
            # print("parameters", parameters)

            if numbers_cp[i] == "1" or (len(numbers_cp[i]) > 1 and numbers_cp[i][-2:] == "01"):
                numbers_cp[parameters[2]] = str(parameters[0] + parameters[1])
                print("puts {} + {} at position {} so numbers_cp[{}] = {}".format(
                    parameters[0], parameters[1], parameters[2], parameters[2], numbers_cp[parameters[2]]))

            elif numbers_cp[i] == "2" or numbers_cp[i][-2:] == '02':
                numbers_cp[parameters[2]] = str(parameters[0] * parameters[1])
                print("puts {} * {} at position {} so numbers_cp[{}] = {}".format(
                    parameters[0], parameters[1], parameters[2], parameters[2], numbers_cp[parameters[2]]))

            i += 4
    return 0


def main():
    numbers_cp = parse_input()

    run_code(numbers_cp)


if __name__ == "__main__":
    main()
