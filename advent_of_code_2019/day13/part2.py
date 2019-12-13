# created class game state, have to refactor the rest
import curses
import itertools
import copy


class Game_state:
    def __init__(self, numbers, game_map, i):
        self.numbers = numbers
        self.numbers_i = i
        self.game_map = game_map
        self.saved_map = copy.deepcopy(game_map)
        self.saved_numbers = numbers[:]
        self.saved_numbers_i = i

    def save(self):
        self.saved_map = copy.deepcopy(self.game_map)
        self.saved_numbers = self.numbers[:]
        self.saved_numbers_i = self.numbers_i

    def load(self):
        self.game_map = copy.deepcopy(self.saved_map)
        self.numbers = self.saved_numbers[:]
        self.numbers_i = self.saved_numbers_i


def parse_inputi(inputi):
    with open(inputi, "r") as f:
        text = f.read()[:-1]
        lines = text.split(",")
    return [line for line in lines]


def get_parameters(numbers, i, base):
    # print("game.numbers[i], i",game.numbers[i], i)
    if numbers[i] == '99':
        return []

    elif numbers[i][-1:] == '3' or numbers[i][-1:] == '4' or numbers[i][-1:] == '9':
        n_params = 1

    elif numbers[i][-1:] == '5' or numbers[i][-1:] == '6':
        n_params = 2

    elif numbers[i][-1:] == '1' or numbers[i][-1:] == '2' or numbers[i][-1:] == '7' or numbers[i][-1:] == '8':
        n_params = 3
    # print(game.numbers[i][-1:])
    # print("instructions:", game.numbers[i : i + n_params + 1])

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
    if c == 's':
        game.savednumbers = game.numbers[:]
        game.saved_map = copy.deepcopy(game.game_map)
        c = stdscr.getkey()
        (c, game) = decode_key(c, stdscr, game)

    if c == 'l':
        # LOAD
        game.numbers = game.saved_numbers[:]
        game.game_map = copy.deepcopy(game.saved_map)
        c = stdscr.getkey()
        (c, game) = decode_key(c, stdscr, game)

    if c == 'KEY_LEFT':
        c = '-1'
    elif c == 'KEY_RIGHT':
        c = '1'
    elif c == 'KEY_UP' or c == 'KEY_DOWN':
        c = '0'
    else:
        c = stdscr.getkey()
        (c, game) = decode_key(c, stdscr, game)
    return (c, game)


def run_intcode(game, stdscr):
    base = 0
    i = game.numbers_i
    output = 0

    # max_num = int(max(game.numbers, key=lambda x: len(x)))
    max_num = 999999
    if len(game.numbers) < max_num:
        game.numbers = game.numbers + (max_num - len(game.numbers)) * ['0']
    print("len game.numbers", len(game.numbers))

    while True:

        if game.numbers[i] == "99":
            yield "STOP"

        parameters = get_parameters(game.numbers, i, base)

        if game.numbers[i][-1:] == '3':
            c = stdscr.getkey()
            (c, game) = decode_key(c, stdscr, game)
            i = game.numbers_i
            parameters = get_parameters(game.numbers, i, base)

            game.numbers[parameters[0]] = c
            # print("puts inputi {} at position {} so game.numbers[{}] = {}".format(
            #      inputiees[0], parameters[0], parameters[0], game.numbers[parameters[0]]))

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


def run_game(game, stdscr):
    game.numbers[0] = '2'
    generator = run_intcode(game, stdscr)
    args = [0, 0, 0]
    n_blocks = 1
    n = 0

    while True:

        print_map(stdscr, game.game_map)

        for i in range(3):
            args[i] = next(generator)
            if args[i] == 'STOP':
                break
        if args[i] == 'STOP':
            break

        [x, y, tile_id] = args

        if x == -1 and y == 0:
            player_score = tile_id
            n_blocks = count_blocks(game.game_map)
            if n_blocks == 0 and n > 5000:
                curses.nocbreak()
                stdscr.keypad(False)
                curses.echo()
                curses.endwin()
                print(player_score)
                break

        else:
            game.game_map[y][x] = tile_id

            stdscr.clear()
        n += 1

    return n_blocks


def count_blocks(game_map):
    n = 0
    for i in range(len(game_map)):
        for i in range(len(game_map)):
            if game_map == 2:
                n += 1
    return n


def print_map(stdscr, game_map):
    next = 0
    previous = 0
    for y in range(25):
        for x in range(44):
            # if x != 43:
            #     next = game_map[y][x+1]
            # if x != 0:
            #     previous = game_map[y][x-1]

            char = game_map[y][x]

            if char == 3 or next == 3 or previous == 3:
                display_char = "T"
                next = 0
            elif char == 0:
                display_char = "."
            elif char == 1:
                display_char = "W"
            elif char == 2:
                display_char = "▓"
            elif char == 4:
                display_char = "o"

            stdscr.addch(y, x, display_char)
    stdscr.refresh()
    return None


def create_map(n):
    line = [0]*n
    game_map = [line[:] for i in range(n)]
    return game_map


def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)

    game_map = create_map(44)
    numbers = parse_inputi("input")
    game = Game_state(numbers, game_map, 0)
    print(run_game(game, stdscr))


if __name__ == "__main__":
    main()
