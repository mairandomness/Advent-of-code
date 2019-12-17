import math


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


def substitute_elem(elem, qtt, reagents, results):
    # CHANGE QTT
    print("Substituting {} for {} ORE".format(elem, qtt))
    if elem != 'FUEL':
        for i, line in enumerate(reagents):
            for j, element in enumerate(line):
                #print("elem", element)
                if element[1] == elem:
                    reagents[i][j] = (element[0] * qtt, "ORE")
            if results[i][1] == elem:
                results[i] = (results[i][0] * qtt, "ORE")

        # this is a print
        for n, line in enumerate(reagents):
            print(line, results[n])

        to_pop = []
        for i, line in enumerate(reagents):
            #print("line", line)
            if len(line) > 1 and len(set([elem[1] for elem in line])) == 1:
                ore_qtt = 0

                for elem in line:
                    ore_qtt += elem[0]
                reagents[i] = [(ore_qtt, 'ORE')]
            if len(line) == 1 and line[0][1] == 'ORE' and results[i][1] == 'ORE':
                print("to_pop", i)
                to_pop = [i] + to_pop

        for line in to_pop:
            results.pop(line)
            reagents.pop(line)

    return(reagents, results)


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
    print("all_names:", reagent_names)
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
                    print("Exchanging {} for {}".format(elem, reagents[i]))

    for line in sorted(to_pop, reverse=True):
        results.pop(line)
        reagents.pop(line)

    print("THIS IS THE SYSTEM:")
    for n, line in enumerate(reagents):
        print(line, results[n])

    new_elem_list = sum_same_element(new_elem_list)
    print("NEW EQUATION", new_elem_list)
    return(new_elem_list, reagents, results)


def solve(reagents, results):
    for n, line in enumerate(reagents):
        if results[n][1] == "FUEL":
            elem_list = reagents[n]
            reagents.pop(n)
            results.pop(n)
            break
    print("ORIGINAL EQUATION:", elem_list)
    while len(elem_list) > 1:
        (elem_list, reagents, results) = multiply(elem_list, reagents, results)

    return(elem_list)


def main():
    (reagents, results) = parse_input("input")
    print(solve(reagents, results))


if __name__ == "__main__":
    main()
