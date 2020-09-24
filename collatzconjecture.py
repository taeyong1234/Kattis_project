
import sys


def odd(n):
    return int(3*n+1)

def even(n):
    return int(n/2)

while(True):

    inp = sys.stdin.readline().split()
    first = int(inp[0])
    second = int(inp[1])
    if first == 0  and second  == 0:
        break

    first_input = {first: 0}
    second_input = {second: 0}
    n = 0
    k = 0

    while (first != 1 and first > 1):
        n += 1
        if first % 2 == 0:
            first_input[even(first)] = n
            first = even(first)
        else:
            first_input[odd(first)] = n
            first = odd(first)

    while (True):

        if second in first_input:
            print('{} needs {} steps, {} needs {} steps, they meet at {}'.format(int(inp[0]), first_input[second], int(inp[1]), k, second))
            break

        k += 1

        if second % 2 == 0:
            second_input[even(second)] = k
            second = even(second)
        else:
            second_input[odd(second)] = k
            second = odd(second)

