class Planet:
    def __init__(self, name, depth):
        self.name = name
        self.is_orbited_by = []
        self.depth = depth


def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
    return [line.split(")") for line in lines]


def find_planets_that_orbit(planet, orbits, total_orbits):
    orbits_copy = orbits[:]

    for orbit in orbits_copy:
        if orbit[0] == planet.name:
            planet.is_orbited_by.append(Planet(orbit[1], planet.depth + 1))
            orbits.remove(orbit)

    total_orbits.append(len(planet.is_orbited_by) * (planet.depth + 1))
    # print("{} depth {} is orbited by {}".format(planet.name,
    #                                           planet.depth, [body.name for body in planet.is_orbited_by]))
    for body in planet.is_orbited_by:
        find_planets_that_orbit(body, orbits, total_orbits)

    if len(orbits) == 0:
        return total_orbits


def count_orbits(orbits):
    depth = 0
    orbited = set([orbit[0] for orbit in orbits])
    orbitees = set([orbit[1] for orbit in orbits])

    root = Planet(list(orbited.difference(orbitees))[0], 0)
    total_orbits = []
    return sum(find_planets_that_orbit(root, orbits, total_orbits))


def main():
    orbits = parse_input()
    print(count_orbits(orbits))


if __name__ == "__main__":
    main()
