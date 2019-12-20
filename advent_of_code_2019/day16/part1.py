import math


def parse_input(inputee):
    with open(inputee, "r") as f:
        text = f.read()[:-1]
        num_list = [int(char) for char in text]
    return num_list


def get_new_list(num_list, base_pattern):
    new_list = []
    for i, num in enumerate(num_list):
        cur_pattern = []
        for n in base_pattern:
            cur_pattern += [n]*(i+1)
        cur_pattern = (cur_pattern * math.ceil(len(num_list) /
                                               (len(cur_pattern) - 1)))[1:]
        # print(cur_pattern)
        # print(num_list)
        new_elem = [cur_pattern[i] * num_list[i] for i in range(len(num_list))]
        new_list.append(abs(sum(new_elem)) % 10)
    return new_list


def run_n_times(n, num_list, base_pattern):
    for i in range(n):
        num_list = get_new_list(num_list, base_pattern)
    return num_list


def main():
    #numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    numbers = parse_input("input")
    base_pattern = [0, 1, 0, -1]
    print(run_n_times(100, numbers, base_pattern))


if __name__ == "__main__":
    main()
