
import curses
import copy
import random


class Game_state:
    def __init__(self, numbers, game_map, i):
        initial = int(len(game_map)/2)
        self.numbers = numbers
        self.numbers_i = i
        # self.numbers_params = []
        self.game_map = game_map
        self.droid_position = (initial, initial)
        self.droid_direction = 'N'


def parse_input(inputi):
    with open(inputi, "r") as f:
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


def decode_key(c, stdscr, game):
    if c == 'KEY_LEFT':
        c = '3'
        game.droid_direction = 'W'
    elif c == 'KEY_RIGHT':
        c = '4'
        game.droid_direction = 'E'
    elif c == 'KEY_UP':
        c = '1'
        game.droid_direction = 'N'
    elif c == 'KEY_DOWN':
        c = '2'
        game.droid_direction = 'S'
    else:
        c = stdscr.getkey()
        (c, game) = decode_key(c, stdscr, game)
    return (c, game)


def decide_where_next(game):
    (y, x) = game.droid_position
    indexes = []
    instructions = ['1', '2', '3', '4']
    directions = ['N', 'S', 'W', 'E']
    neighboring_coords = [(y-1, x), (y+1, x), (y, x-1), (y, x + 1)]
    neighboring_tiles = [game.game_map[a][b] for (a, b) in neighboring_coords]
    # print(neighboring_tiles)
    if '=' not in neighboring_tiles and '.' in neighboring_tiles:
        n = neighboring_tiles.index('.')
    elif '=' not in neighboring_tiles and '.' not in neighboring_tiles:
        for i, tile in enumerate(neighboring_tiles):
            if tile == ':':
                indexes.append(i)
        n = random.choice(indexes)

    else:
        for i, tile in enumerate(neighboring_tiles):
            if tile == '=':
                indexes.append(i)
        n = random.choice(indexes)
    c = instructions[n]
    game.droid_direction = directions[n]
    return (c, game)


def run_intcode(game, stdscr):

    base = 0
    i = 0
    output = 0

    # max_num = int(max(game.numbers, key=lambda x: len(x)))
    max_num = 999999
    if len(game.numbers) < max_num:
        game.numbers = game.numbers + (max_num - len(game.numbers)) * ['0']

    while True:
        print_map(stdscr, game)
        if game.numbers[i] == "99":
            print("STAAAP")
            yield "STOP"

        parameters = get_parameters(game.numbers, i, base)

        if game.numbers[i][-1:] == '3':
            print("press something")
            # c = stdscr.getkey()
            # (c, game) = decode_key(c, stdscr, game)
            (c, game) = decide_where_next(game)
            game.numbers[parameters[0]] = c

        elif game.numbers[i][-1:] == '4':
            if game.numbers[i] == "104":
                output = parameters[0]
            else:
                output = game.numbers[parameters[0]]
            yield int(output)
            # print("OTPUT:", output)

        elif game.numbers[i][-1:] == '9':
            base += parameters[0]
            # print("Add value {} to base, resulting in {}".format(parameters[0], base))

        elif game.numbers[i][-1:] == '5':
            if parameters[0] != 0:
                i = parameters[1] - 3

        elif game.numbers[i][-1:] == '6':
            if parameters[0] == 0:
                i = parameters[1] - 3

        elif game.numbers[i][-1:] == '1':
            game.numbers[parameters[2]] = str(parameters[0] + parameters[1])
            # print("puts {} + {} at position {} so game.numbers_cp[{}] = {}".format(
            #                 parameters[0], parameters[1], parameters[2], parameters[2], game.numbers[parameters[2]]))

        elif game.numbers[i][-1:] == '2':
            game.numbers[parameters[2]] = str(parameters[0] * parameters[1])
            # print("puts {} * {} at position {} so game.numbers_cp[{}] = {}".format(
            #     parameters[0], parameters[1], parameters[2], parameters[2], game.numbers[parameters[2]]))

        elif game.numbers[i][-1:] == '7':
            if parameters[0] < parameters[1]:
                game.numbers[parameters[2]] = '1'
            else:
                game.numbers[parameters[2]] = '0'

        elif game.numbers[i][-1:] == '8':
            if parameters[0] == parameters[1]:
                game.numbers[parameters[2]] = '1'
            else:
                game.numbers[parameters[2]] = '0'

        i += len(parameters) + 1
        game.numbers_i = i


def print_map(stdscr, game):
    stdscr.clear()
    initial_pos = int(len(game.game_map)/2)

    for y in range(len(game.game_map)):
        for x in range(len(game.game_map[0])):
            if (y, x) == game.droid_position:
                stdscr.addch(y, x, 'D')
            elif (y, x) == (initial_pos, initial_pos):
                stdscr.addch(y, x, 'X')
            else:
                stdscr.addch(y, x, game.game_map[y][x])
    stdscr.refresh()
    return None


def run_game(game, stdscr):
    generator = run_intcode(game, stdscr)
    n = 0
    brick = 0
    counter = 0
    found_hole = False
    initial_pos = int(len(game.game_map)/2)
    initial_pos = (initial_pos, initial_pos)

    while True:
        print_map(stdscr, game)
        (y, x) = game.droid_position

        directions = ['N', 'S', 'W', 'E']
        neighboring_coords = [(y-1, x), (y+1, x), (y, x-1), (y, x + 1)]

        response = next(generator)

        (ny, nx) = neighboring_coords[directions.index(
            game.droid_direction)]

        if response == "STOP":
            break

        elif response == 0:
            game.game_map[ny][nx] = 'W'

        elif response == 1:
            if game.game_map[ny][nx] == '=':
                game.game_map[ny][nx] = '.'

            elif game.game_map[ny][nx] == '.':
                game.game_map[ny][nx] = ":"

            game.droid_position = (ny, nx)

        elif response == 2:
            brick = 'O'
            game.droid_position = (ny, nx)
            found_hole = True

        if found_hole:
            print("found hole after")
            for line in game.game_map:
                for tile in line:
                    if tile == ".":
                        counter += 1
            print(counter)
            break

        stdscr.clear()
        n += 1

    return counter


def create_map(n):
    line = ['=']*n
    game_map = [line[:] for i in range(n)]
    return game_map


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    game_map = create_map(100)
    numbers = parse_input("input")
    game = Game_state(numbers, game_map, 0)
    print(run_game(game, stdscr))


if __name__ == "__main__":
    main()
