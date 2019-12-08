import itertools

def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [line for line in lines]


def run_intcode(numbers, phase, input):
    i = 0
    inputees = [str(phase), str(input)]
    # print(numbers)
    # print("len numbers", len(numbers))
    while True:
        if numbers[i] == "99":
            break

        elif numbers[i] == '3':
            # print("instructions", numbers[i], numbers[i+1])
            numbers[int(numbers[i+1])] = inputees[0]
            inputees = inputees[1:]
            # print("puts input {} at position {} so numbers[{}] = {}".format(
            #  input, numbers[i+1], numbers[i+1], numbers[int(numbers[i+1])]))
            i += 2

        elif numbers[i] == '103':
            numbers[i+1] = inputees[0]
            inputees = inputees[1:]
            i += 2

        elif numbers[i] == '4':
            # print("instructions", numbers[i], numbers[i+1])
            output = numbers[int(numbers[i+1])]
            # print(output)
            i += 2

        elif numbers[i] == '104':
            # print("instructions", numbers[i], numbers[i+1])
            output = numbers[i+1]
            # print(output)
            i += 2

        # TAKE 2 PARAMETERS
        elif numbers[i][-1:] == '5' or numbers[i][-1:] == '6':
            parameters = [0, 0]
            mode = [int(char) for char in str(numbers[i][:-2])]
            while len(mode) < 2:
                mode = [0] + mode

            mode.reverse()
            # print("instructions", numbers[i],
            #    numbers[i+1], numbers[i+2])
            # print("modes", mode)
            for j in range(2):
                if mode[j] == 1:
                    parameters[j] = int(numbers[i+j+1])
                else:
                    address = int(numbers[i+j+1])
                    parameters[j] = int(numbers[address])

            # print("parameters:", parameters)
            if numbers[i][-1:] == '5':
                if parameters[0] != 0:
                    i = parameters[1]
                    # print("if {} != 0, change i to {}".format(
                    #   parameters[0], i))
                else:
                    i += 3

            elif numbers[i][-1:] == '6':
                if parameters[0] == 0:
                    i = parameters[1]
                    # print("if {} == 0, change i to {}".format(
                    #   parameters[0], i))
                else:
                    i += 3

        # TAKE 3 PARAMETERS
        else:
            parameters = [0, 0, 0]
            # print("numbers[i][:-2]", numbers[i][:-2])
            mode = [int(char) for char in str(numbers[i][:-2])]
            while len(mode) < 3:
                mode = [0] + mode

            mode.reverse()
            
            for j in range(3):
                if mode[j] == 1 or j == 2:
                    parameters[j] = int(numbers[i+j+1])
                else:
                    address = int(numbers[i+j+1])
                    parameters[j] = int(numbers[address])

            if numbers[i][-1:] == '1':
                numbers[parameters[2]] = str(parameters[0] + parameters[1])
                # print("puts {} + {} at position {} so numbers[{}] = {}".format(
                #   parameters[0], parameters[1], parameters[2], parameters[2], numbers[parameters[2]]))

            elif numbers[i][-1:] == '2':
                numbers[parameters[2]] = str(parameters[0] * parameters[1])
                # print("puts {} * {} at position {} so numbers[{}] = {}".format(
                #   parameters[0], parameters[1], parameters[2], parameters[2], numbers[parameters[2]]))

            elif numbers[i][-1:] == '7':
                # print("mode", mode)
                if parameters[0] < parameters[1]:
                    numbers[parameters[2]] = '1'
                    # print("{} < {} puts 1 at position {}".format(
                    #     parameters[0], parameters[1], parameters[2]))
                else:
                    numbers[parameters[2]] = '0'
            elif numbers[i][-1:] == '8':
                # print("mode", mode)
                if parameters[0] == parameters[1]:
                    numbers[parameters[2]] = '1'
                    # print("{} == {}, puts 1 at position {} numbers[{}] = {} ".format(
                    #     parameters[0], parameters[1], parameters[2], parameters[2], numbers[parameters[2]]))

                else:
                    numbers[parameters[2]] = '0'
                    # print("{} != {}, puts 0 at position {} numbers[{}] = {} ".format(
                    #     parameters[0], parameters[1], parameters[2], parameters[2], numbers[parameters[2]]))

            i += 4
    return output

def run_amplifiers(numbers, phase_setting):
    input = 0
    for i in range(5):
        input = run_intcode(numbers, phase_setting[i], input)
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
