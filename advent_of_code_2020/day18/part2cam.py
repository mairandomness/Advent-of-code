import re
class Num(int):
    def __mul__(self, other):
        return Num(super(Num,self).__add__(other))
    def __add__(self, other):
        return Num(super(Num,self).__mul__(other))

def solve(line):
    line = re.sub(r"(\d+)", r"Num(\1)", line)
    line = line.replace("+", "PLUS").replace("*", "MULT").replace("PLUS", "*",).replace("MULT", "+")
    return eval(line)

with open("input") as f:
    print(sum(solve(line) for line in f))