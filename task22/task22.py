from copy import deepcopy

def readInput(path='input.txt'):
    with open(path, 'r') as f:
        return [[int(x) for x in t.splitlines()[1:]] for t in f.read().split("\n\n")]

def part1(decks):
    while(len(decks[0]) > 0 and len(decks[1]) > 0):
        a = decks[0].pop(0)
        b = decks[1].pop(0)
        if a > b:
            decks[0] += [a,b]
        else:
            decks[1] += [b,a]
    if len(decks[0]) > 0:
        ind = 0
    else:
        ind = 1
    return sum([x * (i+1) for i,x in enumerate(decks[ind][::-1])])

def part2(decks):
    previous = set()
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        if (tuple(decks[0]), tuple(decks[1])) in previous:
            return 0, decks
        else:
            previous.add((tuple(decks[0]), tuple(decks[1])))
        a = decks[0].pop(0)
        b = decks[1].pop(0)
        if len(decks[0]) >= a and len(decks[1]) >= b:
            sub_winner, _ = part2([decks[0][:a],decks[1][:b]])
        else:
            if a > b:
                sub_winner = 0
            else:
                sub_winner = 1
        if sub_winner == 0:
            decks[0] += [a,b]
        else:
            decks[1] += [b,a]
    if len(decks[0]) > 0:
        return 0, decks
    else:
        return 1, decks

def main():
    decks = readInput()
    print('Part 1:', part1(deepcopy(decks)))
    winner, d = part2(deepcopy(decks))
    print('Part 2:', sum([x * (i+1) for i,x in enumerate(d[winner][::-1])]))

main()