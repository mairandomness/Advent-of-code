def filter_numbers(min, max):
    num_list = []
    reference_range = [str(i) for i in range(min, max)]
    for num in reference_range:
        if (len(num) != len(set(num))):
            for i, digit in enumerate(num[:-1]):
                crescent = True
                if num[i] > num[i + 1]:
                    crescent = False
                    break

            if crescent:
                print(num)
                num_list.append(num)

    return len(num_list)


def main():
    print(filter_numbers(234208, 765869))


if __name__ == "__main__":
    main()
