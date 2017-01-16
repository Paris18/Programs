n = input()

ord_dl = []
qry = 0
for i in range(0,n):
	a = [int(x) for x in raw_input().split()]
	if(len(a)<2):
		ord_dl.append(a[0])
		qry += 1
	else:
		ord_dl.append(a[1])
i = 0
while(qry > 0):
	if (ord_dl[i] == 1):
		qry -= 1
		k = i - 1
		while(k >= 0):
			if (ord_dl[k] != 1):
				print ord_dl[k]
				ord_dl.remove(ord_dl[i])
				ord_dl.remove(ord_dl[k])
				break
		else:
			print "No Food"
			ord_dl.remove(ord_dl[i])
			n -= 1
		i = 0

	else:
		i += 1