#!/usr/bin/env python3
from functools import reduce
import numpy as np


def parse_input():
    with open("input", "r") as f:
        text = f.read()
    target, busses = text.split("\n")
    busses = [(int(bus), i)
              for i, bus in enumerate(busses.split(",")) if bus != "x"]
    return busses


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


if __name__ == "__main__":
    busses = parse_input()
    n = [bus[0] for bus in busses]
    a = [bus - i for bus, i in busses]
    print(chinese_remainder(n, a))
