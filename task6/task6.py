sum = 0
all_sum = 0

with open("input.txt", 'r') as f:
    lines = f.readlines()
    str = []
    for i in range(len(lines)):
        l = lines[i]
        if l != '\n':
            l = l.replace('\n', '')
            str.append(l)
        if l == '\n' or i == len(lines) - 1:
            unique = set()
            [[unique.update(c) for c in s] for s in str]
            unique = list(unique)
            unique.sort()
            sum += len(unique)
            for c in unique:
                ok = True
                for s in str:
                    ok = ok and (c in s)
                if ok:
                    all_sum += 1
            str = []
print(sum)
print(all_sum)