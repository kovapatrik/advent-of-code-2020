cnt = -1

def validCoord(i,j, seats):
    return (i >= 0 and j >= 0 and i < len(seats) and j < len(seats[0]))

def checkDirectionsPart1(i,j, seats):
    # Return number of adjacent occupied seats
    cnt = 0
    dirs = [(i, j-1), (i, j+1), (i-1, j), (i+1, j), \
            (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for d in dirs:
        if validCoord(d[0], d[1], seats):
            if seats[d[0]][d[1]] == '#':
                cnt+=1
    return cnt

def checkDirectionsPart2(i,j, seats):
    # Return number of adjacent occupied seats
    cnt = 0
    dirs = [(0,1), (0,-1), (1, 0), (-1,0), \
            (1,-1), (1,1), (-1,-1), (-1,1)]
    for d in dirs:
        t_i = i + d[0]
        t_j = j + d[1]
        while(validCoord(t_i, t_j, seats) and seats[t_i][t_j] == '.'):
            t_i = t_i + d[0]
            t_j = t_j + d[1]
        if validCoord(t_i, t_j, seats):
            cnt += seats[t_i][t_j] == '#'
    return cnt

with open('input.txt', 'r') as f:
    seats = f.readlines()
    # part1_seats = seats.copy()
    # last_cnt = 0
    # while(last_cnt != cnt):
    #     new_seats = part1_seats.copy()
    #     for i in range(len(part1_seats)):
    #         for j in range(len(part1_seats[i])):
    #             n = checkDirectionsPart1(i,j, part1_seats)
    #             if part1_seats[i][j] == 'L' and n == 0:
    #                 new_seats[i] = new_seats[i][:j] + '#' + new_seats[i][j+1:]
    #             elif part1_seats[i][j] == '#' and n >= 4:
    #                 new_seats[i] = new_seats[i][:j] + 'L' + new_seats[i][j+1:]
                
    #         last_cnt += new_seats[i].count('#')
    #     if last_cnt != cnt:
    #         part1_seats = new_seats
    #         cnt = last_cnt
    #         last_cnt = 0
    # print(cnt, '\n')

    cnt = -1
    last_cnt = 0
    part2_seats = seats.copy()
    while (last_cnt != cnt):
        new_seats = part2_seats.copy()
        for i in range(len(part2_seats)):
            for j in range(len(part2_seats[i])):
                n = checkDirectionsPart2(i,j, part2_seats)
                if part2_seats[i][j] == 'L' and n == 0:
                    new_seats[i] = new_seats[i][:j] + '#' + new_seats[i][j+1:]
                elif part2_seats[i][j] == '#' and n >= 5:
                    new_seats[i] = new_seats[i][:j] + 'L' + new_seats[i][j+1:]
                
            last_cnt += new_seats[i].count('#')
        if last_cnt != cnt:
            part2_seats = new_seats
            cnt = last_cnt
            last_cnt = 0
    print(cnt)

