import math

highest = 0
lowest = math.inf

ids = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        rows = [0, 127]
        cols = [0, 7]
        for c in l:
            if c == 'B':
                rows[0] = math.ceil((rows[1] + rows[0]) / 2)
            if c == 'F':
                rows[1] = math.floor((rows[1] + rows[0]) / 2)
            if c == 'R':
                cols[0] = math.ceil((cols[1] + cols[0]) / 2)
            if c == 'L':
                cols[1] = math.floor((cols[1] + cols[0]) / 2)
        if rows[0] * 8 + cols[0] > highest:
            highest = rows[0] * 8 + cols[0]
        ids.append(rows[0] * 8 + cols[0])

ids.sort()

my_id = -1
i = 0
while(i < len(ids) - 1 and my_id == -1):
    if (ids[i] + 1 != ids[i+1]):
        my_id = ids[i] + 1
    i+=1
print(my_id)
