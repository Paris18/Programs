n = input()
d,q = {},[]
for i in range(0,n):
    name ,number = raw_input().strip().split(' ')
    d[name] = number
print d 
while True:
    query = raw_input()
    if query == '':
        break
    q.append(query)
for i in q:
    if i in d.keys():
        print "%s=%s" % (i,d[i])
    else:
        print "Not found"