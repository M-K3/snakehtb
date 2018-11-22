#!/usr/bin/python2.7
import random
lr = 'lr'
print '''
___________.__               _________              __
\__    ___/|  |__   ____    /   _____/ ____ _____  |  | __ ____
  |    |   |  |  \_/ __ \   \_____  \ /    \\__  \ |  |/ // __ \
  |    |   |   Y  \  ___/   /        \   |  \/ __ \|    <\  ___/
  |____|   |___|  /\___  > /_______  /___|  (____  /__|_ \\___  >
                \/     \/          \/     \/     \/     \/    \/

'''
chains = [0x74, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 0x74, 0x72, 0x6f, 0x6c, 0x6c]
db = 'db'
ef = 'ef'
chars = []
keys = [0x70, 0x61, 0x73, 0x73, 0x77, 0x6f, 0x72, 0x64, 0x21, 0x21]
nn = 'nn'
lock_pick = random.randint(0, 0x3e8)
lock = lock_pick * 2
password = [0x69, 0x74, 0x73, 0x20, 0x6e, 0x6f, 0x74, 0x20, 0x74, 0x68, 0x61, 0x74, 0x20, 0x65, 0x61, 0x73, 0x79]
lock = lock + 10
ty = 'ty'
lock = lock / 2
auth = [0x6b, 0x65, 0x65, 0x70, 0x20, 0x74, 0x72, 0x79, 0x69, 0x6e, 0x67]
lock = lock - lock_pick
gh = 'gh'
print 'The Snake Created by 3XPL017'
print 'Your number is ' + str(lock_pick)
for key in keys:
    keys_encrypt = lock ^ key
    chars.append(keys_encrypt)
for chain in chains:
    chains_encrypt = chain + 0xA
    chars.append(chains_encrypt)
aa = 'aa'
rr = 'rr'
slither = aa + db + nn + ef + rr + gh + lr + ty
print 'Authentication required'
print ''
user_input = raw_input('Enter your username\n')
if user_input == slither:
    pass

else:
    print 'Wrong username try harder'
    exit()
pass_input = raw_input('Enter your password\n')
for passes in pass_input:
    for char in chars:
        if passes == str(chr(char)):
            print 'Good Job'
            break
        else:
            print 'Wrong password try harder'
            exit(0)
    break
