cnt = 0

base = {
            "byr": False,
            "iyr": False,
            "eyr": False,
            "hgt": False,
            "hcl": False,
            "ecl": False,
            "pid": False,
            "cid": False
        }

def validatePassport(id, val):
    val = val.replace('\n', '')
    if (id == 'byr'):
        val = int(val)
        if (len(str(val)) == 4 and val >= 1920 and val <= 2002):
            return True
    elif(id == "iyr"):
        val = int(val)
        if (len(str(val)) == 4 and val >= 2010 and val <= 2020):
            return True
    elif(id == "eyr"):
        val = int(val)
        if (len(str(val)) == 4 and val >= 2020 and val <= 2030):
            return True
    elif(id == "hgt"):
        cm = val.find('cm')
        inc = val.find('in')
        if (cm != -1):
            cm = int(val[:cm])
            if (cm >= 150 and cm <= 193):
                return True
        elif(inc != -1):
            inc = int(val[:inc])
            if (inc >= 59 and inc <= 76):
                return True
    elif(id == "hcl"):
        try:
            if (val[0] == '#' and int(val[1:], 16) >= 0 and len(val[1:]) == 6) :
                return True
        except(ValueError):
            pass
    elif(id == "ecl"):
        if (val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            return True
    elif(id == "pid"):
        if (len(val) == 9 and val.isdigit()):
            return True
    elif(id == "cid"):
        return True

    return False


with open("input.txt", 'r') as f:
    lines = f.readlines()
    i = 0
    passport = base.copy()
    while (i < len(lines)):
        l = lines[i]
        if l != "\n":
            splitted = l.split(' ')
            for s in splitted:
                id = s.split(':')[0]
                val = s.split(':')[1]
                passport[id] = validatePassport(id, val)
        if (l == '\n' or i == len(lines) - 1):
            good = True
            for k in passport:
                if k != 'cid':
                    good = good and passport[k]
            if good:
                cnt += 1
            #print(i, passport)
            passport = base.copy()
        i+=1
print(cnt)