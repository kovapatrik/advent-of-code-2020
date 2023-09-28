from itertools import product

mask = ''
mem = dict()

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        # part 1
        line = l.replace('\n', '')
        if line.startswith('mask ='):
            mask = line.split(' = ')[1]
        else:
            split = line.split(' = ')
            adr = split[0][4:-1]
            val = int(split[1])
            if adr not in mem.keys():
                mem[adr] = '0' * 36
            binary_val = '{0:036b}'.format(val)
            final_val = ''
            for i in range(36):
                if mask[i] == 'X':
                    final_val += binary_val[i]
                else:
                    final_val += mask[i]
            mem[adr] = final_val
    sum = 0
    for k in mem.keys():
        sum += int(mem[k], 2)
    print(sum)

    # part 2
    mem = dict()
    for l in lines:
        line = l.replace('\n', '')
        if line.startswith('mask ='):
            mask = line.split(' = ')[1]
        else:
            split = line.split(' = ')
            adr = split[0][4:-1]
            val = int(split[1])
            if adr not in mem.keys():
                mem[adr] = 0
            binary_adr = '{0:036b}'.format(int(adr))
            final_addr = ''
            for i in range(36):
                if mask[i] == '0':
                    final_addr+= binary_adr[i]
                elif mask[i] == '1':
                    final_addr+='1'
                else:
                    final_addr+='X'
            x_count = final_addr.count('X')
            products = list(product([0,1], repeat=x_count))
            all_addresses = []
            if len(products[0]) == 0:
                all_addresses = [final_addr]
            else:
                for p in products:
                    temp_addr = final_addr
                    p_i = 0
                    while(temp_addr.count('X') > 0):
                        x_i = temp_addr.find('X')
                        temp_addr = temp_addr[:x_i] + str(p[p_i]) + temp_addr[x_i+1:]
                        p_i+=1
                    all_addresses.append(str(int(temp_addr,2)))
            for a in all_addresses:
                mem[a] = val
    sum = 0
    #print(mem)
    for k in mem.keys():
        sum += mem[k]
    print(sum)
            



