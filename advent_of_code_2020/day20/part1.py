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
    return [tile[0], tile[-1], "".join([line[0] for line in tile]), "".join([line[-1] for line in tile])]


def get_neighbors(tiles):
    neighbors = {tile: [] for tile in tiles.keys()}
    borders_dict = {}
    for tile1 in tiles.keys():
        borders_dict[tile1] = get_borders(tiles[tile1])
        # print(tiles[tile1])
        #print("borders", get_borders(tiles[tile1]))

    for tile1 in tiles.keys():
        for tile2 in tiles.keys():
            if tile1 > tile2:
                if matches(borders_dict[tile1], borders_dict[tile2]):
                    neighbors[tile1].append(tile2)
                    neighbors[tile2].append(tile1)
    return neighbors


def matches(borders1, borders2):
    for border1 in borders1:
        if border1 in borders2:
            return True
    borders1_rev = ["".join(reversed(border)) for border in borders1]

    for border1 in borders1_rev:
        if border1 in borders2:
            return True

    return False


if __name__ == "__main__":
    tiles = parse_input()
    neighbors = get_neighbors(tiles)
    corners = [i for i in neighbors.keys() if len(neighbors[i]) == 2]
    print("corners: ", corners)
    print("product: ", reduce((lambda x, y: x * y), corners))
