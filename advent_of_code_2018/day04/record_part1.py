from datetime import datetime
from pprint import pprint


def take_first(elem):
    return elem[0]


def take_second(elem):
    return elem[1]


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

    guard = list(guards.values())
        
    guard.sort(key=take_second, reverse=True)
    sample = [(line[0], line[1]) for line in guard[:5]]
    pprint(sample)

    return guard[0]


def main():
    schedule = parse_input()
    guard = sleepy_time(schedule)
    id = guard[0]
    sleepy_minutes = guard[2]
    mostly_slept = max(set(sleepy_minutes), key=sleepy_minutes.count)
    print(mostly_slept)
    print(id*mostly_slept)


if __name__ == "__main__":
    main()
