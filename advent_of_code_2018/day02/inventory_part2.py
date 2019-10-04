def parse_input():
    with open("input", "r") as f:
        text = f.read()[:-1]
    lines = text.split("\n")
    return lines


def box_id(lines):
    two_times = [0]*len(lines)
    three_times = [0]*len(lines)

    for word1 in lines:
        for word2 in lines:
            if word1 > word2:
                diff = 0

                for i, letter in enumerate(word1):

                    if letter != word2[i]:
                        diff += 1

                        if diff > 1:
                            break

                if diff == 1:
                    # we found the words, now its just about convenient #printing
                    #print(word1, word2)

                    for i, letter in enumerate(word1):
                        
                        if letter == word2[i]:
                            #print(letter, end='')
                    break


def main():
    lines = parse_input()
    box_id(lines)
    #print()


if __name__ == "__main__":
    main()
