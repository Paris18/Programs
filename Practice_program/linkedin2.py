n = input("enter no of inputs : ")
a=[]
for i in range (0,n):
	a.append(input())
for i in range (0,n):
	b = bin(a[i])[2:].zfill(32)
	b_str = ''.join('1' if x == '0' else '0' for x in b)
	print int(b_str,2)