no_process = input()
cl_order = [int(x) for x in raw_input().split()]
id_order = [int(x) for x in raw_input().split()]
count = 0

def rotate(l , n = 1):
	return l[n:]+l[:n]


while(no_process > 0):
	if(id_order[0] == cl_order[0]):
		count += 1
		no_process -=1 
		cl_order = rotate(cl_order)
		id_order = rotate(id_order)
	else:
		count +=1
		cl_order = rotate(cl_order)
print count