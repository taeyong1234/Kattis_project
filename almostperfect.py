import sys
import math

def sum_factorizing(num):

    first = 2
    sum_factors = 1
    nn = math.sqrt(num)
    if nn == int(nn):
        sum_factors += nn


    while(first**2 < num):
        if num % first == 0:
            sum_factors += first + num//first
        first += 1
    return sum_factors

def mai(number):

    sumvalue = sum_factorizing(number)

    if number == sumvalue:
        print(number , "perfect")
    elif abs(number - sumvalue) <= 2:
        print(number , "almost perfect")
    else:
        print(number, "not perfect")


if __name__ == '__main__':
    for line in sys.stdin:
        number = int(line)
        mai(number)