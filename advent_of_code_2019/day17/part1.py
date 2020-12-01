
class Robot:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction


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


def run_intcode(numbers, input):
    base = 0
    i = 0
    output = 0

    # max_num = int(max(numbers, key=lambda x: len(x)))
    max_num = 999999
    if len(numbers) < max_num:
        numbers = numbers + (max_num - len(numbers)) * ['0']

    while True:

        if numbers[i] == "99":
            print("PLZSTAP")
            yield "STOP"

        parameters = get_parameters(numbers, i, base)

        if numbers[i][-1:] == '3':
            numbers[parameters[0]] = input[0]
            # print("puts input {} at position {} so numbers[{}] = {}".format(
            #      input[0], parameters[0], parameters[0], numbers[parameters[0]]))
            input.pop(0)

        elif numbers[i][-1:] == '4':
            if numbers[i] == "104":
                output = parameters[0]
            else:
                output = numbers[parameters[0]]
            yield int(output)

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


def get_map(numbers, inputi):
    map_view = []
    cur_line = []
    generator = run_intcode(numbers, inputi)
    while True:
        response = next(generator)
        if response == 'STOP':
            break
        if response == 10:
            map_view.append(cur_line[:])
            cur_line = []
        else:
            cur_line.append(chr(response))
    return map_view[:-1]


def print_map(map_view):
    for y, line in enumerate(map_view):
        print(line)


def get_alignment(map_view):
    align = 0

    for y, line in enumerate(map_view):
        # print("height", len(map_view))
        for x, tile in enumerate(line):
            # print("width", len(line))
            if y != 0 and x != 0 and y != len(map_view) - 1 and x != len(line) - 1 and tile == '#':
                neighboring_coords = [(y-1, x), (y+1, x), (y, x-1), (y, x + 1)]
                neighboring_tiles = [map_view[a][b]
                                     for (a, b) in neighboring_coords]
                if '.' not in neighboring_tiles and 'X' not in neighboring_tiles:
                    align += x*y
    return align


def main():

    numbers = parse_input("input")
    inputi = []
    map_view = get_map(numbers, inputi)
    print_map(map_view)
    print(get_alignment(map_view))


if __name__ == "__main__":
    main()
