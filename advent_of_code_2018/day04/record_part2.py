from datetime import datetime
from p#print import p#print

min = 41
def take_first(elem):
    return elem[0]


def take_second(elem):
    return elem[1]


def take_third(elem):
    return elem[2]


def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
    lines = text.split("\n")
    lines = [line.split("]") for line in lines]
    lines = [[datetime.strptime(
        line[0][1:], '%Y-%m-%d %H:%M'), line[1][1:]]for line in lines]
    lines.sort(key=take_first)
    return lines


def sleepy_time(schedule_data):
    # make a dict dict[guard_id] = [guard_id, total sleep, [minutes they were asleep]
    guards = {}
    cur_guard = 0
    fell_asleep = 0
    for event in schedule_data:
        title = event[1]
        if title.startswith('Guard'):
            cur_guard = int(title.split(" ")[1][1:])
            if not cur_guard in guards:
                guards[cur_guard] = [cur_guard, 0, []]

        if title.startswith('falls'):
            fell_asleep = event[0].minute

        if title.startswith('wakes'):
            woke_up = event[0].minute
            guards[cur_guard][1] += woke_up - fell_asleep
            guards[cur_guard][2] += [i for i in range(fell_asleep, woke_up)]

    guard_list = list(guards.values())

    for guard in guard_list:
        if guard[1] > 0:
            sleepy_minutes = guard[2]
            mostly_slept = max(set(sleepy_minutes), key=sleepy_minutes.count)
            guard[1] = guard[2].count(mostly_slept)
            guard.append(mostly_slept)

        else:
            guard.append(0)

    guard_list.sort(key=take_second, reverse=True)
    sample = [(line[0], line[1], line[3]) for line in guard_list]
    p#print(sample)
    return guard_list[0]


def main():
    schedule = parse_input()
    guard = sleepy_time(schedule)
    id = guard[0]
    sleepy_minutes = guard[3]

    #print(id*sleepy_minutes)


if __name__ == "__main__":
    main()
