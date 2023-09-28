numbers = []
with open('input.txt', 'r') as f:
    numbers = [int(c) for c in f.readline().split(',')]


# part 1

game = dict()
i = 0
curr_num = 1
while(i < 30000000):
    if i < len(numbers):
        game[numbers[i]] = [i]
    else:
        last_num = numbers[i-1]
        if last_num in game.keys() and len(game[last_num]) == 1:
            curr_num = 0
        elif last_num in game.keys() and len(game[last_num]) > 1:
            curr_num = game[last_num][-1] - game[last_num][-2]
        if curr_num not in game.keys():
            game[curr_num] = []
        game[curr_num].append(i)
        numbers.append(curr_num)
    i+=1
print(curr_num)

