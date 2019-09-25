def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
    return text

def react(polymer):
    polymer_copy = polymer[:]
    i = len(polymer_copy) - 1
    while i >= 1:
        cur = polymer_copy[i]
        next = polymer_copy[i-1]
        
        if cur != next and cur.lower() == next.lower():
            polymer = polymer[:i-1] + polymer[i+1:]
            i -= 1
        
        i -= 1
    return polymer

def loop(polymer):
    next = react(polymer)
    while len(next) != len(polymer):
        polymer = next
        next = react(polymer)
    return next


def main():
    polymer = parse_input()
    #polymer = "abBA"
    new_poly = loop(polymer)
    print(new_poly)
    print(len(new_poly))


if __name__ == "__main__":
    main()
