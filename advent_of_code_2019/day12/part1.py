from itertools import combinations


def parse_input(input):
    with open(input, "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
        lines = [line[1:-1].split(", ") for line in lines]
        lines = [[int(elem[2:]) for elem in line] for line in lines]
        lines = [(i[0], i[1], i[2]) for i in lines]
        return lines


def update_velocity(pairs, moons, velocity):
    for pair in pairs:
        (a, b) = pair
        for i in range(3):
            if moons[a][i] < moons[b][i]:
                velocity[a][i] += 1
                velocity[b][i] -= 1
            elif moons[a][i] > moons[b][i]:
                velocity[a][i] -= 1
                velocity[b][i] += 1
    return velocity


def apply_velocity(moons, velocity):

    for i, moon in enumerate(moons):
        (x, y, z) = moon
        [vx, vy, vz] = velocity[i]
        # print("moon", x,y,z, "vel",vx,vy,vz)
        moons[i] = (x + vx, y + vy, z + vz)
    return moons


def time_step(pairs, moons, velocity):
    velocity = update_velocity(pairs, moons, velocity)
    moons = apply_velocity(moons, velocity)
    return (moons, velocity)


def get_total_energy(moons, velocity):
    total_energy = 0
    for i, moon in enumerate(moons):
        (x, y, z) = moon
        [vx, vy, vz] = velocity[i]
        pot = abs(x) + abs(y) + abs(z)
        kin = abs(vx) + abs(vy) + abs(vz)
        total_energy += pot * kin
    return total_energy


def main():

    # moons = parse_input("test2")

    # velocity = [[0, 0, 0] for moon in moons]
    # pairs = list(combinations('0123', 2))
    # print(pairs)
    # pairs = [(int(a), int(b)) for (a, b) in pairs]
    # print(pairs)

    # for i in range(101):
    #     # print("previous_mem_len", previous_mem_len)
    #     # print("new_mem_len",  len(set(memory)))

    #     print("step ", i)
    #     for j, moon in enumerate(moons):
    #         print("pos: ", moon, " vel: ", velocity[j])
    #     print("total_energy: ", get_total_energy(moons, velocity))

    #     (moons, velocity) = time_step(pairs, moons, velocity)

    moons = parse_input("input")

    velocity = [[0, 0, 0] for moon in moons]
    pairs = list(combinations('0123', 2))
    print(pairs)
    pairs = [(int(a), int(b)) for (a, b) in pairs]
    print(pairs)

    for i in range(1001):
        # print("previous_mem_len", previous_mem_len)
        # print("new_mem_len",  len(set(memory)))
        if i == 1000:
            print("step ", i)
            for j, moon in enumerate(moons):
                print("pos: ", moon, " vel: ", velocity[j])
            print("total_energy: ", get_total_energy(moons, velocity))

        (moons, velocity) = time_step(pairs, moons, velocity)


if __name__ == "__main__":
    main()
