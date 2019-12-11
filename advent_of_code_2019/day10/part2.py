import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        grid = text.split("\n")
    return grid


def list_asteroids(grid):
    asteroids = {}
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if grid[i][j] == '#':
                asteroids[(j, i)] = []
    return asteroids


def are_collinear(a, b, c):
    (xa, ya) = a
    (xb, yb) = b
    (xc, yc) = c

    dif = (xa - xb) * (yb - yc) - (xb - xc) * (ya - yb)

    if dif == 0:
        return True
    else:
        return False


def b_blocks_c(a, b, c):
    if are_collinear(a, b, c) == False:
        return False

    (xa, ya) = a
    (xb, yb) = b
    (xc, yc) = c
    dxab = (xa - xb)
    dyab = (ya - yb)
    dxac = (xa - xc)
    dyac = (ya - yc)
    if dxab * dxac >= 0 and dyab * dyac >= 0:
        return True
    else:
        return False


def get_distance(a, b):
    (xa, ya) = a
    (xb, yb) = b
    return (abs(xa-xb) + abs(ya-yb))


def get_closest(a, b, c):
    dab = get_distance(a, b)
    dac = get_distance(a, c)
    if a== (11,13) and (b == (11,12) or c == (11, 12)):
        print("dab: {} dac: {}".format(dab,dac))
    if dab < dac:
        return b
    else:
        return c


def find_how_many_are_seen(asteroids):
    for a, list_a in asteroids.items():
        # print("a:", a)

        seen_from_a = asteroids[a]
        # print("seen from a:", seen_from_a)
        for b in asteroids.keys():
            # print("b", b)

            can_be_seen = True
            # check if a seen asteroid blocks the new one
            for c in list_a:
                # print("comparing:", a, b, c)
                if b == c or b == a:
                    can_be_seen = False
                    break

                if b_blocks_c(a, b, c):
                    can_be_seen = False
                    # check if the new asteroid is actually the one seen
                    if a== (11,13) and (b == (11,12) or c == (11, 12)):
                        print("a: {} b: {} c: {}".format(a,b,c))
                        print("closest to a is:", get_closest(a, b, c))
                    if c != get_closest(a, b, c):
                        seen_from_a.remove(c)
                        seen_from_a.append(b)
                    break

            if can_be_seen == True:
                seen_from_a.append(b)
                asteroids[a] = seen_from_a
            # print(seen_from_a)

        # add each asteroid that is seen from a to the
        # list of the respective asteroid

    return asteroids


def order(o, a):
    (xa, ya) = a
    (xo, yo) = o
    dx = float(xa - xo)
    dy = float(ya - yo)
    # on the upper y axis
    if dx == 0 and dy < 0:
        return 0

    # on first quadrant
    if dx > 0 and dy <= 0:
        return 4 +(2 * math.atan(dy/dx))

    # on fourth quadrant
    if dx > 0 and dy > 0:
        return 4 + (2 * math.atan(dy/dx))

    # on lower y axis
    if dx == 0 and dy >= 0:
        return 8

    # on third quadrant
    if dx < 0 and dy > 0:
        return 12 +(2 * math.atan(dy/dx))

    # on sencond quadrant
    if dx < 0 and dy <= 0:
        return 12 + (2 * math.atan(dy/dx))
    print(o, a)


def main():
    # print(are_collinear((2,4),(4,6),(6,8)))
    # true
    # print(b_blocks_c((2,4),(4,6),(6,8)))
    # true
    # print(b_blocks_c((4,6),(2,4),(6,8)))
    # false

    #grid = parse_input("test_part2")

    grid = parse_input("input")

    asteroids = list_asteroids(grid)
    dicti = find_how_many_are_seen(asteroids)
    key = max(dicti, key=lambda key: len(dicti[key]))

    base = key
    asteroids = dicti[key]
    final_list = sorted(asteroids, key=lambda x: order(base, x))
    for i, num in enumerate(final_list):
        print("blasted", i+1, " point ", num, " order:", order(base, num))

    print("200th:", final_list[199])


if __name__ == "__main__":
    main()
