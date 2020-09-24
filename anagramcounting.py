'''
1. inputs by sys.line()
2. count the numbers of each word
3. count how many time each word is repeated
4. calculate factorial
5. return the result
'''

import sys
from functools import reduce

def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    if n == 1:
        return 1

for line in sys.stdin:
    number_info = {}
    alist = line.split()[0]
    total_number = len(alist)
    for i in range(total_number):
        if alist[i] in number_info:
            number_info[alist[i]] += 1
        else:
            number_info[alist[i]] = 1
    num = factorial(total_number)
    dec_list = list(filter(lambda z : z > 1,number_info.values()))
    dec_fac = list(map(lambda i : factorial(i),dec_list))

    if len(dec_fac) == 0:
        print(num)
    else:
        dec = reduce((lambda x,y:x*y),dec_fac)
        print(num//dec)