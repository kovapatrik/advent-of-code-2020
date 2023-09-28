from copy import deepcopy

s = 0

rules = dict()
my_ticket = []
nearby_tickets = []

with open('input.txt', 'r') as f:
    for line in f:
        l = line.replace('\n', ' ')
        if s == 0:
            if l.isspace():
                s = 1
            else:
                splitted = l.split(': ')
                vals = splitted[1].split(' or ')
                rules[splitted[0]] = []
                for v in vals:
                    in_val = v.split('-')
                    rules[splitted[0]] += list(range(int(in_val[0]), int(in_val[1]) + 1))
        elif s == 1:
            if l.isspace():
                s = 2
            elif not l.startswith('your'):
                my_ticket = [int(n) for n in l.split(',')]
        else:
           if not l.startswith('nearby'):
               nearby_tickets.append([int(n) for n in l.split(',')])

sum = 0
part2_nearby_tickets = nearby_tickets.copy()
for n in nearby_tickets:
    for m in n:
        if not any([m in rules[k] for k in rules]):
            sum+=m
            part2_nearby_tickets.remove(n)
print(sum)

part2_rules = dict()
for k in rules:
    part2_rules[k] = []
    i = 0
    while(i < len(rules.keys())):
        good = True
        for m in part2_nearby_tickets:
            good = good and (m[i] in rules[k])
        if good:
            part2_rules[k].append(i)
        i+=1


sorted_part2_rules = {k: v for k, v in sorted(part2_rules.items(), key=lambda item: item[1], reverse=True)}

temp = deepcopy(sorted_part2_rules)
keys = list(temp.keys())
cannot_delete = []
while(keys):
    k = keys.pop(0)

    #print(k, temp[k], cannot_delete)
    deletable_numbers = [x for x in temp[k] if x not in cannot_delete]
    if len(temp[k]) == 1 and (temp[k][0] in cannot_delete):
        removed_number = temp[k][0]
    else:
        removed_number = deletable_numbers[0]

    for in_k in temp.keys():
        if in_k != k and removed_number in temp[in_k]:
            temp[in_k].remove(removed_number)
    
    if not all([len(temp[t]) > 0 for t in temp]):
        temp = deepcopy(sorted_part2_rules)
        keys = list(temp.keys())
        cannot_delete.append(removed_number)

ans = 1
for k in temp:
    if k.startswith('departure'):
        k_i = temp[k][0]
        ans *= my_ticket[k_i]
print(ans)