coords = [0,0]
directions = {
    'W': [1,0],
    'N': [0,1],
    'E': [-1,0],
    'S': [0,-1],
}
facing = 2

def changeFacing(facing, dir, val):
    while(val > 0):
        val -= 90
        if dir == 'R':
            facing += 1
            if facing > 3:
                facing = 0
        elif dir == 'L':
            facing -= 1
            if facing < 0:
                facing = 3
    return facing

def rotateWP(wp, m, val):
    while(val > 0):
        val-=90
        if m == 'R':
            wp = [-wp[1], wp[0]]
        elif m == 'L':
            wp = [wp[1], -wp[0]]
    return wp
            
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        m = l[0]
        val = int(l[1:])
        if m == 'N':
            coords[1] += val
        elif m == 'S':
            coords[1] -= val
        elif m == 'E':
            coords[0] -= val
        elif m == 'W':
            coords[0] += val
        elif m == 'L' or m == 'R':
            facing = changeFacing(facing, m, val)
        elif m == 'F':
            coords[0] += list(directions.values())[facing][0] * abs(val)
            coords[1] += list(directions.values())[facing][1] * abs(val)
        #print(m, val, coords, facing)
    print(abs(coords[0]) + abs(coords[1]))
    
    coords = [0,0]
    wp = [-10,1]
    for l in lines:
        m = l[0]
        val = int(l[1:])
        if m == 'N':
            wp[1] += val
        elif m == 'S':
            wp[1] -= val
        elif m == 'E':
            wp[0] -= val
        elif m == 'W':
            wp[0] += val
        elif m == 'L' or m == 'R':
            wp = rotateWP(wp, m, val)
        elif m == 'F':
            coords[0] += wp[0] * abs(val)
            coords[1] += wp[1] * abs(val)
        print(coords, wp)
    print(abs(coords[0]) + abs(coords[1]))


