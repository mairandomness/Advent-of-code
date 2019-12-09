from collections import Counter


def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        layers = [text[i * 150: i * 150 + 150] for i in range(len(text)/150)]
    return layers


def find_least_zero_layer(layers):
    layers = [[char for char in layer if char != '0'] for layer in layers]
    least_zero = sorted(layers, key=lambda x: len(x), reverse=True)[0]
    return dict(Counter(least_zero))


def main():
    layers = parse_input()
    counter = find_least_zero_layer(layers)
    values = counter.values()
    print(values[0] * values[1])


if __name__ == "__main__":
    main()
