#!/usr/bin/env python3


def parse_input():
    with open("r", "input") as f:
        text = f.read()


def get_loop(subj_num, target):
    value = 1
    i = 0
    while value != target:
        value *= subj_num
        value %= 20201227
        i += 1
    return i

def transform(subj_num, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subj_num
        value %= 20201227
    return value

if __name__ == "__main__":
    pub_card = 1717001
    pub_door = 523731
    card_loop = get_loop(7, pub_card)
    door_loop = get_loop(7, pub_door)

    print(transform(pub_card, door_loop))
    print(transform(pub_door, card_loop))
