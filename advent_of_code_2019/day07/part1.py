# Did some refactoring to reuse this code on day 9
# It was kinda unsustainable

import itertools


def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [line for line in lines]


def get_parameters(numbers, i):
    # print("numbers[i], i",numbers[i], i)
    if numbers[i] == '99':
        return []

    elif numbers[i][-1:] == '3' or numbers[i][-1:] == '4':
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
        if mode[j] == 1 or j == 2 or numbers[i] == '3' or numbers[i] == '4':
            parameters[j] = int(numbers[i+j+1])
        else:
            address = int(numbers[i+j+1])
            parameters[j] = int(numbers[address])

    # print("parameters:", parameters)

    return parameters


def run_intcode(numbers_original, phase, input):
    numbers = numbers_original[:]
    i = 0
    output = 0

    inputees = [str(phase), str(input)]
    while True:

        if numbers[i] == "99":
            return output

        parameters = get_parameters(numbers, i)

        if numbers[i] == '3':
            numbers[int(numbers[i+1])] = inputees[0]
            # print("puts input {} at position {} so numbers[{}] = {}".format(
            #      inputees[0], parameters[0], parameters[0], numbers[parameters[0]]))
            inputees.pop(0)

        elif numbers[i][-1:] == '4':
            if numbers[i] == "104":
                output = parameters[0]
            else:
                output = numbers[parameters[0]]
            print("OTPUT:", output)

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


def run_amplifiers(numbers, phase_setting):
    input = 0
    for i in range(5):
        input = run_intcode(numbers, phase_setting[i], input)
        print("finished run", i)
        print("output of this run", input)
    return input


def run_all_amplifiers(numbers):
    phase_settings = itertools.permutations('01234', 5)
    phase_settings = [list(phase_setting) for phase_setting in phase_settings]
    to_truster = []
    print(len(phase_settings))
    for phase_setting in phase_settings:
        phase_setting = [int(phase) for phase in phase_setting]
        to_truster.append(int(run_amplifiers(numbers, phase_setting)))
    return to_truster


def main():
    # numbers = parse_input("test1")
    # print(run_amplifiers(numbers, [4,3,2,1,0]))
    # 43210

    #numbers = parse_input("test2")
    #print(run_amplifiers(numbers, [0,1,2,3,4]))
    # 54321

    numbers = parse_input("input")
    print(max(run_all_amplifiers(numbers)))


if __name__ == "__main__":
    main()
