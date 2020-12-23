#!/usr/bin/env python3

from functools import reduce


def parse_input():
    with open("input", "r") as f:
        text = f.read()
    pieces = text.split("\n\n")
    tiles = {int(piece.split("\n")[0].replace(
        "Tile ", "")[:-1]): piece.split("\n")[1:] for piece in pieces}
    return tiles


def get_borders(tile):
    return [tile[0], "".join([line[-1] for line in tile]), tile[-1], "".join([line[0] for line in tile])]


def get_neighbors(tiles):
    neighbors = {tile: [] for tile in tiles.keys()}
    borders_dict = {}
    for tile1 in tiles.keys():
        borders_dict[tile1] = get_borders(tiles[tile1])
        # print(tiles[tile1])
        # print("borders", get_borders(tiles[tile1]))

    for tile1 in tiles.keys():
        for tile2 in tiles.keys():
            if tile1 > tile2:
                if matches(borders_dict[tile1], borders_dict[tile2]):
                    neighbors[tile1].append(tile2)
                    neighbors[tile2].append(tile1)
    return neighbors, borders_dict


def matches(borders1, borders2):
    for border1 in borders1:
        if border1 in borders2:
            return True
            # return (borders1.index(border1), borders2.index(border1))
    borders1_rev = ["".join(reversed(border)) for border in borders1]

    for border1 in borders1_rev:
        if border1 in borders2:
            return True
            # return ("rev", borders1.index(border1), borders2.index(border1))

    return False


def make_map(tiles, neighbors, borders_dict):
    corners = [i for i in neighbors.keys() if len(neighbors[i]) == 2]
    matched = [corners[0]]
    corner = corners[0]
    cur = corner
    tiles[corner] = vertical_flip(tiles[corner])
    map = [line[1:-1] for line in tiles[corner][1:-1]]
    corners = corners[1:]

    while len(map) < 96 or len(map[0]) < 96:
        while len(map[0]) < 96:
            for neighbor in neighbors[cur]:
                if neighbor not in matched:
                    tiles = transform_to_match(cur, neighbor, tiles)
                    if get_borders(tiles[neighbor])[1] == get_borders(tiles[cur])[3]:
                        matched.append(neighbor)
                        for i, line in enumerate(map[:8]):
                            map[i] = tiles[neighbor][1:-1][i][1:-1] + map[i]
                        cur = neighbor

        if len(matched) > 12:
            matched = matched[11:]
        cur = matched.pop(0)
        for neighbor in neighbors[cur]:
            if neighbor not in matched:
                tiles = transform_to_match(cur, neighbor, tiles)

                if get_borders(tiles[neighbor])[2] == get_borders(tiles[cur])[0]:
                    matched.append(neighbor)
                    map = [line[1:-1] for line in tiles[neighbor][1:-1]] + map
                    cur = neighbor
    return map


def transform_to_match(tile1, tile2, tiles):
    borders1 = get_borders(tiles[tile1])
    borders2 = get_borders(tiles[tile2])
    match_this = 0
    i, j = 0, 0
    for border1 in borders1:
        if border1 in borders2:
            (i, j) = borders1.index(border1), borders2.index(border1)
            match_this = border1

    borders2_rev = ["".join(reversed(border)) for border in borders2]

    for border1 in borders1:
        if border1 in borders2_rev:
            (i, j) = borders1.index(border1), borders2_rev.index(border1),
            match_this = border1

    while (j - i) % 4 != 2:
        tiles[tile2] = turn_to_right(tiles[tile2])
        j += 1
        j %= 4

    if get_borders(tiles[tile2])[j] != match_this:
        if j % 2 == 0:
            tiles[tile2] = horizontal_flip(tiles[tile2])
        else:
            tiles[tile2] = vertical_flip(tiles[tile2])

    return tiles


def turn_to_right(matrix):
    new_matrix = ["".join(reversed([line[i] for line in matrix]))
                  for i in range(len(matrix))]
    return new_matrix


def vertical_flip(matrix):
    return list(reversed(matrix))


def horizontal_flip(matrix):
    return ["".join(reversed(line)) for line in matrix]


def find_monsters(map):
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "]

    monsters = [monster]
    for i in range(3):
        monster = turn_to_right(monster)
        monsters.append(monster)
    monsters = monsters + [horizontal_flip(monster) for monster in monsters]
    monsters_coord = []
    map = [list(line) for line in map]
    for monster in monsters:
        cur = []
        for y, line in enumerate(monster):
            for x, char in enumerate(line):
                if char == '#':
                    cur.append((y, x))
        monsters_coord.append(cur)

    for monster in monsters_coord:
        y_max = max([coord[0] for coord in monster])
        x_max = max([coord[1] for coord in monster])
        for y1, line in enumerate(map[:len(map) - y_max]):
            for x1, char in enumerate(line[:len(line) - x_max]):
                is_monster = True
                for (y2, x2) in monster:
                    if map[y1+y2][x1+x2] != '#' and map[y1+y2][x1+x2] != 'O':
                        is_monster = False
                        break
                if is_monster:
                    for (y2, x2) in monster:
                        if map[y1+y2][x1+x2] == '#':
                            map[y1+y2][x1+x2] = 'O'
        if sum([1 for line in map for char in line if char == 'O']) > 0:
            return map
    return map


if __name__ == "__main__":
    tiles = parse_input()
    neighbors, borders_dict = get_neighbors(tiles)
    map = make_map(tiles, neighbors, borders_dict)
    map = find_monsters(map)
    print(sum([1 for line in map for char in line if char == '#']))
    for line in map:
        print("".join(line))
