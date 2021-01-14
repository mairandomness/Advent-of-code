#!/usr/bin/env python3

# TRY A CICULAR LINKED LIST
def crab_game(curr, cup_nodes):
    three_cups_root = curr.next
    three_cups_val = [curr.next.value,
                      curr.next.next.value, curr.next.next.next.value]
    curr.next = curr.next.next.next.next
    dest_cup_val = curr.value - 1

    while dest_cup_val in three_cups_val or dest_cup_val == 0:
        dest_cup_val -= 1
        if dest_cup_val == 0 or dest_cup_val == -1:
            dest_cup_val = 1000000

    #print("destcupval: ", dest_cup_val)
    dest_node = cup_nodes[dest_cup_val]
    #print("destnode: ", dest_node)
    temp = dest_node.next
    dest_node.next = three_cups_root
    dest_node.next.next.next.next = temp

    curr = curr.next
    return curr

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


if __name__ == "__main__":
    input = "523764819"
    test = "389125467"
    cups = [i for i in range(1, 1000001)]
    for i, char in enumerate(input):
        cups[i] = int(char)

    cup_nodes = [0] * 10000001
    curr = Node(cups[0])
    root = curr
    for i, cup in enumerate(cups):
        cup_nodes[cup] = curr
        if i != len(cups) - 1:
            curr.next = Node(cups[i+1])
            curr = curr.next
    curr.next = root
    curr = root
    n = 0
    while n < 10000000:
        # print("curr value: ", curr.value)
        curr = crab_game(curr, cup_nodes)
        n += 1

    node_one = cup_nodes[1]
    print(node_one.next.value)
    print(node_one.next.next.value)
    print("product: ", node_one.next.next.value * node_one.next.value)

