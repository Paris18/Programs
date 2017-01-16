import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    s = []
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    for i in range(1,n+1):
        s.append(i)
    maxi = 0
    for i in range(0,n-1):
        for j in range(1+i,n):
            x = s[i] & s[j]
            if((x < k) & ( x > maxi )):
                maxi = x
    print maxi
