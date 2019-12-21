import math


def parse_input(inputee):
    with open(inputee, "r") as f:
        text = f.read()[:-1]
        num_list = [int(char) for char in text]
    return num_list


def get_new_list(num_list):
    new_list = []
    for i, num in enumerate(num_list):
        new_elem = 0

        if i >= len(num_list)/2:
            new_elem = sum(num_list[i:])
        elif i >= len(num_list)/3:
            new_elem = sum(num_list[i: 2 * i + 1])
        else:
            generator = pattern_generator(i)
            for j in range(len(num_list)):
                multiply = next(generator)
                # print("multiply by", multiply)
                # print(num_list[j])
                new_elem += multiply * num_list[j]
        new_list.append(abs(new_elem) % 10)
    return new_list


def pattern_generator(posi):
    first_run = True
    while True:
        if first_run:
            for i in range(posi):
                yield 0
        else:
            for i in range(posi + 1):
                yield 0
        for i in range(posi + 1):
            yield 1
        for i in range(posi + 1):
            yield 0
        for i in range(posi + 1):
            yield -1
        first_run = False


def run_n_times(times, num_list):
    for i in range(times):
        num_list = get_new_list(num_list)
        # print(num_list)

    return num_list


def main():
    base_pattern = [0, 1, 0, -1]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(run_n_times(100, numbers))

    # numbers = parse_input("input")
    # base_pattern = [0, 1, 0, -1]
    # print(run_n_times(100, numbers))


if __name__ == "__main__":
    main()
