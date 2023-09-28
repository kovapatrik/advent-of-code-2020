import re

DIRECTIONS = {
    "e": [2,0],
    "se": [1,-1],
    "sw": [-1,-1],
    "w": [-2,0],
    "nw": [-1,1],
    "ne": [1,1]
}

def readInput(path='input.txt'):
    with open(path, 'r') as f:
        return [re.findall(r'nw|ne|sw|se|e|w', x) for x in f.read().splitlines()]

def init(tiles):
    blacks = set()
    for t in tiles:
        coord = [0,0]
        for step in t:
            coord[0] += DIRECTIONS[step][0]
            coord[1] += DIRECTIONS[step][1]
        tuped = tuple(coord)
        if tuped not in blacks:
            blacks.add(tuped)
        else:
            blacks.remove(tuped)
    return blacks

def part1(tiles):
    return len(init(tiles))

def part2(tiles):
    black = init(tiles)
    for _ in range(100):
        neigh = {}
        for t in black:
            if t not in neigh:
                neigh[t] = 0
            for d in DIRECTIONS:
                curr = list(t)
                curr[0] += DIRECTIONS[d][0]
                curr[1] += DIRECTIONS[d][1]
                curr = tuple(curr)
                if curr not in neigh:
                    neigh[curr] = 1
                else:
                    neigh[curr]+=1
        newBlack = set()
        for n in neigh:
            if (n in black and neigh[n] in [1,2] or \
                n not in black and neigh[n] == 2):
                newBlack.add(n)
        black = newBlack
    
    return len(black)


def main():
    tiles = readInput()
    print('Part 1:', part1(tiles))
    print('Part 2:', part2(tiles))

main()