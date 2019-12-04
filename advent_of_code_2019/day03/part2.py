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


def register_point(n, steps, currently_at, map, crossing):
    if currently_at in map.keys():
        if map[currently_at][n] == 0:
            map[currently_at][n] = 1
        if map[currently_at][:-1] == [1, 1]:
            crossing.append([currently_at, steps + map[currently_at][2]])

    else:
        map[currently_at] = [0, 0, steps]
        map[currently_at][n] = 1

    return(currently_at, map, crossing)


def draw_lines(instructions):
    map = {}
    crossing = []
    currently_at = [(0, 0), (0, 0)]
    steps = [0, 0]
    keep_checking_until = 99999999

    for order in range(len(instructions[0])):
        for line in range(2):
            if instructions[line][order][0] == 'R':
                for i in range(instructions[line][order][1]):
                    currently_at[line] = (
                        currently_at[line][0] + 1, currently_at[line][1])
                    steps[line] += 1
                    (currently_at[line], map, crossing) = register_point(
                        line, steps[line], currently_at[line], map, crossing)

            if instructions[line][order][0] == 'L':
                for i in range(instructions[line][order][1]):
                    currently_at[line] = (
                        currently_at[line][0] - 1, currently_at[line][1])
                    steps[line] += 1
                    (currently_at[line], map, crossing) = register_point(
                        line, steps[line], currently_at[line], map, crossing)

            if instructions[line][order][0] == 'U':
                for i in range(instructions[line][order][1]):
                    currently_at[line] = (
                        currently_at[line][0], currently_at[line][1] + 1)
                    steps[line] += 1
                    (currently_at[line], map, crossing) = register_point(
                        line, steps[line], currently_at[line], map, crossing)

            if instructions[line][order][0] == 'D':
                for i in range(instructions[line][order][1]):
                    currently_at[line] = (
                        currently_at[line][0], currently_at[line][1] - 1)
                    steps[line] += 1
                    (currently_at[line], map, crossing) = register_point(
                        line, steps[line], currently_at[line], map, crossing)

            if len(crossing) > 0:
                print(crossing)
                crossing.sort(key=lambda x: x[1])
                keep_checking_until = crossing[0][1]
                if min(steps) > keep_checking_until:
                    return sorted(crossing, key=lambda x: x[1])

    return sorted(crossing, key=lambda x: x[1])


def main():
    instructions = parse_input()
    print(draw_lines(instructions))


if __name__ == "__main__":
    main()
