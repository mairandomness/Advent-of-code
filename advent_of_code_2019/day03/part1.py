def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
        result = []
        for line in lines:
            line1 = line.split(",")
            result.append([(direction[0], int(direction[1:]))
                           for direction in line1])
        return result


def register_point(n, currently_at, map, crossing):
    if sum([abs(coord) for coord in currently_at]) < 1000:
        if currently_at in map.keys():
            map[currently_at][n] = 1
            if map[currently_at] == [1, 1]:
                crossing.append(currently_at)

        else:
            map[currently_at] = [0, 0]
            map[currently_at][n] = 1

    return(currently_at, map, crossing)


def draw_lines(instructions):
    map = {}
    crossing = []

    for n, line in enumerate(instructions):
        currently_at = (0, 0)
        for order in line:
            if order[0] == 'R':
                for i in range(order[1]):
                    currently_at = (currently_at[0] + 1, currently_at[1])
                    (currently_at, map, crossing) = register_point(
                        n, currently_at, map, crossing)

            if order[0] == 'L':
                for i in range(order[1]):
                    currently_at = (currently_at[0] - 1, currently_at[1])
                    (currently_at, map, crossing) = register_point(
                        n, currently_at, map, crossing)

            if order[0] == 'U':
                for i in range(order[1]):
                    currently_at = (currently_at[0], currently_at[1] + 1)
                    (currently_at, map, crossing) = register_point(
                        n, currently_at, map, crossing)

            if order[0] == 'D':
                for i in range(order[1]):
                    currently_at = (currently_at[0], currently_at[1] -
                                    1)
                    (currently_at, map, crossing) = register_point(
                        n, currently_at, map, crossing)

    print(crossing)
    crossing = [abs(coord[0]) + abs(coord[1]) for coord in crossing]
    return sorted(crossing)


def main():
    instructions = parse_input()
    print(draw_lines(instructions))


if __name__ == "__main__":
    main()
