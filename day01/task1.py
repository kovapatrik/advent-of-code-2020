numbers = []

with open("input.txt", 'r') as f:
    lines = f.readlines()
    for l in lines:
        num = int(l)
        numbers.append(num)
        for n in numbers:
            for m in numbers:
                if n != num != m and n + m + num == 2020:
                    print(n, num, m, n*num*m)