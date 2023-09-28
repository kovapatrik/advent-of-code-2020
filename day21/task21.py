from os import read


def readInput(path='input.txt'):
    foods = []
    with open(path, 'r') as f:
        for l in f.read().splitlines():
            ing, allerg = l.split(' (contains ')
            ing = set(ing.split())
            allerg = set(allerg[:-1].split(', '))
            foods.append((ing, allerg))
    return foods

def part1(foods):
    foodCount = {}
    allergFoods = {}
    for ing, allerg in foods:
        for i in ing:
            if i not in foodCount.keys():
                foodCount[i] = 1
            else:
                foodCount[i]+= 1
        for a in allerg:
            if a not in allergFoods.keys():
                allergFoods[a] = ing.copy()
            else:
                allergFoods[a] &= ing

    tutker = set()
    for f in allergFoods.values():
        tutker.update(f)
    
    return sum(foodCount[i] for i in (foodCount.keys() - tutker))

def part2(foods):
    allergs = {}
    for ing, allerg in foods:
        for a in allerg:
            if a not in allergs:
                allergs[a] = ing.copy()
            else:
                allergs[a]&= ing
    

    foundIng = set()
    final = []
    while len(final) < len(allergs.keys()):
        for allerg, ing in allergs.items():
            if len(ing - foundIng) == 1:
                in_ing = min(ing - foundIng)
                final.append((allerg, in_ing))
                foundIng.add(in_ing)
                break
    return ','.join(x[1] for x in sorted(final))
    
def main():
    foods = readInput()
    print('Part 1:', part1(foods))
    print('Part 2:', part2(foods))
main()