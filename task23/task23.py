def part1(cups, round):
    curr_cup = (cups[0], 0)
    min_c, max_c = min(cups), max(cups)
    max_i = len(cups)-1
    for _ in range(round):
        j = curr_cup[1]+1
        pickups = []
        while(len(pickups) < 3):
            if j > len(cups) - 1:
                j = 0
            pickups.append(cups.pop(j))
        destination_cup = curr_cup[0] - 1
        while(destination_cup in pickups or destination_cup < min_c):
            if destination_cup < min_c:
                destination_cup = max_c
            else:
                destination_cup-=1
        
        cups = cups[:cups.index(destination_cup)+1] + pickups + cups[cups.index(destination_cup)+1:]
        #print(curr_cup[0], pickups, destination_cup, cups)
        next_i = cups.index(curr_cup[0]) + 1
        if next_i > max_i:
            next_i = 0

        curr_cup = (cups[next_i], next_i)
        
    i = cups.index(1) + 1
    final = ""
    while(len(final) < len(cups) - 1):
        if i > len(cups) - 1:
            i = 0
        final+=str(cups[i])
        i+=1
    return final


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def part2(cups):
    lookup = {}

    prev = None
    for i in range(len(cups)-1, -1, -1):
        new = Node(cups[i])
        new.next = prev
        lookup[cups[i]] = new
        prev = new

    for i in range(1000000, 9, -1):
        new = Node(i)
        new.next = prev
        lookup[i] = new
        prev = new

    lookup[cups[-1]].next = lookup[10]

    cur = lookup[cups[0]]

    for _ in range(10000000):
        remove1 = cur.next
        remove2 = remove1.next
        remove3 = remove2.next
        cur.next = remove3.next
        removed = {cur.val, remove1.val, remove2.val, remove3.val}
        cval = cur.val
        while cval in removed:
            cval -= 1
            if cval == 0:
                cval = 1000000
        targetLoc = lookup[cval]
        afterTarget = targetLoc.next

        targetLoc.next = remove1
        remove3.next = afterTarget

        cur = cur.next

    cup1 = lookup[1]
    remove1 = cup1.next
    remove2 = remove1.next

    return remove1.val * remove2.val



def main(input='219748365'):
    cups = [int(x) for x in input]
    print('Part 1:', part1(cups.copy(), 100))
    print('Part 2:', part2(cups.copy()))

main()