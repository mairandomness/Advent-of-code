def parse_input():
    with open("input", "r") as f:
        text = f.read()
    return text.split("\n")


def flip(instructions):
    map = {}

    for inst in instructions:
        line = 0
        col = 0
        i = 0
        while i < len(inst):
            if col % 2 == 0:
                if inst[i] == 'e':
                    line += 1
                elif inst[i] == 'w':
                    line -= 1
                elif inst[i:i+2] == "ne":
                    col += 1
                    i += 1
                elif inst[i:i+2] == "nw":
                    line -= 1
                    col += 1
                    i += 1
                elif inst[i:i+2] == "se":
                    col -= 1
                    i += 1
                elif inst[i:i+2] == "sw":
                    line -= 1
                    col -= 1
                    i += 1
            else:
                if inst[i] == 'e':
                    line += 1
                elif inst[i] == 'w':
                    line -= 1
                elif inst[i:i+2] == "ne":
                    col += 1
                    line += 1
                    i += 1
                elif inst[i:i+2] == "nw":
                    col += 1
                    i += 1
                elif inst[i:i+2] == "se":
                    col -= 1
                    line += 1
                    i += 1
                elif inst[i:i+2] == "sw":
                    col -= 1
                    i += 1
            i += 1

        if (line, col) in map.keys():
            map[(line, col)] = not map[(line, col)]
        else:
            map[(line, col)] = False
    return map


def get_neighbors(tile):
    l, c = tile
    if c % 2 == 0:
        neighbors = [(l + 1, c), (l - 1, c), (l, c + 1),
                     (l - 1, c + 1), (l, c - 1), (l - 1, c - 1)]
    else:
        neighbors = [(l + 1, c), (l - 1, c), (l + 1, c + 1),
                     (l, c + 1), (l + 1, c - 1), (l, c - 1)]
    return neighbors


def conway(map):
    new_tiles = []
    new_map = {}

    for curr in map.keys():
        neighbors = get_neighbors(curr)
        if not map[curr]:
            new_tiles += [tile for tile in neighbors if tile not in map.keys()]
        neighbors = sum(1 for i in [map.get(k, True)
                                    for k in neighbors] if not i)

        if not map[curr] and (neighbors > 2 or neighbors == 0):
            new_map[curr] = True
        elif map[curr] and neighbors == 2:
            new_map[curr] = False
        else:
            new_map[curr] = map[curr]

    new_tiles = list(set(new_tiles))
    for curr in new_tiles:
        neighbors = get_neighbors(curr)
        neighbors = sum(1 for i in [map.get(k, True)
                                    for k in neighbors] if not i)

        if  neighbors == 2:
            new_map[curr] = False

    return new_map


if __name__ == "__main__":
    instructions = parse_input()
    map = flip(instructions)
    print(sum([1 for i in map.values() if not i]))
    for i in range(100):
        map = conway(map)
        print(sum([1 for i in map.values() if not i]))
