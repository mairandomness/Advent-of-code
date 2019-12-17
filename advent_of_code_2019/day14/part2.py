
import math
import copy


def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
        lines = [line.split(" => ") for line in lines]
        reagents = [line[0].split(", ") for line in lines]
        reagents = [[element.split(" ") for element in line]
                    for line in reagents]
        reagents = [[[int(element[0]), element[1]]
                     for element in line] for line in reagents]
        result = [line[1].split(" ") for line in lines]
        result = [[int(line[0]), line[1]] for line in result]

        return (reagents, result)


def sum_same_element(elem_list):
    new_elem_list = []
    for i, elem1 in enumerate(elem_list):
        names = [name for [qtt, name] in new_elem_list]
        if elem1[1] not in names:
            new_elem_list.append(elem1)
        else:
            j = names.index(elem1[1])
            new_elem_list[j][0] += elem1[0]

    return(new_elem_list)


def multiply(elem_list, reagents, results):
    # print("incoming elemntlist", elem_list)
    new_elem_list = []
    to_pop = []
    reagent_names = [elem[1] for line in reagents for elem in line]
    # print("all_names:", reagent_names)
    for n, elem in enumerate(elem_list):
        if elem[1] in reagent_names:
            new_elem_list.append(elem)
        else:
            for i, line in enumerate(results):

                if elem[1] == line[1]:
                    multiplier = math.ceil(elem[0]/line[0])
                    results[i][0] = line[0] * multiplier
                    for j, r_elemen in enumerate(reagents[i]):
                        reagents[i][j][0] *= multiplier

                    new_elem_list += reagents[i]
                    to_pop = [i] + to_pop
                    # print("Exchanging {} for {}".format(elem, reagents[i]))

    for line in sorted(to_pop, reverse=True):
        results.pop(line)
        reagents.pop(line)

    # print("THIS IS THE SYSTEM:")
    # for n, line in enumerate(reagents):
    #     print(line, results[n])

    new_elem_list = sum_same_element(new_elem_list)
    # print("NEW EQUATION", new_elem_list)
    return(new_elem_list, reagents, results)


def solve(try_next, reagents, results):
    # print(results)
    for n, line in enumerate(reagents):
        if results[n][1] == "FUEL":
            elem_list = [[elem[0] * try_next, elem[1]]for elem in reagents[n]]
            reagents.pop(n)
            results.pop(n)
            break
    # print("ORIGINAL EQUATION:", elem_list)
    while len(elem_list) > 1:
        (elem_list, reagents, results) = multiply(elem_list, reagents, results)

    return(elem_list[0])


def find_max(og_reagents, og_results):
    # print(results)
    # print(og_results)
    max_fuel = 1000000000000
    min_fuel = 1
    tried = 0
    try_next = int((max_fuel + min_fuel)/2)
    while tried != try_next:
        print(try_next)
        tried = int((max_fuel + min_fuel)/2)
        results = [[int(line[0]), line[1]] for line in og_results]
        reagents = [[[int(element[0]), element[1]]
                     for element in line] for line in og_reagents]
        ores = solve(try_next, reagents, results)[0]
        if ores > 1000000000000:
            max_fuel = tried
        else:
            min_fuel = tried
        try_next = int((max_fuel + min_fuel)/2)

    return(try_next)


def main():
    (reagents, results) = parse_input("input")
    print(find_max(reagents, results))


if __name__ == "__main__":
    main()
