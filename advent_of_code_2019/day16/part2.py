import math


def parse_input(inputee):
    with open(inputee, "r") as f:
        text = f.read()[:-1]
        num_list = [int(char) for char in text]
    return num_list * 10000


def get_new_list(num_list):
    cur_sum = 0
    i = len(num_list) - 1
    for num in reversed(num_list):
        cur_sum = (num + cur_sum) % 10
        num_list[i] = cur_sum
        i -= 1
    return num_list


def run_n_times(times, num_list):
    offset = [n * (10 ** (6 - i)) for i, n in enumerate(num_list[:7])]
    offset = sum(offset)

    num_list = num_list[offset:]

    for i in range(times):
        num_list = get_new_list(num_list)

    msg = sum([n * (10 ** (7 - i)) for i, n in enumerate(num_list[:8])])

    return msg


def main():
    #numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    numbers = parse_input("input")
    result = run_n_times(100, numbers)
    print(result)
    # for i in range(int(len(result)/ 650)):
    #     print(result[i*650:(i+1)*650])


if __name__ == "__main__":
    main()
