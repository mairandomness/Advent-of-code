def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        text = text.replace('+', '')
    lines = text.split("\n")
    return [int(line) for line in lines]
    
def main():
    numbers = parse_input()
    print(sum(numbers))

if __name__ == "__main__":
    main()