import itertools


def parse_input():
    with open("test", "r") as f:
        text = f.read()
    lines = text[:-1].split("\n")
    lines = [line.split(" ") for line in lines]
    deps = [[line[1], line[7]] for line in lines]
    # print(deps)
    return deps


def path(deps):
    remaining_letters = list(set(itertools.chain(*deps)))
    can_be_next = []
    path = ""
    can_be_next = find_possible_next(deps, can_be_next)

    while len(can_be_next) > 0:
        can_be_next.sort()
        next = can_be_next[0]
        path += next
        remaining_letters.remove(next)
        #print("path", path)
        can_be_next = can_be_next[1:]
        deps = [line for line in deps if line[0] != next]
        can_be_next = list(set(find_possible_next(deps, can_be_next)))

        if len(deps) == 0:
            can_be_next += remaining_letters



    return path


def find_possible_next(deps, can_be_next):
    all_letters = list(set(itertools.chain(*deps)))
    #print("all letters", all_letters)
    dep_letters = set([line[1] for line in deps])
    #print("dep letters", list(dep_letters))
    #print("deps", deps)

    for letter in all_letters:
        if letter not in dep_letters:
            can_be_next.append(letter)
    #print("can_be_next", can_be_next)
    return can_be_next


def main():
    dependencies = parse_input()
    print(path(dependencies))


if __name__ == "__main__":
    main()
