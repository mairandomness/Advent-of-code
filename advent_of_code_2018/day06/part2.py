TOTAL_D = 10000

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    lines = text.split("\n")
    lines = [line.split(", ") for line in lines]
    coords = [(int(a), int(b)) for [a, b] in lines]
    return coords


def count_points(coords):
    n = int(TOTAL_D/len(coords))
    max_x = max([a for (a, b) in coords]) + n
    min_x = min([a for (a, b) in coords]) - n
    max_y = max([b for (a, b) in coords]) + n
    min_y = min([b for (a, b) in coords]) - n

    y_range = range(min_y, max_y)
    x_range = range(min_x, max_x)

    count = 0

    for y in y_range:
        for x in x_range:
            dist = 0
            for coord in coords:
                dist += distance((x, y), coord)
                if dist >= TOTAL_D:
                    break
            if dist < TOTAL_D:
                count += 1

    return count


def distance(point_A, point_B):
    (a, b) = point_A
    (c, d) = point_B
    return abs(a - c) + abs(b - d)


def main():
    coords = parse_input()
    print(count_points(coords))


if __name__ == "__main__":
    main()
