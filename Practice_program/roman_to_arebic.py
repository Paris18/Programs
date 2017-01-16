
def roman_to_no(n):
    roman_value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    n = n.upper()
    total = 0
    while n:
        if len(n) == 1 or roman_value[n[0]] >= roman_value[n[1]]:
            total += roman_value[n[0]]
            n = n[1:]
        else:
            total += roman_value[n[1]] - roman_value[n[0]]
            n = n[2:]
    return total



def no_to_roman(n):
    # if n % 1 != 0 :
    #     print "roman does not support for fractions"
    #     return 
    returnstring=''
    # roman_value = [['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    
    for i in roman_value.keys():
        while n - roman_value[i] >= 0:
            n -= roman_value[i]
            returnstring += i
    return returnstring

import re
qry = raw_input()
oprtr = re.sub(r'[IVXLCDM]','',qry).strip()
roman_no = ['I','X','V','X','L','C','D','M']
qryl = [x.strip() for x in qry.split(oprtr)]
q = str(roman_to_no(qryl[0])) + oprtr + str(roman_to_no(qryl[1]))
rst = eval(q)

# if '+' in qry :
#     rst = roman_to_no(qryl[0]) + roman_to_no(qryl[1])
# elif '-' in qry:
#     rst = roman_to_no(qryl[0]) - roman_to_no(qryl[1])
# elif '/' in qry:
#     rst = roman_to_no(qryl[0]) / roman_to_no(qryl[1])
# elif '*' in qry:
#     rst = roman_to_no(qryl[0]) * roman_to_no(qryl[1])
# elif '%' in qry:
#     rst = roman_to_no(qryl[0]) % roman_to_no(qryl[1])
print no_to_roman(rst)