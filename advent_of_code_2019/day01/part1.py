import math

def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        lines = text.split("\n")
    return sum([math.floor(int(line)/3) - 2 for line in lines])
    
def main():
    numbers = parse_input()
    print(numbers)

if __name__ == "__main__":
    main()