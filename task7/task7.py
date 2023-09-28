bags = {}

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        s = l.replace('bags', '').replace('bag', '').replace('.\n', '').split(' contain ')
        s = [c.strip() for c in s]
        other_bags = s[1].split(' , ')
        final_bags = []
        if "no other" not in other_bags:
            for c in other_bags:
                splitted = c.split(' ', 1)
                for i in range(0,int(splitted[0])):
                    final_bags.append(splitted[1])
            for o in final_bags:
                if o not in bags.keys():
                    bags[o] = []
                bags[o].append(s[0])

print(bags)

good_bags = list(set(bags['shiny gold'].copy()))
for b in good_bags:
    if b in bags.keys():
        good_bags.extend(bags[b].copy())
good_bags = set(good_bags)
print(len(good_bags))

def count_bag(bag):
    t = [(b, bags[b].count(bag)) for b in bags if bag in bags[b]]
    if len(t) > 0:
        cnt = 0
        for k in t:
            cnt += k[1] + k[1] * count_bag(k[0])
        return cnt
    else:
        return 0

cnt = count_bag('shiny gold')
print(cnt)

