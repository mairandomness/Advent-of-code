# decided to play around with generators
import itertools


def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [line for line in lines]


def run_intcode(numbers, inputees):
    numbers_cp = numbers[:]
    i = 0
    output = '0'
    # print(numbers_cp)
    # print("len numbers_cp", len(numbers_cp))
    while True:
        if numbers_cp[i] == "99":
            yield 'STOP'
            break

        elif numbers_cp[i] == '3':
            if len(inputees) != 0:
                # print("instructions", numbers_cp[i], numbers_cp[i+1])
                numbers_cp[int(numbers_cp[i+1])] = inputees[0]
                inputees.pop(0)
                # print("puts input {} at position {} so numbers_cp[{}] = {}".format(
                #  input, numbers_cp[i+1], numbers_cp[i+1], numbers_cp[int(numbers_cp[i+1])]))
                i += 2
            else:
                yield None

        elif numbers_cp[i] == '103':
            if len(inputees) != 0:
                numbers_cp[i+1] = inputees[0]
                inputees.pop(0)
                i += 2
            else:
                yield None

        elif numbers_cp[i] == '4':
            # print("instructions", numbers_cp[i], numbers_cp[i+1])
            output = numbers_cp[int(numbers_cp[i+1])]
            yield output
            i += 2

        elif numbers_cp[i] == '104':
            # print("instructions", numbers_cp[i], numbers_cp[i+1])
            output = numbers_cp[i+1]
            yield output
            i += 2

        # TAKE 2 PARAMETERS
        elif numbers_cp[i][-1:] == '5' or numbers_cp[i][-1:] == '6':
            parameters = [0, 0]
            mode = [int(char) for char in str(numbers_cp[i][:-2])]
            while len(mode) < 2:
                mode = [0] + mode

            mode.reverse()
            # print("instructions", numbers_cp[i],
            #    numbers_cp[i+1], numbers_cp[i+2])
            # print("modes", mode)
            for j in range(2):
                if mode[j] == 1:
                    parameters[j] = int(numbers_cp[i+j+1])
                else:
                    address = int(numbers_cp[i+j+1])
                    parameters[j] = int(numbers_cp[address])

            # print("parameters:", parameters)
            if numbers_cp[i][-1:] == '5':
                if parameters[0] != 0:
                    i = parameters[1]
                    # print("if {} != 0, change i to {}".format(
                    #   parameters[0], i))
                else:
                    i += 3

            elif numbers_cp[i][-1:] == '6':
                if parameters[0] == 0:
                    i = parameters[1]
                    # print("if {} == 0, change i to {}".format(
                    #   parameters[0], i))
                else:
                    i += 3

        # TAKE 3 PARAMETERS
        else:
            parameters = [0, 0, 0]
            # print("numbers_cp[i][:-2]", numbers_cp[i][:-2])
            mode = [int(char) for char in str(numbers_cp[i][:-2])]
            while len(mode) < 3:
                mode = [0] + mode

            mode.reverse()

            for j in range(3):
                if mode[j] == 1 or j == 2:
                    parameters[j] = int(numbers_cp[i+j+1])
                else:
                    address = int(numbers_cp[i+j+1])
                    parameters[j] = int(numbers_cp[address])

            if numbers_cp[i][-1:] == '1':
                numbers_cp[parameters[2]] = str(parameters[0] + parameters[1])
                # print("puts {} + {} at position {} so numbers_cp[{}] = {}".format(
                #   parameters[0], parameters[1], parameters[2], parameters[2], numbers_cp[parameters[2]]))

            elif numbers_cp[i][-1:] == '2':
                numbers_cp[parameters[2]] = str(parameters[0] * parameters[1])
                # print("puts {} * {} at position {} so numbers_cp[{}] = {}".format(
                #   parameters[0], parameters[1], parameters[2], parameters[2], numbers_cp[parameters[2]]))

            elif numbers_cp[i][-1:] == '7':
                # print("mode", mode)
                if parameters[0] < parameters[1]:
                    numbers_cp[parameters[2]] = '1'
                    # print("{} < {} puts 1 at position {}".format(
                    #     parameters[0], parameters[1], parameters[2]))
                else:
                    numbers_cp[parameters[2]] = '0'
            elif numbers_cp[i][-1:] == '8':
                # print("mode", mode)
                if parameters[0] == parameters[1]:
                    numbers_cp[parameters[2]] = '1'
                    # print("{} == {}, puts 1 at position {} numbers_cp[{}] = {} ".format(
                    #     parameters[0], parameters[1], parameters[2], parameters[2], numbers_cp[parameters[2]]))

                else:
                    numbers_cp[parameters[2]] = '0'
                    # print("{} != {}, puts 0 at position {} numbers_cp[{}] = {} ".format(
                    #     parameters[0], parameters[1], parameters[2], parameters[2], numbers_cp[parameters[2]]))

            i += 4



def gen_zero():
    yield '0'


def a_ant(generatorE):
    i = 0
    while True:
        if i == 0:
            i = 1
            yield '0'
        else:
            yield(next(generatorE))


def run_amplifiers(numbers, phase_setting):
    phase_setting = [str(phase) for phase in phase_setting]
    inputA = [phase_setting[0], '0']
    inputB = [phase_setting[1]]
    inputC = [phase_setting[2]]
    inputD = [phase_setting[3]]
    inputE = [phase_setting[4]]

    generatorA = run_intcode(numbers, inputA)
    generatorB = run_intcode(numbers, inputB)
    generatorC = run_intcode(numbers, inputC)
    generatorD = run_intcode(numbers, inputD)
    generatorE = run_intcode(numbers, inputE)

    temp = "0"
    while temp != 'STOP':
        temp = 0
        #print("inputA", inputA)
        result = inputA[0]
        temp = next(generatorA)
        if temp == 'STOP':
            break
        if temp != None:
            inputB.append(temp)


        # print("inputB", inputB)
        
        temp= 0
        temp = next(generatorB)
        if temp != None:
            inputC.append(temp)

        temp = 0
        temp = next(generatorC)
        if temp != None:
            inputD.append(temp)
        
        temp = 0
        temp = next(generatorD)
        if temp != None:
            inputE.append(temp)

        # print("inputE", inputE)
        temp = 0

        temp = next(generatorE)
        if temp != None:
            inputA.append(temp)   
    return result


def run_all_amplifiers(numbers):
    phase_settings = itertools.permutations('56789', 5)
    phase_settings = [list(phase_setting) for phase_setting in phase_settings]
    to_truster = []
    print(len(phase_settings))
    for phase_setting in phase_settings:
        phase_setting = [int(phase) for phase in phase_setting]
        to_truster.append(int(run_amplifiers(numbers, phase_setting)))
    return to_truster


def main():
    # numbers_cp = parse_input("test1_part2")
    # print(run_amplifiers(numbers_cp, [9, 8, 7, 6, 5]))
    # 139629729

    #numbers_cp = parse_input("test2")
    #print(run_amplifiers(numbers_cp, [0,1,2,3,4]))
    # 54321

    numbers = parse_input("input")
    print(max(run_all_amplifiers(numbers)))


if __name__ == "__main__":
    main()
