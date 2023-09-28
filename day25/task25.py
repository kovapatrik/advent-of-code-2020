def readInput(path='input.txt'):
    with open(path, 'r') as f:
        t = f.read().splitlines()
        return int(t[0]), int(t[1])

def getLoopSize(key):
    base_val = 7
    subject = 1
    i = 0
    while(subject != key):
        subject *= base_val
        subject = subject % 20201227
        i+=1
    return i

def getEncryptionKey(key, loopSize):
    subject = 1
    base_val = key
    for _ in range(loopSize):
        subject *= base_val
        subject = subject % 20201227
    return subject

def part1(card, door):
    card_loop = getLoopSize(card)
    return getEncryptionKey(door, card_loop)

def main():
    card_public, door_public = readInput()
    print('Part 1:', part1(card_public, door_public))

main()