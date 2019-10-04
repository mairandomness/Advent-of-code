def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        text = text.replace('+', '')
    lines = text.split("\n")
    return [int(line) for line in lines]


def main():
    numbers = parse_input()

    i = 0
    cur_freq = 0
    freqs = [0]
    not_found = True

    while not_found:
        for number in numbers:
            cur_freq += number
            # if we saw this freq before, we are done
            if (cur_freq in freqs):
                #print(cur_freq)
                not_found = False
                break

            freqs.append(cur_freq)


if __name__ == "__main__":
    main()
