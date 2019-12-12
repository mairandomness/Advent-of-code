# after much suffering, I think its time to refactor this a bit
# I never expected this code to be reused so much...
# and it's now.. just...bad...

import itertools


def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [line for line in lines]


def get_parameters(numbers, i, base):
    # print("numbers[i], i",numbers[i], i)
    if numbers[i] == '99':
        return []

    elif numbers[i][-1:] == '3' or numbers[i][-1:] == '4' or numbers[i][-1:] == '9':
        n_params = 1

    elif numbers[i][-1:] == '5' or numbers[i][-1:] == '6':
        n_params = 2

    elif numbers[i][-1:] == '1' or numbers[i][-1:] == '2' or numbers[i][-1:] == '7' or numbers[i][-1:] == '8':
        n_params = 3
    # print(numbers[i][-1:])
    # print("instructions:", numbers[i : i + n_params + 1])

    parameters = [0] * n_params

    if len(numbers[i]) == 1:
        mode = [0]
    else:
        mode = [int(char) for char in str(numbers[i][:-2])]

    while len(mode) < n_params:
        mode = [0] + mode
    mode.reverse()

    # print("modes:", mode)

    for j in range(n_params):
        if mode[j] == 2 and (j == 2 or numbers[i][-1:] == '3' or numbers[i][-1:] == '4'):
            parameters[j] = int(numbers[i+j+1]) + base
        elif mode[j] == 2:
            address = int(numbers[i+j+1]) + base
            parameters[j] = int(numbers[address])
        elif mode[j] == 1 or j == 2 or numbers[i][-1:] == '3' or numbers[i][-1:] == '4':
            parameters[j] = int(numbers[i+j+1])
        else:
            address = int(numbers[i+j+1])
            parameters[j] = int(numbers[address])

    # print("parameters:", parameters)

    return parameters


def run_intcode(numbers_original, input):
    numbers = numbers_original[:]
    base = 0
    i = 0
    output = 0

    # max_num = int(max(numbers, key=lambda x: len(x)))
    max_num = 999999
    if len(numbers) < max_num:
        numbers = numbers + (max_num - len(numbers)) * ['0']
    print("len numbers", len(numbers))

    inputees = [str(input)]
    while True:


        if numbers[i] == "99":
            return output

        parameters = get_parameters(numbers, i, base)

        if numbers[i][-1:] == '3':
            numbers[parameters[0]] = inputees[0]
            # print("puts input {} at position {} so numbers[{}] = {}".format(
            #      inputees[0], parameters[0], parameters[0], numbers[parameters[0]]))
            inputees.pop(0)

        elif numbers[i][-1:] == '4':
            if numbers[i] == "104":
                output = parameters[0]
            else:
                output = numbers[parameters[0]]
            print("OTPUT:", output)

        elif numbers[i][-1:] == '9':
            base += parameters[0]
            # print("Add value {} to base, resulting in {}".format(parameters[0], base))

        elif numbers[i][-1:] == '5':
            if parameters[0] != 0:
                i = parameters[1] - 3

        elif numbers[i][-1:] == '6':
            if parameters[0] == 0:
                i = parameters[1] - 3

        elif numbers[i][-1:] == '1':
            numbers[parameters[2]] = str(parameters[0] + parameters[1])
            # print("puts {} + {} at position {} so numbers_cp[{}] = {}".format(
            #                 parameters[0], parameters[1], parameters[2], parameters[2], numbers[parameters[2]]))

        elif numbers[i][-1:] == '2':
            numbers[parameters[2]] = str(parameters[0] * parameters[1])
            # print("puts {} * {} at position {} so numbers_cp[{}] = {}".format(
            #     parameters[0], parameters[1], parameters[2], parameters[2], numbers[parameters[2]]))

        elif numbers[i][-1:] == '7':
            if parameters[0] < parameters[1]:
                numbers[parameters[2]] = '1'
            else:
                numbers[parameters[2]] = '0'

        elif numbers[i][-1:] == '8':
            if parameters[0] == parameters[1]:
                numbers[parameters[2]] = '1'
            else:
                numbers[parameters[2]] = '0'

        i += len(parameters) + 1

    return output


def main():
    # input = 1
    # numbers = parse_input("test1")
    # run_intcode(numbers, input)

    input = 1
    numbers = parse_input("input")
    run_intcode(numbers, input)


if __name__ == "__main__":
    main()
