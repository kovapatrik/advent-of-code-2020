import math

min = 99999999999
id = -1

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chineseTheorem(inputs):
        M = math.prod([x[0] for x in inputs])
        res = 0
        for x in inputs:
            ai = x[1]
            bi = M // x[0]
            bi_ = mul_inv(bi,x[0])
            res += ai * bi * bi_
        return res % M

with open('input.txt', 'r') as f:
    lines = f.readlines()
    earliest = int(lines[0].strip())
    buses = lines[1].split(',')
    buses = [c.replace('\n', '') for c in buses]

    part1_buses = [int(c) for c in buses if c != 'x']
    for b in part1_buses:
        upper = math.ceil(earliest / b) * b
        if abs(earliest - upper) < min:
            min = abs(earliest - upper)
            id = b
    print(id * min)

    part2_buses = buses.copy()
    part2_buses = [(int(x), -i) for i, x in enumerate(part2_buses) if x != 'x']

    print(chineseTheorem(part2_buses))



