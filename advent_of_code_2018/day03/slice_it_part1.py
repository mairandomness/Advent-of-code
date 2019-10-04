def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
    lines = text.split("\n")
    lines = [line.split(" ") for line in lines]
    lines = [[line[2][:-1].split(','), line[3].split('x')]for line in lines]
    lines = [[[int(num) for num in coord] for coord in line]for line in lines]
    return lines


def count_claims(fabric, claims):
    for claim in claims:
        line_start = claim[0][1]
        row_start = claim[0][0]
        line_end = line_start + claim[1][1]
        row_end = row_start + claim[1][0]

        for i in range(line_start, line_end):
            for j in range(row_start, row_end):
                fabric[i][j] += 1

    count = 0
    for line in fabric:
        for item in line:
            if item > 1:
                count += 1
    ##print('\n'.join(['\t'.join([str(cell) for cell in row[:10]]) for row in fabric[:10]]))
    return count


def main():
    fabric = [[0] * 1000 for n in range(1000)]
    claims = parse_input()
    #print(count_claims(fabric, claims))


if __name__ == "__main__":
    main()
