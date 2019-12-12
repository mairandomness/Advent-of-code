
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
    print("len numbers", len(numbers))

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


def robot_run(map, numbers):
    painted = []
    input = []
    x = int(len(map)/2)
    robot = Robot((x, x), 0)

    generator = run_intcode(numbers, input)

    while True:
        if len(painted) % 100 == 0:
            print(len(painted))

        (x, y) = robot.position
        # black 0, white 1
        input.append(str(map[x][y]))

        color_list = ["black", "white"]
        direction_list = ["up", "right", "down", "left"]
        print("Robot is at position {}, facing {}, the tile is {}".format(
            robot.position, direction_list[robot.direction], color_list[int(input[0])]))

        color = next(generator)
        if color == "STOP":
            return painted

        direction = next(generator)
        if direction == "STOP":
            return painted

        print("color: {}, direction: {}".format(color, direction))

        # PAINT

        map[x][y] = color
        painted.append((x, y))

        print("Robot is painting it {}, the map tile is now {}".format(
            color_list[color], color_list[map[x][y]]))

        direc_inst = ["turn left", "turn right"]
        print(direc_inst[direction])

        # GET DIRECTION
        # up right down left
        #  0   1    2    3

        if direction == 0:
            robot.direction += -1
        elif direction == 1:
            robot.direction += 1

        # MOVE
        # up (on the matrix its y-1)
        if robot.direction == 4 or robot.direction == 0:
            robot.direction = 0
            robot.position = (x, y - 1)
        # right
        elif robot.direction == 1:
            robot.position = (x + 1, y)
        # down
        elif robot.direction == 2:
            robot.position = (x, y + 1)
        # left
        elif robot.direction == -1 or robot.direction == 3:
            robot.direction = 3
            robot.position = (x - 1, y)

        print("The new direction is {}, the new position is {}".format(
            direction_list[robot.direction], robot.position))


def creat_map(n):
    line = [0]*n
    map = [line[:] for i in range(n)]
    return map


def main():
    # instrutions = parse_input("test")
    # map = creat_map(10)
    # painted = robot_run(map, instrutions)
    # print(len(set(painted)))

    numbers = parse_input("input")
    map = creat_map(80)
    painted = robot_run(map, numbers)
    print(len(set(painted)))


if __name__ == "__main__":
    main()
