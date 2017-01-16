Num = {"ZERO":0,"ONE":1,"TWO":2,"THREE":3,"FOUR":4,"FIVE":5,"SIX":6,"SEVEN":7,"EIGHT":8,"NINE":9}
n = {}
m = []
no_case = input()
for i in range(0,no_case):
    test_case = input()
    if(test_case % 2 == 0):
        print "wrong formate"
    else:
        m.append(test_case)
        n[i] =raw_input().split(' ')
for i in range(0,no_case):
    sumn = Num[n[i][0]]
    for j in range(0,m[i]):
        if j % 2 != 0:
            if n[i][j] == 'PLUS':
                sumn += Num[n[i][j+1]]
            if n[i][j] == 'MINUS':
                sumn -= Num[n[i][j+1]]
    print sumn