from itertools import combinations
import math


def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
        lines = [line[1:-1].split(", ") for line in lines]
        lines = [[int(elem[2:]) for elem in line] for line in lines]
        lines = [[i[0], i[1], i[2]] for i in lines]
        result = []
        for line in lines:
            result += line
        return result


def find_repetition(pairs, statex):
    n = 0

    initial_statex = statex[:]

    while True:
        # update speeds
        for pair in pairs:
            (a, b) = pair
            if statex[a] < statex[b]:
                statex[a + 4] += 1
                statex[b + 4] -= 1
            elif statex[a] > statex[b]:
                statex[a + 4] -= 1
                statex[b + 4] += 1

        # apply speeds
        statex[0] += statex[4]
        statex[1] += statex[5]
        statex[2] += statex[6]
        statex[3] += statex[7]

        n += 1
        if statex == initial_statex:
            return n
    return(n)


def main():

    moons = parse_input("input")
    velocity = [0]*12
    state = moons + velocity

    pairs = list(combinations('0123', 2))
    pairs = [(int(a), int(b)) for (a, b) in pairs]

    statex = [state[3*i] for i in range(8)]
    statey = [state[3*i + 1] for i in range(8)]
    statez = [state[3*i + 2] for i in range(8)]

    # print(statex)
    # print(statey)
    # print(statez)
    repx = find_repetition(pairs, statex)
    repy = find_repetition(pairs, statey)
    repz = find_repetition(pairs, statez)

    print(repx, ",", repy, ",", repz)
    lcm1 = repx * repy // math.gcd(repx, repy)
    lcm2 = repx * repz // math.gcd(repx, repz)
    result = lcm1 * lcm2 // math.gcd(lcm1, lcm2)
    print("LCM from the above numbers is:", result)


if __name__ == "__main__":
    main()
