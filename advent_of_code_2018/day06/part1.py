import sys
sys.setrecursionlimit(1500000)

def parse_input():
    with open("input", "r") as f:
        text = f.read()
    lines = text.split("\n")
    lines = [line.split(", ") for line in lines]
    coords = [(int(a), int(b)) for [a, b] in lines]
    return coords

def get_coords_to_check(coords):
    max_x = max([a for (a, b) in coords]) + 100
    min_x = min([a for (a, b) in coords]) - 100
    max_y = max([b for (a, b) in coords]) + 100
    min_y = min([b for (a, b) in coords]) - 100

    to_remove = []

    y_range = [min_y, max_y]
    x_range = range(min_x, max_x)
    
    to_check = coords[:]
    for y in y_range:
        for x in x_range:
            to_remove.append(min_distance((x,y), coords))
    
    y_range = range(min_y, max_y)
    x_range = [min_x, max_x]

    for y in y_range:
        for x in x_range:
            to_remove.append(min_distance((x,y), coords))

    print(max_x - min_x)
    print(max_y - min_y)

    print(len(to_remove))

    remove = set(to_remove)
    for coord in coords:
        if coord in remove:
            to_check.remove(coord)
    return to_check
        
    

def max_area(coords):
    # each point in the space is reprenseted
    # by a dict (x,y): (a,b) or (x,y): None
    # with (x,y) being its coordinates,
    # (a,b) being the coordinates of the closest point
    # d being the distance to the closest point
    # and is_unique a bool which it True if the distance is unique
    # and False if the distance is not
    grid = {}
    count = {}
    coords_to_check = get_coords_to_check(coords)
    print(coords_to_check)

    #populate the coordinates that we got
    for coord in coords:
        grid[coord] = coord
        if coord in coords_to_check:
            count[coord] = 1


    for coord in coords_to_check:
        (x, y) = coord
        populate_neighbors(coord, coord, grid, count, coords)
            
    return count


def neighbors(point):
    (x, y) = point
    neighbors = [(x + a, y + b) for a in [0, 1, -1] for b in [0, 1, -1] if (a, b) != (0,0)]
    return neighbors

def populate_neighbors(point, coord, grid, count, coords):
    print(len(count.keys()))
    print(len(grid))
    print(coord)
    print(count)
        
    possible_n = neighbors(point)

    for n in possible_n:
        new_neighbor = False
        if n not in grid.keys():
            d = min_distance(n, coords) 
            grid[n] = d
            new_neighbor = True
            if d in count.keys():
                count[d] += 1
                
            if grid[n] == coord:
                populate_neighbors(n, coord, grid, count, coords)
    return None



def distance(point_A, point_B):
    (a, b) = point_A
    (c, d) = point_B
    return abs(a - c) + abs(b - d)


def min_distance(point, coords):
    min_distance = TOTAL_D
    min_coord = (-1, -1)
    double = False
    for coord in coords:
        cur_distance = distance(point, coord)

        if cur_distance == min_distance:
            double = True

        if cur_distance < min_distance:
            double = False
            min_distance = cur_distance
            min_coord = coord

    if double == True:
        return None
    else:
        return min_coord


def main():
    coords = parse_input()
    print(sorted(max_area(coords).values()))

    
    


if __name__ == "__main__":
    main()
