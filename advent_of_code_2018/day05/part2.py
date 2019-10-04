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

def analyze(polymer):
    return set(polymer.lower())

def main():
    
    polymer = parse_input()
    # order doesn't matter here, so we can start with the smallest form of
    # the big input polymer, so the code runs faster
    polymer = loop(polymer)
    new_polys = []
    lens = []
    #print(analyze(polymer))
    for unit in analyze(polymer):
        new_polys.append(polymer.replace(unit, '').replace(unit.upper(),''))
    for poly in new_polys:
        lens.append(len(loop(poly)))
    
    #print(min(lens))


if __name__ == "__main__":
    main()
