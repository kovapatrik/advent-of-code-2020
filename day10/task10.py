diffs = {'1': 0, '2': 0, '3': 0}
jolt = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    jolts = [int(c.strip()) for c in lines]
    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1]+3)
    #Part1
    i = 0
    while(i < len(jolts) - 1):
        d = jolts[i+1] - jolts[i]
        diffs[str(d)]+=1
        i+=1
    print(diffs['1'] * diffs['3'])

    #0 1 2 3 4 6
    #1 1 2 4 7 11

    #Part2
    paths = [1]
    for i in range(1, len(jolts)):
        arrange = paths[i-1]
        j = i - 2
        while j >= 0 and jolts[i] - jolts[j] <= 3:
            arrange += paths[j];
            j -= 1

        paths.append(arrange); 
    print(paths[-1])