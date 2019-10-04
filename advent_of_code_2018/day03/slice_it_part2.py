def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
    lines = text.split("\n")
    lines = [line.split(" ") for line in lines]
    lines = [[line[2][:-1].split(','), line[3].split('x')]for line in lines]
    lines = [[[int(num) for num in coord] for coord in line]for line in lines]
    return lines


def count_claims(fabric, claims):
    ids = set([i for i in range(1, len(claims) + 1)])
    
    for id1, claim1 in enumerate(claims):
        for id2, claim2 in enumerate(claims):
            if claim1[0] < claim2[0]:

                line1_start = claim1[0][1]
                row1_start = claim1[0][0]
                line1_end = line1_start + claim1[1][1]
                row1_end = row1_start + claim1[1][0]

                line2_start = claim2[0][1]
                row2_start = claim2[0][0]
                line2_end = line2_start + claim2[1][1]
                row2_end = row2_start + claim2[1][0]

                if not ((line1_start > line2_end or line2_start > line1_end) or (row1_start > row2_end or row2_start > row1_end)):
                    ids.discard(id1 + 1)
                    ids.discard(id2 +1)
                    # #print("pair")
                    # #print(claim1)
                    # #print(claim2)

    return ids


def main():
    claims = parse_input()
    #print(count_claims(fabric, claims))


if __name__ == "__main__":
    main()
