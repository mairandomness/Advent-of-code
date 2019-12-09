from collections import Counter


def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
        layers = [text[i * 150: i * 150 + 150]
                  for i in range(int(len(text)/150))]
    return layers


def find_colors(layers):
    final_image = ['3'] * 150
    for i, pix in enumerate(final_image):
        for layer in layers:
            if layer[i] == '0':
                final_image[i] = '0'
                break

            elif layer[i] == '1':
                final_image[i] = '1'
                break

    return final_image


def print_image(image):
    final_image = [image[i * 25: i * 25 + 25]
                   for i in range(int(len(image)/25))]
    for line in final_image:
        for char in line:
            if char == '0':
                print("▓", end='')
            if char == '1':
                print(" ", end='')
        print("")


def main():
    layers = parse_input()
    image = find_colors(layers)
    print_image(image)


if __name__ == "__main__":
    main()
