n = input("enter size of array : ")
k = input("enter k value : ")
value,a = 0,[]
print "enter your numbers press enter after each element:"
for i in range(0,n):
	a.append(input())
for i in range(0,n-1):
	for j in range(i+1,n):
		if((a[i]+a[j]) % k == 0):value +=1
print "output: %d " %value