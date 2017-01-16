# Enter your code here. Read input from STDIN. Print output to STDOUT
n,s = raw_input().strip().split(' ')
n,s = [int(n),int(s)]
d = [int(i) for i in raw_input().split()]
d.rotate(s)
print d