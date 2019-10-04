import itertools

WORKERS = 5
STEP = 60


def parse_input():
    with open("input", "r") as f:
        text = f.read()
    lines = text[:-1].split("\n")
    lines = [line.split(" ") for line in lines]
    deps = [[line[1], line[7]] for line in lines]
    # print(deps)
    return deps


def value(letter):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters.index(letter) + 1 + STEP


def is_working(workers):
    for worker in workers:
        if type(worker[0]) == str:
            return True
    return False


def assign_work(workers, can_be_next, not_assigned_letters):
    workers_copy = workers[:]
    for i, worker in enumerate(workers_copy):
        if len(can_be_next) > 0:
            if workers[i][0] == -1:
                not_assigned_letters.remove(can_be_next[0])
                workers[i] = (can_be_next[0], value(can_be_next[0]))
                can_be_next = can_be_next[1:]
    #print(workers)
    #print("can be next after assign", can_be_next)
    return (workers, can_be_next, not_assigned_letters)


def step_time(workers):
    return [(letter, time - 1) for (letter, time) in workers]


def finished_task(workers):
    if len([(letter, time) for (letter, time) in workers if time == 0]) != 0:
        return True
    else:
        return False


def get_finished(workers):
    finished = []
    workers_copy = workers[:]
    for i, worker in enumerate(workers_copy):
        if workers[i][1] == 0:
            finished.append(workers[i][0])
            workers[i] = (-1, -1)
    return finished


def path(deps):
    workers = [(-1, -1)] * WORKERS
    remaining_letters = list(set(itertools.chain(*deps)))
    not_assigned_letters = remaining_letters[:]
    finished = []
    can_be_next = []
    time = 0
    can_be_next = find_possible_next(deps, can_be_next, not_assigned_letters)
    #print(" first possible_next", can_be_next)
    (workers, can_be_next, not_assigned_letters) = assign_work(workers, can_be_next, not_assigned_letters)
    #print("possible_next after assign work", can_be_next)

    #print("workers", workers)

    while is_working(workers):
        time += 1
        workers = step_time(workers)

        if finished_task(workers):
            finished = get_finished(workers)

        while len(finished) > 0:
            next = finished[0]
            finished = finished[1:]
            remaining_letters.remove(next)
            deps = [line for line in deps if line[0] != next]

            if len(deps) == 0:
                can_be_next += remaining_letters
            
            can_be_next = list(set(find_possible_next(deps, can_be_next, not_assigned_letters)))
            #print("possible_next", can_be_next)


        (workers, can_be_next, not_assigned_letters) = assign_work(workers, can_be_next, not_assigned_letters)

    return time


def find_possible_next(deps, can_be_next, not_assigned_letters):
    all_letters = list(set(itertools.chain(*deps)))
    #print("all letters", all_letters)
    dep_letters = set([line[1] for line in deps])
    #print("dep letters", list(dep_letters))
    #print("deps", deps)

    for letter in all_letters:
        if (letter not in dep_letters) and letter in not_assigned_letters:
            can_be_next.append(letter)
    #print("can_be_next", can_be_next)
    return can_be_next


def main():
    dependencies = parse_input()
    print(path(dependencies))


if __name__ == "__main__":
    main()
