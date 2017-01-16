n = input()
value,position,a,sum_af=[],[],[],0
for i in range(0,n):
    a= [raw_input().split()]
    value.append(int(a[0]))
    position.append(int(a[1]))
for i in range(0,n):
    for j in range(0,n):
        if(i == j):
            sum_af += (max(position[i],position[j]) - min(position[i],position[j]))*max(value[i],value[j])

print sum_af