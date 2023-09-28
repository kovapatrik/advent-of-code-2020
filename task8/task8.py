acc = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    i = 0
    arr = []
    while(i not in arr):
        arr.append(i)
        l = lines[i]
        s = l.split(' ')
        if s[0] == 'acc':
            acc += int(s[1])
            i+=1
        elif s[0] == 'nop':
            i+=1
        elif s[0] == 'jmp':
            i += int(s[1])
    print(acc)

    i = 0
    acc = 0
    arr = []
    changed_i = []
    changed = False
    cop = lines.copy()
    while(i != len(cop)):
        l = cop[i]
        s = l.split(' ')
        if i in arr and changed:
            i = 0
            acc = 0
            arr = []
            changed = False
            cop = lines.copy()
        else:
            if s[0] == 'acc':
                acc += int(s[1])
                arr.append(i)
                i+=1
            elif s[0] == 'nop' or s[0] == 'jmp':
                if s[0] == 'nop':
                    m = 1
                    text = 'jmp '
                else:
                    m = int(s[1])
                    text = 'nop '
                if i not in changed_i and not changed:
                    changed_i.append(i)
                    changed = True
                    cop[i] = text + s[1]
                else:
                    arr.append(i)
                    i+=m
    print(acc)

