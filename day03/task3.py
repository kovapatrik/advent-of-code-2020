cnt = 0


index_to_check = [(1,1), (3,1), (5,1), (7,1), (1,2)]

for t in index_to_check:
    in_cnt = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        map_i = t[0]
        for i in range(t[1], len(lines), t[1]):
            line = lines[i]
            if line[map_i] == '#':
                in_cnt += 1
            map_i += t[0]
            if map_i > len(line) - 2:
                map_i = map_i - len(line) + 1
    if cnt == 0:
        cnt += in_cnt
    else:
        cnt *= in_cnt
print(cnt)