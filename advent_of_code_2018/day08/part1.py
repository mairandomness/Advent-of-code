

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    lines = text[:-1].split(" ")
    numbers_cp = [int(line) for line in lines]
    return numbers_cp


def sum_metadata(numbers_cp):
    metadata = []
    metadata_lens = 0
    while len(numbers_cp) > 0:
        #print(numbers_cp)
        if len(metadata) == 0:
            numbers_cp = numbers_cp[2:]
            metadata += numbers_cp[-numbers_cp[1]:]
            numbers_cp = numbers_cp[:-numbers_cp[1]]
        else:
            metadata_lens += numbers_cp[1]
            if numbers_cp[0] == 0:
                numbers_cp = numbers_cp[2:]
                metadata += numbers_cp[:metadata_lens]
                numbers_cp = numbers_cp[metadata_lens:]
                metadata_lens = 0
            else:
                numbers_cp = numbers_cp[2:]

    return sum(metadata)


def main():
    numbers_cp = parse_input()
    print(sum_metadata(numbers_cp))


if __name__ == "__main__":
    main()
