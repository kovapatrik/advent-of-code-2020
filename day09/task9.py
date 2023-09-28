preamble = 25

with open('input.txt', 'r') as f:
    lines = f.readlines()
    XMAS = True
    i = preamble
    curr_n = None
    while XMAS:
        l = lines[i]
        curr_n = int(l)
        sums = [[int(n)+int(m) for n in lines[i-preamble:i] if n != m] for m in lines[i-preamble:i] ]
        sums = [item for sublist in sums for item in sublist]
        if curr_n not in sums:
            XMAS = False
            print(curr_n)
        i+=1

    i = 0
    gen_number = 0
    numbers = []
    while(gen_number != curr_n):
        numbers = [int(lines[i])]
        j = i+1
        while (sum(numbers) < curr_n or len(numbers) < 2) and i < len(lines) and j < len(lines):
            numbers.append(int(lines[j]))
            j+=1
        gen_number = sum(numbers)
        i+=1
    print(min(numbers) + max(numbers))

