from itertools import permutations
n = input()
d = []
for i in range(0,n):
    a = raw_input()
    d.append(a)
for i in d:
    brk = False
    chk = True
    perms = [''.join(p) for p in permutations(i)]
    perms.sort()
    for j in perms:
        if i < j :
            print j
            brk = True
            chk = False
        if brk:
            break
    if chk:
        print "no answer"
        chk = False