cnt = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        splitted = l.split(':')
        password = splitted[1].strip()
        policy_split = splitted[0].split(' ')
        policy_low = int(policy_split[0].split('-')[0]) - 1
        policy_high = int(policy_split[0].split('-')[1]) - 1
        policy_char = policy_split[1]
       
        if ((password[policy_low] == policy_char and password[policy_high] != policy_char) or \
            (password[policy_low] != policy_char and password[policy_high] == policy_char)):
            cnt+=1
print(cnt)