class Planet:
    def __init__(self, name, depth, parent=None):
        self.name = name
        self.is_orbited_by = []
        self.orbits = parent
        self.depth = depth
        self.all_direct_indirect_children = []


def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
    return [line.split(")") for line in lines]


def find_planets_that_orbit(planet, orbits, all_planets):
    orbits_copy = orbits[:]
    for orbit in orbits_copy:
        if orbit[0] == planet.name:
            all_planets[orbit[1]] = Planet(
                orbit[1], planet.depth + 1, planet.name)
            planet.is_orbited_by.append(orbit[1])
            orbits.remove(orbit)

    for body in planet.is_orbited_by:
        find_planets_that_orbit(all_planets[body], orbits, all_planets)

    if len(orbits) == 0:
        return all_planets


def build_tree(orbits):
    depth = 0
    orbited = set([orbit[0] for orbit in orbits])
    orbitees = set([orbit[1] for orbit in orbits])

    root = Planet(list(orbited.difference(orbitees))[0], 0)
    all_planets = {}
    all_planets[root.name] = root
    find_planets_that_orbit(root, orbits, all_planets)
    # for planet in all_planets.values():
    #   print("{} depth {} is orbited by {}".format(
    #      planet.name, planet.depth, planet.is_orbited_by))
    return all_planets


def find_path_len(all_planets, planet1, planet2):
    planet1_ancesters = []
    current_planet = planet1
    while all_planets[current_planet].orbits != None:
        current_planet = all_planets[current_planet].orbits
        planet1_ancesters.append(current_planet)

    current_planet = planet2
    while all_planets[current_planet].orbits != None:
        current_planet = all_planets[current_planet].orbits
        if current_planet in planet1_ancesters:
            common_ancester = current_planet
            break

    common_ancester_depth = all_planets[common_ancester].depth
    planet1_depth = all_planets[planet1].depth
    planet2_depth = all_planets[planet2].depth
    return planet1_depth + planet2_depth - 2 * common_ancester_depth - 2


def main():
    orbits = parse_input()
    all_planets = build_tree(orbits)
    planet = all_planets['YOU']

    print(find_path_len(all_planets, 'YOU', 'SAN'))


if __name__ == "__main__":
    main()
