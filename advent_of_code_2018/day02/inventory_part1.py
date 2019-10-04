def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
    lines = text.split("\n")
    return lines


def checksum(lines):
    two_times = [0]*len(lines)
    three_times = [0]*len(lines)

    for i, line in enumerate(lines):

        for letter in line:

            if line.count(letter) == 2:
                two_times[i] = 1

            if line.count(letter) == 3:
                three_times[i] = 1
    
    return sum(two_times) * sum(three_times)


def main():
    lines = parse_input()
    #print(checksum(lines))


if __name__ == "__main__":
    main()
