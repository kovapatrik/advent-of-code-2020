from itertools import product

def printDim(dim, num):
    for l in dim[num]:
        print(l)
    print()

def init(input, dimensions):
    actives = set()
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char == '#':
                actives.add(tuple([i,j,] + [0] * (dimensions - 2)))
    return actives

def doTask(input, dimensions, rounds):
    actives = init(input, dimensions)
    for _ in range(rounds):
        cntActives = {}
        for loc in actives:
            for v in product([-1, 0, 1], repeat=dimensions):
                new_loc = tuple(map(sum, zip(loc, v)))
                if new_loc != loc:
                    if new_loc not in cntActives:
                        cntActives[new_loc] = 1
                    else:
                        cntActives[new_loc]+=1
        stayActive = set([loc for loc in actives if loc in cntActives and cntActives[loc] in [2,3]])
        setActive  = set([loc for loc in cntActives if loc not in actives and cntActives[loc] == 3])
        actives = stayActive | setActive
    return actives

with open('input.txt', 'r') as f:
    lines = f.readlines()
    #part1
    part1_actives = doTask(lines, 3, 6)
    print(len(part1_actives))
    part2_actives = doTask(lines, 4, 6)
    print(len(part2_actives))